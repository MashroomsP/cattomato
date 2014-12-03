from django.conf.urls import  patterns, include, url
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Entry

info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'created',
}

sitemaps = {
    'blog': GenericSitemap(info_dict, priority=0.6),
}
    
urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^', include('blog.urls')),
    )