from django.conf.urls import url

from .views import (
        cart_home, 
        cart_update, 
        success,
        checkout_done_view
        )

urlpatterns = [
    url(r'^$', cart_home, name='home'),
    url(r'^checkout/success/$', checkout_done_view, name='success'),
    url(r'^checkout/$', success, name='checkout'),
    url(r'^update/$', cart_update, name='update'),
]