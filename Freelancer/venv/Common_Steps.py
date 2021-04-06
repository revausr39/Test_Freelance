from Globals import *
from Locators import *


@allure.step
def Go_to_site():
    driver.maximize_window()
    driver.get("https://www.freelancer.com/signup")

@allure.step
def enter_username():
    rand_email = 'some_email_' + str(random.randrange(1,100)) + '@testemail.com'
    driver.find_element_by_xpath(new_username).send_keys(rand_email)

@allure.step
def enter_password():
    driver.find_element_by_xpath(new_password).send_keys('Password123')

@allure.step
def check_user_agreement():
    driver.find_element_by_xpath('/html/body/app-root/app-logged-out-shell/app-signup-page/fl-container/fl-bit/app-sign'
                                 'up/app-details-form/form/fl-bit/fl-label/fl-text/span/label/fl-text/div').click()
                                    #Cannot be referenced, since it will be turned into json.

@allure.step
def join_button():
    driver.find_element_by_xpath('/html/body/app-root/app-logged-out-shell/app-signup-page/fl-container'
                                 '/fl-bit/app-signup/app-details-form/form/app-login-signup-button/fl-button/button').click()

@allure.step
def select_suggestion():
    driver.find_element_by_xpath(suggest1).click()
    driver.find_element_by_xpath(next_button_uname_suggest).click()

@allure.step
def want_to_work():
    driver.find_element_by_xpath(want_to_work).click()

@allure.step
def want_to_hire():
    driver.find_element_by_xpath('/html/body/app-root/app-logged-out-shell/app-signup-page/fl-container/fl-bit/'
                                 'app-signup/app-account-type-form/form/fl-card[2]/fl-bit/fl-bit/fl-grid/fl-col[2]/fl-text/div').click()