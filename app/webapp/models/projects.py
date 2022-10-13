from django.db import models


class Project(models.Model):
    started_at = models.DateField(verbose_name='Date of started', null=False)
    finished_at = models.DateField(verbose_name='Date of finished', null=True)
    title = models.CharField(verbose_name='Titile', max_length=50, null=False, blank=False)
    description = models.TextField(verbose_name="Description", max_length=1000, null=True)
    created_at = models.DateTimeField(verbose_name='Date of created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date of updates', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Date of delete', null=True, default=None)
    is_deleted = models.BooleanField(verbose_name="Delete", default=False, null=False)
