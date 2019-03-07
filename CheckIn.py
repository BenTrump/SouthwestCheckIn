#  import selenium
from selenium import webdriver
import datetime
import time


class Southwest:
    def __init__(self):
        self.confirmation_number = "ABC123"
        self.first_name = "Tom"
        self.last_name = "Brady"
        self.email = "tombrady@hotmail.com"
        self.now = datetime.datetime.now()
        self.flight_time = self.now.replace(hour=12, minute=20)

    def check_in(self):
        driver = webdriver.Chrome()
        driver.get("https://www.southwest.com/air/check-in/")

        confirmation_box_id = driver.find_element_by_id("confirmationNumber")
        first_name_box_id = driver.find_element_by_id("passengerFirstName")
        last_name_box_id = driver.find_element_by_id("passengerLastName")
        confirmation_box_id.send_keys(self.confirmation_number)
        first_name_box_id.send_keys(self.first_name)
        last_name_box_id.send_keys(self.last_name)
        checkin_button = driver.find_element_by_id("form-mixin--submit-button")
        checkin_button.click()
        time.sleep(3)

        second_checkin_btn = driver.find_element_by_xpath('//*[@data-a="airCheckInReviewResults_checkIn"]')
        second_checkin_btn.click()
        time.sleep(3)

        email_button = driver.find_element_by_xpath(
            '//*[@data-a="airCheckInBoardingPassOption_button_mobileBoardingPassOption_email"]')
        email_button.click()
        time.sleep(3)

        email_box_id = driver.find_element_by_id("emailBoardingPass")
        email_box_id.send_keys(self.email)
        time.sleep(2)

        email_submit_btn = driver.find_element_by_id("form-mixin--submit-button")
        email_submit_btn.click()
        time.sleep(5)

    def wait_until(self, resolution):
        while self.now < self.flight_time:
            time.sleep(resolution)
            self.now = datetime.datetime.now()


obj = Southwest()
obj.wait_until(5)
obj.check_in()
