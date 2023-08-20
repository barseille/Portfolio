# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from projects.views import ProjectViewSet

# router = DefaultRouter()
# router.register(r'projects', ProjectViewSet)

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('', include(router.urls)),
# ]

from django.contrib import admin
from django.urls import path
from projects.views import ProjectViewSet
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', ProjectViewSet.as_view({'get': 'list'}), name='project-list'), # Note le changement ici
]




if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)