
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from mysite import views
from mysite.views import (tourist_login, tourist_register, tourist_logout )

urlpatterns = [

url(r'^admin/', admin.site.urls),
url(r'^mysite/', include("mysite.urls", namespace="mysite")),
url(r'^mysite/tourists/', include("mysite.urls")),
url(r'^mysite/list/touristlogin/$', views.tourist_login, name='tourist_login'),  # tourist login page saperate
url(r'^touristregister/', tourist_register, name="tourist_register" ),
url(r'^mysite/list/touristregister/', tourist_register, name="tourist_register" ),

#url(r'^touristcreate/', tourist_create, name="tourist_create" ),
url(r'^touristlogin/', tourist_login, name="tourist_login" ),
url(r'^touristlogout/', tourist_logout, name="tourist_logout" ),
url(r'^mysite/touristlist/touristcreate/$', views.tourist_create, name='tourist_create'),


#url(r'^mysite/$', "mysite.views.site_home"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
