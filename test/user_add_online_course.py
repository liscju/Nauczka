__author__ = 'lee'

from selenium import webdriver
import unittest

class UserAddOnlineCourse(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_user_click_add_online_course_button(self):
        # User open Nauczka website
        self.browser.get('http://localhost:5000')

        # User clicks on add course button
        add_online_course_btn = self.browser.find_element_by_id("add_online_course")
        add_online_course_btn.click()

        # User is linked to site '/add_online_course'
        self.assertEqual(self.browser.current_url,'http://localhost:5000/add_online_course')

        # User typed name of the course and his url in input text
        course_name_input = self.browser.find_element_by_id("course_name")
        course_url_input = self.browser.find_element_by_id("course_url")
        save_button = self.browser.find_element_by_id("save_course")

        course_name_input.send_keys("HTML5")
        course_url_input.send_keys("https://courses.edx.org/courses/course-v1:W3Cx+W3C-HTML5+2015T3/info")

        # User clicked save button
        save_button.click()

        # User is back in main site
        self.assertEqual(self.browser.current_url,'http://localhost:5000/')

        # User see in main page in course list his new course
        online_courses_names = self.browser.find_elements_by_class_name("online_course_name")
        self.assertIn("1. HTML5",[course_name.text for course_name in online_courses_names])

        self.fail("Finish test")

if __name__ == '__main__':
    unittest.main()