from functional_tests.base import FunctionalTest

__author__ = 'lee'

from selenium import webdriver
import unittest

class UserAddOnlineCourse(FunctionalTest):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_user_click_add_online_course_button(self):
        # User open Nauczka website
        self.browser.get(self.live_server_url)

        # User clicks on add course button
        add_online_course_btn = self.browser.find_element_by_id("add_online_course")
        add_online_course_btn.click()

        # User is linked to site '/add_online_course'
        self.assertEqual(self.browser.current_url,self.live_server_url + '/courses/add')

        # User typed name of the course and his url in input text
        course_name_input = self.browser.find_element_by_id("course_name")
        course_url_input = self.browser.find_element_by_id("course_url")
        course_description_input = self.browser.find_element_by_id("course_description")
        save_button = self.browser.find_element_by_id("save_course")

        course_name_input.send_keys("HTML5")
        course_url_input.send_keys("https://courses.edx.org/courses/course-v1:W3Cx+W3C-HTML5+2015T3/info")
        course_description_input.send_keys("Learn basic to the new html standard")

        # User clicked save button
        save_button.click()

        # User is back in main site
        self.assertEqual(self.browser.current_url,self.live_server_url + "/")

        # User see in main page in course list his new course
        online_courses_names = self.browser.find_elements_by_class_name("online_course_name")
        self.assertIn("HTML5",[course_name.text for course_name in online_courses_names])

    def test_user_click_on_home_page_get_back_to_main_site(self):
        # User open Nauczka in website
        self.browser.get(self.live_server_url)

        # User click on add course button
        add_online_course_btn = self.browser.find_element_by_id("add_online_course")
        add_online_course_btn.click()

        # User is linked to site '/add_online_course'
        self.assertEqual(self.browser.current_url,self.live_server_url + '/courses/add')

        # User click on site logo
        site_banner = self.browser.find_element_by_id("site_logo")
        site_banner.click()

        # User is back in main site
        self.assertEqual(self.browser.current_url,self.live_server_url + "/")

