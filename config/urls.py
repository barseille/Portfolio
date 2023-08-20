from django.contrib import admin
from django.urls import path
from projects.views import ProjectViewSet
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', ProjectViewSet.as_view({'get': 'list'}), name='project_list'),
    path('projects/<int:pk>/', ProjectViewSet.as_view({'get': 'retrieve'}), name='project_detail'), # Ligne ajoutée
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
