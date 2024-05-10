from django.contrib import admin
from django.urls import path
from my_work import views

urlpatterns = [
    path("home/",views.HomePage.as_view(),name="home_1"),
    path("add/",views.AddUser.as_view(),name="add"),
    path("login/",views.CustomLoginView.as_view(),name="lgn"),
    path("createbin/",views.CreateGarbage.as_view(),name="create_garbage"),
    path("updatebin/<int:pk>",views.UpdateBin.as_view(),name="update_garbage"),
    path("deletebin/<int:pk>",views.DeleteBin.as_view(),name="delete_garbage"),
    path("publiclist/",views.UsersList.as_view(),name="userlist")
]