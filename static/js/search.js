'use strict';

export function start() {
    const advanced_search = $('#advanced_search');
    const adv_search_link = $('#show_advanced_search');

    // Only show advanced search fields if one of them has been filled in
    let advanced_search_fields_all_empty = true;
    for (const field of ['#title', '#text', '#author', '#recipient', '#cced',
                         '#min_year', '#max_year', '#doc_type_selector']) {

        if (field === '#doc_type_selector') {
            if (($(field).val()).length) {
                advanced_search_fields_all_empty = false;
            }
        } else if ($(field).val()) {
            advanced_search_fields_all_empty = false;
        }
    }

    if (advanced_search_fields_all_empty) {
        advanced_search.hide();
    } else {
        adv_search_link.remove();
    }

    adv_search_link.click(() => {
        advanced_search.show();
        adv_search_link.remove();
    });

    setup_refine_search();
}


export function setup_refine_search() {

    const refine_author = $("a[id^='refine_author:']"); // elements whose id starts with 'refine_author'
    for (const el of refine_author) {
        $(el).click(() => {
            const new_author = el.id.split(":")[1];
            const existing_authors = $('#author').val();
            const updated_authors = add_facet(existing_authors, new_author);
            if (updated_authors) {
                $('#author').val(updated_authors);
                $('#search').submit();
            }
        });
    }

    const refine_recipient = $("a[id^='refine_recipient:']"); // elements whose id starts with 'refine_recipient'
    for (const el of refine_recipient) {
        $(el).click(() => {
            const new_recipient = el.id.split(":")[1];
            const existing_recipients = $('#recipient').val();
            const updated_recipients = add_facet(existing_recipients, new_recipient);
            if (updated_recipients) {
                $('#recipient').val(updated_recipients);
                $('#search').submit();
            }
        });
    }

    const refine_cced = $("a[id^='refine_cced:']"); // elements whose id starts with 'refine_cced'
    for (const el of refine_cced) {
        $(el).click(() => {
            const new_cced = el.id.split(":")[1];
            const existing_cced = $('#cced').val();
            const updated_cced = add_facet(existing_cced, new_cced);
            if (updated_cced) {
                $('#cced').val(updated_cced);
                $('#search').submit();
            }
        });
    }

    const refine_year = $("a[id^='refine_year:']"); // elements whose id starts with 'refine_year'
    for (const el of refine_year) {
        $(el).click(() => {
            const year = parseInt(el.id.split(":")[1]);
            $('#min_year').val(year);
            $('#max_year').val(year);
            $('#search').submit();
        });
    }
}


function add_facet(existing_facets, new_facet) {
    // When the user clicks on a search facet to refine their search
    // this appends that new facet to the existing facets.
    // Returns false if the new facet isn't actually new, so we can
    // check for false above and not actually submit a new search.
    
    if (!existing_facets) {
        return new_facet;
    } else if (existing_facets.includes(new_facet)) {
        return false;
    } else {
        return existing_facets + " AND " + new_facet;
    }
}

