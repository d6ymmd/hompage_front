from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('notice/', views.notice_list, name='notice'),
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('photo/', views.photo_list, name='photo_list'),
    path('address/', views.address, name='address'),
    path('practice/', views.practice, name='practice'),
    path('photo/detail/', views.photo_detail, name='photo-detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
