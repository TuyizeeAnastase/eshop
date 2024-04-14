from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('login',views.user_login,name='login'),
    path('signup',views.register,name='register')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

