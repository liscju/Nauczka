from django.conf.urls import patterns, url
from django.contrib import admin
import home.views as homeViews


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nauczka.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', homeViews.home_page, name='home'),
    url(r'^add_online_course$', homeViews.add_online_course, name='add_online_course')
)
