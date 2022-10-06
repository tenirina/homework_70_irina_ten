from django.db import models


class Issue(models.Model):
    summary = models.CharField(verbose_name='Summary', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name="Description", max_length=1000, null=True)
    status = models.ForeignKey(verbose_name='Status', to='webapp.Status', null=False, blank=False, related_name='issue', on_delete=models.RESTRICT, default='new')
    type = models.ForeignKey(verbose_name='Type', to='webapp.Type', null=False, blank=False, related_name='issue', on_delete=models.RESTRICT, default='task')
    created_at = models.DateTimeField(verbose_name='Date of created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date of updates', auto_now=True)
