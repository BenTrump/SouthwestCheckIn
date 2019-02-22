#  import selenium
from selenium import webdriver
import time


def check_in():
    confirmation_number = "ABCDE9"
    first_name = "Tom"
    last_name = "Brady"
    email = "tom_brady@hotmail.com"
    date_time = "date.time format"

    # Todo: add a 'wait until' feature that allows user to run script all day until they can check in

    driver = webdriver.Chrome()
    driver.get("https://www.southwest.com/air/check-in/")

    confirmation_box_id = driver.find_element_by_id("confirmationNumber")
    first_name_box_id = driver.find_element_by_id("passengerFirstName")
    last_name_box_id = driver.find_element_by_id("passengerLastName")
    confirmation_box_id.send_keys(confirmation_number)
    first_name_box_id.send_keys(first_name)
    last_name_box_id.send_keys(last_name)
    checkin_button = driver.find_element_by_id("form-mixin--submit-button")
    checkin_button.click()
    time.sleep(3)

    second_checkin_btn = driver.find_element_by_xpath('//*[@data-a="airCheckInReviewResults_checkIn"]')
    second_checkin_btn.click()
    time.sleep(2)

    email_button = driver.find_element_by_xpath(
        '//*[@data-a="airCheckInBoardingPassOption_button_mobileBoardingPassOption_email"]')
    email_button.click()
    time.sleep(2)

    email_box_id = driver.find_element_by_id("emailBoardingPass")
    email_box_id.send_keys(email)
    time.sleep(2)

    email_submit_btn = driver.find_element_by_id("form-mixin--submit-button")
    email_submit_btn.click()
    time.sleep(5)


check_in()
