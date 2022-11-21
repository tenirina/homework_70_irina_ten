from rest_framework import serializers

from webapp.models import Project, Issue


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'started_at', 'finished_at', 'title', 'description', 'users')
        read_only_fields = ('id', 'started_at')


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'summary', 'description', 'status', 'type', 'project')
        read_only_fields = ('id', 'summary', 'project')
