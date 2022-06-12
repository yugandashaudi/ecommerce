from django.urls  import path
from .import views 
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns=[
    path('',views.home,name="home"),
    path('checkout/',views.checkout,name="checkout"),
    path('shipping/',views.shipping,name='shipping'),
    path('payment/',views.payment,name='payment'),
    path('failed/',views.failed,name='failed'),
    path('verify/',views.verify,name='verify')
]+static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)