from django.urls import path

from . import views

urlpatterns=[

    path('razor/<str:uuid>/',views.RazorPayView.as_view(),name='razorpay'),

    path('payment-verify/',views.PaymentVerifyView.as_view(),name='payment-verify'),
]