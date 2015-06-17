from functional_tests.base import FunctionalTest

__author__ = 'lee'


class UserAddNotesToOnlineCourse(FunctionalTest):

    def test_user_click_add_note_button_in_course(self):
        # User open Nauczka website
        self.browser.get(self.live_server_url)

        # User clicks on add course button
        add_online_course_btn = self.browser.find_element_by_id("add_online_course")
        add_online_course_btn.click()

        # User typed name of the course and his url in input text
        course_name_input = self.browser.find_element_by_id("course_name")
        course_url_input = self.browser.find_element_by_id("course_url")
        save_button = self.browser.find_element_by_id("save_course")

        course_name_input.send_keys("HTML5")
        course_url_input.send_keys("https://courses.edx.org/courses/course-v1:W3Cx+W3C-HTML5+2015T3/info")

        # User clicked save button
        save_button.click()

        # User click on "HTML5"
        algorithm_online_course_el = self.browser.find_element_by_class_name("online_course_name")
        algorithm_online_course_el.click()

        # User click on add new note button
        add_new_note_btn = self.browser.find_element_by_id("add_new_note")
        add_new_note_btn.click()

        # User see form showed to add new note
        minutes_count = self.browser.find_element_by_id("new_note_minutes_spend")
        description_of_note = self.browser.find_element_by_id("new_note_description")

        # User inserts "30" as minutes spent, and "Done I part" of note description
        minutes_count.send_keys("30")
        description_of_note.send_keys("Done I part")

        # User clicks on Add Note
        add_note_btn = self.browser.find_element_by_id("new_note_add")
        add_note_btn.click()

        # User see that a new note was added just below notes
        notes_time_spent = self.browser.find_element_by_class_name("note-time-spent")
        notes_description = self.browser.find_element_by_class_name("note-time-description")

        self.assertEqual( notes_time_spent.text, "30")
        self.assertEqual( notes_description.text, "Done I part")























