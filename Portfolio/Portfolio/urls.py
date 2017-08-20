"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from gallery.views import Display_Gallery
from gallery.views import Display_About_Page
from gallery.views import Display_Contact_Page
from gallery.views import Display_Details_Page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Homepage/', Display_Gallery, name='Display_Gallery'),
    url(r'^About/', Display_About_Page, name='Display_About_Page'),
    url(r'^Contact/', Display_Contact_Page, name='Display_Contact_Page'),
    url(r'^(?P<gallery_id>[0-9]+)/Details/$', Display_Details_Page, name='Display_Details_Page'),
    url(r'^$', Display_Gallery, name='Display_Gallery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
