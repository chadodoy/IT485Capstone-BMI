from django.conf.urls import url
from accounts import views
from newsletter import subscription, unsubscription

urlpatterns = [
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^newsletter/$', views.login_and_signup, name='login_and_signup'),

]
