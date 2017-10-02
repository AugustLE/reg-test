from django.conf.urls import url

from . import views

app_name = 'home'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^behandling/$', views.TreatmentView.as_view(), name='treatment'),
    url(r'^voksne/$', views.VoksneView.as_view(), name='voksne'),
    url(r'^priser/$', views.PriceView.as_view(), name='prices'),
    url(r'^om-oss/$', views.AboutView.as_view(), name='about'),
    url(r'^kontakt/$', views.ContactView.as_view(), name='contact'),


]
