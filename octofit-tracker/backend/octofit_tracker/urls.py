import os
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

codespace = os.environ.get('CODESPACE_NAME')
if codespace:
    root_target = f"https://{codespace}-8000.app.github.dev/api/"
else:
    root_target = '/api/'

urlpatterns = [
    path('', RedirectView.as_view(url=root_target)),
    path('admin/', admin.site.urls),
    path('api/', include('octofit_tracker.tracker.urls')),
]
