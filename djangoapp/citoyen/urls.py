from citoyen import views

from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, re_path
urlpatterns=[

                re_path(r'^citoyen$',views.citoyenApi),
                re_path(r'^citoyen/([0-9]+)$',views.citoyenApi),


            ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)