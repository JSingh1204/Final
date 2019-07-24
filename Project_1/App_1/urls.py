
from django.urls import path

from . import views
from django.views.generic import TemplateView

urlpatterns = [
				#path('App_1',views.index,name='index'),
				path('App_1/register',views.register,name='register'),
				path('App_1/user_logged', views.user_logged, name='user_logged'),
				path('App_1/user_out',views.user_out,name='user_out'),
				path('App_1/welcome',views.welcome,name='welcome'),
				#path('App_1/index.html', TemplateView.as_view(template_name='App_1/index.html'), name='index'),
				]

