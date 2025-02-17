from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage.as_view(),name='homepage'),
    path('details/<slug:slug>/',views.meetup_details,name='post_details'),
    path('details/<slug:slug>/registration',views.registration.as_view(),name='registration'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)