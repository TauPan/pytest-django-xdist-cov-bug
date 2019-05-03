from django.contrib import admin
from django.conf.urls import url

from app import views

urlpatterns = [
    url('', views.home, name='home'),
    url('admin/', admin.site.urls),
]
