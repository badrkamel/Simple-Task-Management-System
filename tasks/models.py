from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Task(models.Model):

    user = models.ForeignKey(
        UserModel, 
        related_name='users', 
        on_delete=models.CASCADE, 
        verbose_name=_('User')
    )

    title = models.CharField(_('Title'), max_length=100)
    description = models.TextField(_('Description'))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    completed = models.BooleanField(_('Completed'), default=False)

    class Meta:
        ordering = ('title', )
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
   
    def __str__(self):
        return str(self.title)