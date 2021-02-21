from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('app_accounts.urls')),
    path('entities/', include('app_entities.urls')),
    path('projects/', include('app_projects.urls')),
]
