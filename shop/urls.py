from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name = "shop"
from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path("", views.index, name="Shophome"),
    # path('', TemplateView.as_view(template_name='social_app / index.html')),

    path("contact/", views.contact, name="AboutUs"),
    path("search/", views.search, name="search"),
    path("products/<int:myid>", views.productview, name="product"),
    path("login/", views.loginsystem, name="login"),
    path("register/", views.signupsys, name="register"),
    path("yourcart/", views.yourcart, name="yourcart"),
    path("categorywise/", views.categorywise, name="categorywise"),
    path("logout/", views.logout_view, name="logout"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]
