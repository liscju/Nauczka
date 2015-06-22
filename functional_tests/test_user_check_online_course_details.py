from functional_tests.base import FunctionalTest

__author__ = 'lee'

class UserCheckOnlineCourseDetails(FunctionalTest):

    def test_user_check_online_course_details(self):
        # User go to nauczka website
        self.browser.get(self.live_server_url)

        # User click add on online course
        add_online_course_btn = self.browser.find_element_by_id("add_online_course")
        add_online_course_btn.click()

        # User write as course name "Udacity - Introduction to algorithms"
        # and as website "www.udacity.com/algorithms" and click enter

        course_name_input = self.browser.find_element_by_id("course_name")
        course_url_input = self.browser.find_element_by_id("course_url")
        save_button = self.browser.find_element_by_id("save_course")

        course_name_input.send_keys("Udacity - Introduction to algorithms")
        course_url_input.send_keys("www.udacity.com/algorithms")
        save_button.click()

        # User get back to main site
        self.assertEqual(self.browser.current_url,self.live_server_url + "/")

        # User click on "Udacity - Introduction to algorithms"
        algorithm_online_course_el = self.browser.find_element_by_class_name("online_course_name")
        algorithm_online_course_el.click()

        # User see as course name "Udacity - Introduction to algorithms"
        # on details page
        course_details_name = self.browser.find_element_by_id("course_details_name")
        course_details_website = self.browser.find_element_by_id("course_details_website")
        self.assertEqual(course_details_name.text , "Udacity - Introduction to algorithms")
        self.assertEqual(course_details_website.text, "www.udacity.com/algorithms")

        # User goes to main site again:
        site_banner = self.browser.find_element_by_id("site_logo")
        site_banner.click()

        # User click add for another course
        add_online_course_btn = self.browser.find_element_by_id("add_online_course")
        add_online_course_btn.click()

        # User write as course name "Udacity - Advanced operating system"
        # and as website "www.udacity.com/advopsys" and click enter

        course_name_input = self.browser.find_element_by_id("course_name")
        course_url_input = self.browser.find_element_by_id("course_url")
        course_description_input = self.browser.find_element_by_id("course_description")
        save_button = self.browser.find_element_by_id("save_course")

        course_name_input.send_keys("Udacity - Advanced operating system")
        course_url_input.send_keys("www.udacity.com/advopsys")
        course_description_input.send_keys("Advancing part of operating system")
        save_button.click()

        # User click on "Udacity - Advanced operating system"
        online_courses = self.browser.find_elements_by_class_name("online_course_name")
        self.assertEqual(online_courses[1].text,"Udacity - Advanced operating system")
        online_courses[1].click()

        # User see as course name "Udacity - Advanced operating system"
        # on details page
        course_details_name = self.browser.find_element_by_id("course_details_name")
        course_details_website = self.browser.find_element_by_id("course_details_website")
        course_details_description = self.browser.find_element_by_id("course_details_description")
        self.assertEqual(course_details_name.text , "Udacity - Advanced operating system")
        self.assertEqual(course_details_website.text, "www.udacity.com/advopsys")
        self.assertEqual(course_details_description.text, "Advancing part of operating system")




















