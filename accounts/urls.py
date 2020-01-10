from django.conf.urls import url
from accounts import views
# from newsletter import subscription, unsubscription

urlpatterns = [

    url(r'^login/$', views.login_and_signup, name='login_and_signup'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^home/$', views.home, name='home'),
    url(r'^bmiform/$', views.bmiform, name='bmiform'),

]
