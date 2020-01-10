from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from accounts import views
# from newsletter.urls import subscription, unsubscription 

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
 	path(r'^newsletter$', TemplateView.as_view(template_name='newsletter.html'), name='newsletter'),
 	path(r'^aboutus$', TemplateView.as_view(template_name='aboutus.html'), name='aboutus'),
 	# url(r'^newsletter/', include('newsletter.urls')),
]
