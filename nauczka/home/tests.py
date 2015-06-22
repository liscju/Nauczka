from django.core.urlresolvers import resolve
from django.http.request import HttpRequest
from django.test import TestCase
from nauczka.home.models import Course, Note
from nauczka.home.views import *

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_add_online_course_resolves_to_add_online_course(self):
        found = resolve('/courses/add')
        self.assertEqual(found.func, add_online_course)

    def test_add_online_course_save_given_course(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['course_name'] = 'Apache Spark'
        request.POST['course_url'] = 'www.coursera.com/apache_spark'
        request.POST['course_description'] = 'Introduction to Apache Spark'

        add_online_course(request)

        courses = Course.objects.all()
        self.assertEqual("Apache Spark",courses[0].name)
        self.assertEqual('Introduction to Apache Spark',courses[0].description)

class CourseDetails(TestCase):

    def test_get_course_details_handle_proper_template(self):
        alg_course = Course.objects.create(name='Udacity - Algorithms',
                                           url='www.udacity.com/algorithms')

        response = self.client.get('/courses/%d/' % (alg_course.id,) )
        self.assertTemplateUsed(response,'get_course_details.html')

    def test_get_course_details_pass_proper_arguments(self):
        alg_course = Course.objects.create(name='Udacity - Algorithms',
                                           url='www.udacity.com/algorithms',
                                           description="Introduction to algorithms")

        response = self.client.get('/courses/%(id)s/' % { "id" : alg_course.id} )
        self.assertContains(response, 'Udacity - Algorithms')
        self.assertContains(response, 'www.udacity.com/algorithms')
        self.assertContains(response, "Introduction to algorithms")

    def test_get_course_details_return_course_notes(self):
        alg_course = Course.objects.create(name='Udacity - Algorithms',
                                           url='www.udacity.com/algorithms')

        Note.objects.create(time_spent=30,description="Done I Part",course=alg_course)

        response = self.client.get('/courses/%(id)s/' % { "id" : alg_course.id} )
        self.assertContains(response, "Done I Part")
        self.assertContains(response, "30")


class CourseTest(TestCase):

    def test_save_load_course(self):
        course_name = "HTML5"
        course_website = "www.coursera.com/html5"
        course_description = "Introduction to html5"

        html5 = Course(name=course_name,url=course_website,description=course_description)

        html5.save()
        courses = Course.objects.all()

        self.assertEqual(course_name,courses[0].name)
        self.assertEqual(course_website,courses[0].url)
        self.assertEqual(course_description,courses[0].description)

class NoteTest(TestCase):

    def test_save_note(self):
        course_ = Course.objects.create(name="HTML5",url="www.coursera.com/html5")
        note = Note(time_spent=30,description="Done I part",course=course_)
        note.save()

        loaded_note = Note.objects.first()
        self.assertEqual(loaded_note.time_spent, 30)
        self.assertEqual(loaded_note.description, "Done I part")
        self.assertEqual(loaded_note.course, course_)

    def test_load_all_notes_for_given_course(self):
        course_ = Course.objects.create(name="HTML5",url="www.coursera.com/html5")
        note = Note(time_spent=30,description="Done I part",course=course_)
        note.save()

        course_notes = Note.objects.filter(course=course_)
        self.assertEqual(course_notes[0].description, "Done I part")

class AddCourseNote(TestCase):

    def test_add_course_note_resolve_add_course_note_function(self):
        found = resolve("/courses/%d/add_note" % (1,) )
        self.assertEqual( found.func , add_note_to_course)

    def test_add_course_note_added_note_to_db(self):
        html5_course = Course.objects.create(name="HTML5",url="www.coursera.com/html5")

        self.client.post("/courses/%d/add_note" % (html5_course.id,) ,
            { 'time_spent' : "30", 'description' : 'Done I Part'}
        )

        note = Note.objects.first()

        self.assertEqual( note.time_spent , 30)
        self.assertEqual( note.description, "Done I Part")

    def test_add_course_note_redirects_to_course_details(self):
        html5_course = Course.objects.create(name="HTML5",url="www.coursera.com/html5")

        res = self.client.post("/courses/%d/add_note" % (html5_course.id,) ,
            { 'time_spent' : "30", 'description' : 'Done I Part'}
        )

        self.assertRedirects(res,"/courses/%d/" % ( html5_course.id,) )

















