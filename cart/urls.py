from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('cart',views.cart,name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)