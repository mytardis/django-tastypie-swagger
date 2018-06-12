try:
    from django.conf.urls import include, url
except ImportError:
    from django.conf.urls.defaults import include, url

from .views import SwaggerView, ResourcesView, SchemaView

app_name = 'tastypie_swagger'

urlpatterns = [
    url(r'^$', SwaggerView.as_view(), name='index'),
    url(r'^resources/$', ResourcesView.as_view(), name='resources'),
    url(r'^schema/(?P<resource>\S+)$', SchemaView.as_view()),
    url(r'^schema/$', SchemaView.as_view(), name='schema'),
]
