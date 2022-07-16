"""courseedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('accounts/login',auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('accounts/logout',auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/siteadmin/',views.siteadminView, name='siteadmin'),
    path('accounts/siteadmin/add',views.addcategory, name='addcategory'),
    path('accounts/siteadmin/view/<id>',views.viewcategory, name='view-entry'),
    path('accounts/siteadmin/edit/<id>',views.editcategory, name='edit-entry'),
    path('accounts/siteadmin/<id>',views.deletecategory, name='delete-entry'),
    path('accounts/siteadmin#show',views.showentry, name='showentry'),
    path('accounts/siteadmin#hide',views.hideentry, name='hideentry'),
    path('accounts/siteadmin#delete',views.deleteselected, name='deleteselected'),
    path('accounts/siteadmin#deselectall',views.resetselection, name='resetselection'),
    path('accounts/siteadmin#selectall',views.selectallentry, name='selectallentry'),
    path('accounts/siteadmin/select/<id>',views.select, name='select-entry'),
    path('accounts/siteadmin/deselect/<id>',views.deselect, name='deselect-entry'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
