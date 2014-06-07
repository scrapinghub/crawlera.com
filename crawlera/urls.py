from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic.base import RedirectView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

def site(name, pattern=None, template=None, **kwargs):
    if pattern is None: pattern = '^{0}'.format(name)
    if template is None: template = 'site/{0}.html'.format(name)

    if not pattern.startswith('^'): pattern = '^' + pattern
    if not pattern.endswith('$'): pattern += '$'

    kwargs.update(dict(
        template = template,
    ))
    return url(pattern, 'direct_to_template', kwargs, name=name)

urlpatterns = patterns('django.views.generic.simple',
    site('home', pattern = ''),
    url(r'^features/$'  , RedirectView.as_view(url='http://scrapinghub.com/crawlera#features', permanent=False)),
    url(r'^usage/$'     , RedirectView.as_view(url='http://scrapinghub.com/crawlera#example', permanent=False)),
    url(r'^pricing/$'   , RedirectView.as_view(url='http://scrapinghub.com/pricing#crawlera-pricing', permanent=False), name='pricing'),
    url(r'^signup/$'    , RedirectView.as_view(url='http://scrapinghub.com/pricing#crawlera-pricing', permanent=False)),
    url(r'^faq/$'       , RedirectView.as_view(url='http://scrapinghub.com/faq#crawlera', permanent=False)),
    url(r'^support/$'   , RedirectView.as_view(url='http://support.scrapinghub.com/list/19086-general/?category=4879', permanent=False)),

    # Examples:
    # url(r'^$', 'crawlera.views.home', name='home'),
    # url(r'^crawlera/', include('crawlera.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
