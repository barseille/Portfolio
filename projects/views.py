from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from django.shortcuts import render
from .models import Project
from .serializers import ProjectSerializer
from django.shortcuts import get_object_or_404
from portfolio.models import User
from datetime import datetime


class ProjectViewSet(ModelViewSet):
    """
    ViewSet pour la gestion des projets.
    """
    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        """
        Obtient les permissions en fonction de l'action.
        Les administrateur ont toutes les permissions, les autres ont un accès en lecture seule.
        """
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [AllowAny]
        return super(ProjectViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        """
        Liste tous les projets et les affiche dans le modèle de base.
        Inclut l'utilisateur et l'année en cours dans le contexte.
        """
        queryset = self.get_queryset()
        serializer = ProjectSerializer(queryset, many=True)
        try:
            user = User.objects.get(username='Barseille')
        except User.DoesNotExist:
            user = None 
        context = {'projects': serializer.data, 'user': user, 'year': datetime.now().year}
        return render(request, 'base.html', context)
    
    def retrieve(self, request, pk=None):
        """
        Récupère un seul projet par clé primaire et l'affiche dans le modèle de détail du projet.
        """
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return render(request, 'projects/project_detail.html', {'project': serializer.data})
    