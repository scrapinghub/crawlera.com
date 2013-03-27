from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

def site(name, pattern=None, template=None, **kwargs):
    if pattern is None: pattern = '^{0}\.html'.format(name)
    if template is None: template = 'site/{0}.html'.format(name)

    if not pattern.startswith('^'): pattern = '^' + pattern
    if not pattern.endswith('$'): pattern += '$'

    kwargs.update(dict(
        template = template,
    ))
    return url(pattern, 'direct_to_template', kwargs, name=name)

urlpatterns = patterns('django.views.generic.simple',
    site('home', pattern = ''),
    site('about'),
    site('pricing'),
    site('api'),
    site('faq'),
    site('examples'),
    # Examples:
    # url(r'^$', 'crawlera.views.home', name='home'),
    # url(r'^crawlera/', include('crawlera.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
