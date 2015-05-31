from django.conf.urls import patterns, url
from django.contrib import admin
import home.views as homeViews


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', homeViews.home_page, name='home')
)
