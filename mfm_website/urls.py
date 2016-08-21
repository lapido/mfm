from django.conf.urls import url
from . import views

app_name = 'mfm_website'
urlpatterns = [
	url(r'^$', views.index, name='index'),	
	url(r'^blog/', views.blog, name='blog'),
]
