from django.contrib import admin
from django.urls import path, include
from users_office.views import *
from test_app.yasg import urlpatterns as new_url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('all/users/', UserListView.as_view()),
    path('admin', admin.site.urls),
    path('drf-auth', include('rest_framework.urls')),
    path('registration/', RegistrUserView.as_view()),
    path('update/', UserUpdate.as_view()),
    path('user/one/', UserOne.as_view()),
    path('add/new_office/', AddNewOffice.as_view()),
    path('office_all/', OfficeAll.as_view()),
]
urlpatterns += new_url

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)