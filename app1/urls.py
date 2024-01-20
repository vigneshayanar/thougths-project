from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.frontpage,name='fronpage'),
    path('signup/',views.siginup,name='signup'),
        path('login/',auth_views.LoginView.as_view(template_name='app1/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout')

]