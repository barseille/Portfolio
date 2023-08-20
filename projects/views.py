from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from django.shortcuts import render
from .models import Project
from .serializers import ProjectSerializer
from django.shortcuts import get_object_or_404
from portfolio.models import User

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super(ProjectViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProjectSerializer(queryset, many=True)
        user = User.objects.get(username='barseille') 
        context = {'projects': serializer.data, 'user': user}
        return render(request, 'base.html', context)
    
    def retrieve(self, request, pk=None):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return render(request, 'projects/project_detail.html', {'project': serializer.data})
    

