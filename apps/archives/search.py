import re
from collections import Counter

from django.db.models import Q

from .models import Person, Document, Folder, Organization


def process_search(search_params):
    """
    Processes one search request and returns the search_results as a queryset

    :param search_params:
    :return:
    """

    keywords = search_params.get('keyword')
    title = search_params.get('title')
    text = search_params.get('text')
    author = search_params.get('author')
    recipient = search_params.get('recipient')
    cced = search_params.get('cced')
    min_year = search_params.get('min_year')
    max_year = search_params.get('max_year')

    if not (keywords or title or text or author or recipient or cced or min_year or max_year):
        return None
    else:
        docs_qs = Document.objects.all()
        people_qs = Person.objects.none()

    if keywords:
        # construct keyword list, extracting exact search phrases 
        keywordlist = []
        exact_searches = re.findall(r'"([^"]+)"', keywords)
        if exact_searches:
            for phrase in exact_searches:
                keywords = re.sub(f'"{phrase}"', '', keywords)  # strip exact search search terms out
        keywordlist.extend(exact_searches)
        keywordlist.extend(keywords.split())

        temp_people_Q = Q()
        for word in keywordlist:
            temp_people_Q |= Q(first__icontains=word)
            temp_people_Q |= Q(last__iexact=word)
            people_qs = Person.objects.filter(Q(first__icontains=word) | Q(last__iexact=word))
            organization_objs = Organization.objects.filter(Q(name__icontains=word))

            doc_Q = Q(title__icontains=word)
            for person in people_qs:
                doc_Q |= Q(author_person=person)
                doc_Q |= Q(recipient_person=person)
                doc_Q |= Q(cced_person=person)
            for org in organization_objs:
                doc_Q |= Q(author_organization=org)
                doc_Q |= Q(recipient_organization=org)
                doc_Q |= Q(cced_organization=org)

            docs_qs = docs_qs.filter(doc_Q)

        people_qs = Person.objects.filter(temp_people_Q)

    if title:
        docs_qs = docs_qs.filter(Q(title__icontains=title))

    if text:  # full text search
        words_q = Q()

        # handle exact search terms wrapped in " or '
        exact_searches = re.findall(r'"([^"]+)"', text)
        if exact_searches:
            for phrase in exact_searches:
                words_q &= Q(text__icontains=phrase)
                text = re.sub(f'"{phrase}"', '', text)  # strip exact search search terms out

        # handle all leftover text
        words = text.split()
        for word in words:
            words_q &= Q(text__icontains=word)
        docs_qs = docs_qs.filter(words_q)

    if author:
        for names in author.split(" AND "):
            author_q = Q()
            for name in names.split():
                if len(name) > 2:
                    author_q |= Q(author_person__first__icontains=name)
                    author_q |= Q(author_person__last__icontains=name)
                    author_q |= Q(author_organization__name__icontains=name)
            docs_qs = docs_qs.filter(author_q)

    if recipient:
        for names in recipient.split(" AND "):
            rec_q = Q()
            for name in names.split():
                if len(name) > 2:
                    rec_q |= Q(recipient_person__first__icontains=name)
                    rec_q |= Q(recipient_person__last__icontains=name)
                    rec_q |= Q(recipient_organization__name__icontains=name)
            docs_qs = docs_qs.filter(rec_q)

    if cced:
        for names in cced.split(" AND "):
            cced_q = Q()
            for name in names.split():
                if len(name) > 2:
                    cced_q |= Q(cced_person__first__icontains=name)
                    cced_q |= Q(cced_person__last__icontains=name)
                    cced_q |= Q(cced_organization__name__icontains=name)
            docs_qs = docs_qs.filter(cced_q)

    doc_types = search_params.getlist('doc_type')
    # if a key points to a list of values, querydict.get() just returns the last item in the list!
    # https://docs.djangoproject.com/en/2.1/ref/request-response/#django.http.QueryDict.__getitem__
    if doc_types:
        docs_qs = docs_qs.filter(type__in=doc_types)

    if not min_year:
        min_year = 1900
    if not max_year:
        max_year = 2000

    # TODO: this will break if we can't cast these to int - fine for now
    # bc we validate in the frontend
    min_year = int(min_year)
    max_year = int(max_year)
    docs_qs = docs_qs.filter(Q(date__year__gte=min_year) &
                             Q(date__year__lte=max_year))

    # prevents template from hitting the db
    docs_qs = docs_qs.prefetch_related('author_person', 'author_organization', 'folder',
                                       'recipient_person', 'recipient_organization',
                                       'cced_person','cced_organization')

    docs_qs.order_by('date')

    search_facets = generate_search_facets(docs_qs)
    return docs_qs, people_qs, search_facets


def generate_search_facets(doc_objs):
    """
    Creates a dictionary of facets with keys of each of the different facets and values that are a list of tuples that
     contain the top 10 most common instances of the facet and how many times these instances occur.
    :param doc_objs:
    :return: dict_facets
    """

    counter_authors = Counter()
    counter_dates = Counter()
    counter_recipients = Counter()
    counter_cceds = Counter()

    for document in doc_objs.all():
        # Some dates are None --> Skip those documents
        if document.date:
            counter_dates[document.date.year] += 1
        for author in document.author_person.all():
            counter_authors[str(author)] += 1
        for org in document.author_organization.all():
            counter_authors[org.name] += 1
        for recipient in document.recipient_person.all():
            counter_recipients[str(recipient)] += 1
        for org in document.recipient_organization.all():
            counter_recipients[org.name] += 1
        for cc in document.cced_person.all():
            counter_cceds[str(cc)] += 1
        for org in document.cced_organization.all():
            counter_cceds[org.name] += 1

    dict_facets = {
        "authors": counter_authors.most_common(10),
        "recipients": counter_recipients.most_common(10),
        "cceds": counter_cceds.most_common(10),
        "years": counter_dates.most_common(10),
    }
    return dict_facets

