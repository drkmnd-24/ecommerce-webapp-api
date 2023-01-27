from django.urls import path, include

from api_core.views import *


urlpatterns = [
    path('customer/', CustomerView.as_view(), name='customer'),
    path('address/', AddressView.as_view(), name='address-view'),

    path('address/<int:pk>/', AddressDetail.as_view(), name='address-detail'),
    path('category/', CategoryViews.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
]
