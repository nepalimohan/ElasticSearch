from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Books
from .documents import BookDocument

#this code is not required. elasticsearch automatically updates indexupon CRUD

@receiver(post_save, sender=Books)
def update_document(sender, instance, **kwargs):
    BookDocument().update(instance)

@receiver(post_delete, sender=Books)
def delete_document(sender, instance, **kwargs):
    BookDocument().delete(instance)
