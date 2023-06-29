from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('processadd', views.processadd, name='processadd'),
    path('<int:user_id>/detail/', views.detail, name='detail'),
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
