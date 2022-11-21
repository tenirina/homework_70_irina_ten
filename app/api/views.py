import json

from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProjectSerializer, IssueSerializer
from webapp.models import Project, Issue


class ProjectListView(APIView):

    def get(self, request, *args, **kwargs):
        objects = Project.objects.all()
        serializer = ProjectSerializer(objects, many=True)
        return Response(serializer.data)


class ProjectDetailView(APIView):

    def get(self, request, *args, **kwargs):
        project = Project.objects.filter(pk=kwargs.get('pk'))[0]
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class ProjectUpdateView(APIView):

    def put(self, request, *args, **kwargs):
        project = Project.objects.filter(pk=kwargs.get('pk'))[0]
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDeleteView(APIView):

    def delete(self, request, *args, **kwargs):
        project = Project.objects.filter(pk=kwargs.get('pk'))[0]
        pk_project = project.pk
        project.delete()
        return Response(pk_project, status=status.HTTP_204_NO_CONTENT)



