from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('product/<int:product_id>/',views.product,name='product_detail'),
    path('search',views.search,name='search'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)