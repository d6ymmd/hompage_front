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

    # 데이터 넣기전
    path('photo/detail/', views.photo_detail, name='photo-detail'),
    # 데이터 넣은 후
    # path('photo/<int:pk>/', views.photo_detail, name='photo-detail'),
    # 폴라로이드 다른버전_연습
    path('photo/detail2/', views.photo_detail2, name='photo-detail2'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
