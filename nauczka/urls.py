from django.conf.urls import patterns, url
from django.contrib import admin
import home.views as homeViews


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nauczka.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', homeViews.home_page, name='home'),
    url(r'^courses/add$', homeViews.add_online_course, name='add_online_course'),
    url(r'^courses/(\d+)/$', homeViews.get_course_details, name='get_course_details'),
    url(r'^courses/(\d+)/add_note$', homeViews.add_note_to_course, name='add_note_to_course'),
)
