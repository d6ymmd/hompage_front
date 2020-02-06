from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('notice/', views.notice_list, name='notice'),
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('portfolio2/', views.portfolio_list2, name='portfolio2'),
    path('jsscript/', views.jsscript, name='jsscript'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
