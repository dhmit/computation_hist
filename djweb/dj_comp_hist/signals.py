from .models import Document, Page
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Document)
def create_pages(sender, instance, **kwargs):
    print("Signal called")
    if instance.last_page != 0:
        for i in range(1, instance.number_of_pages +1):
            if Page.objects.filter(document=instance, page_number=i):
                pass
            else:
                new_page = Page(document=instance, page_number=i)
                new_page.save()
