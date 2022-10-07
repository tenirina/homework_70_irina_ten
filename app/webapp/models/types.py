from django.db import models


class Type(models.Model):
    title = models.CharField(verbose_name='Type', max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Date of created', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date of updates', auto_now=True)


class IssueType(models.Model):
    issue = models.ForeignKey('webapp.Issue', related_name='issue_types', on_delete=models.CASCADE, verbose_name='Issue')
    type = models.ForeignKey('webapp.Type', related_name='type_issues', on_delete=models.CASCADE, verbose_name='Types')
