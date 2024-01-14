from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/tunetracker/songs/'), name='root_redirect'),
    path('admin/', admin.site.urls),
    path('tunetracker/', include('TuneTracker.urls')),
]
