from django.db import models


class Status(models.Model):
    title = models.CharField(verbose_name='Status', max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Date of created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date of updates', auto_now=True)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.title