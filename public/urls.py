from django.contrib import admin
from django.urls import path
from public import views

urlpatterns = [
    path("home/",views.HomePage.as_view(),name="home_2"),
    path("request_bin/",views.RequestBin.as_view(),name="request_bin"),
    path("complaint/",views.CustmoerComplaint.as_view(),name="complaint"),
    path('pending-requests/', views.PendingRequestsView.as_view(), name='pending_requests'),
    path('accept-request/<int:pk>/', views.AcceptRequestView.as_view(), name='accept_request'),
    path('reject-request/<int:pk>/', views.RejectRequestView.as_view(), name='reject_request'),
    path('pending-re/', views.pending_requests_view, name='pending_requests'),

]
