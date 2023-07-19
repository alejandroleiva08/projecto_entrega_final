from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from .views import index

app_name = "CORE"

urlpatterns = [
    path('',index, name="index"),
]

urlpatterns += staticfiles_urlpatterns()