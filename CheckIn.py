import selenium
from selenium import webdriver
import time


def check_in():
    confirmation_number = "FDEEY9"
    first_name = "Tom"
    last_name = "Brady"

    driver = webdriver.Chrome()
    driver.get("https://www.southwest.com/air/check-in/")

    confirmation_box_id = driver.find_element_by_id("confirmationNumber")
    first_name_box_id = driver.find_element_by_id("passengerFirstName")
    last_name_box_id = driver.find_element_by_id("passengerLastName")
    confirmation_box_id.send_keys(confirmation_number)
    first_name_box_id.send_keys(first_name)
    last_name_box_id.send_keys(last_name)
    checkin_button = driver.find_element_by_id("form-mixin--submit-button")
    for i in range(5):
        checkin_button.click()
        time.sleep(3)


check_in()
