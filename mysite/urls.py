from django.conf.urls import patterns, include, url

from django.contrib import admin

from mysite.views import hello,hours_ahead,date,displayhttpheader,search_form,search,contact

admin.autodiscover()

urlpatterns = patterns('',(r'^hello/$',hello),(r'^(?P<offset>\d{1,2})/$',hours_ahead),(r'date/$',date),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^header/$',displayhttpheader),
    (r'^search-form/$', search_form),
    (r'^search/$', search),
    (r'^contact/$',contact),

)
