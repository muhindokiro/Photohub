from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^photo/(\d+)',views.photo,name ='photo')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

