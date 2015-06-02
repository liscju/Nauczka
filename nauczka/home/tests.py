from django.core.urlresolvers import resolve
from django.http.request import HttpRequest
from django.test import TestCase
from nauczka.home.models import Course
from nauczka.home.views import *

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_add_online_course_resolves_to_add_online_course(self):
        found = resolve('/add_online_course')
        self.assertEqual(found.func, add_online_course)

    def test_add_online_course_save_given_course(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['course_name'] = 'Apache Spark'
        request.POST['course_url'] = 'www.coursera.com/apache_spark'

        add_online_course(request)

        courses = Course.objects.all()
        self.assertEqual("Apache Spark",courses[0].name)

class CourseTest(TestCase):

    def test_save_load_course(self):
        html5 = Course(name="HTML5",url="www.coursera.com/html5")

        html5.save()
        courses = Course.objects.all()

        self.assertEqual("HTML5",courses[0].name)

