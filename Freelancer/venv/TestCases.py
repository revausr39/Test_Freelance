from Common_Steps import *


@allure.step
@allure.severity(allure.severity_level. NORMAL)
@allure.title("Go to Post a Project Page")
def test_TC01():
    Go_to_site()
    time.sleep(3)
    enter_username()
    enter_password()
    check_user_agreement()
    join_button()
    time.sleep(3)
    select_suggestion()
    time.sleep(3)
    want_to_hire()
    time.sleep(3)
    url_post = driver.current_url
    allure.attach(driver.get_screenshot_as_png(), name="Post Project Page_Screens", attachment_type=AttachmentType.PNG)
    assert 'https://www.freelancer.com/post-project?onboard=true' in url_post
