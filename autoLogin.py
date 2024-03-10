from time import sleep
from playwright.sync_api import sync_playwright
from key import key
# username = "40221343"
# password = "a13841384"
with sync_playwright() as p :
    browser = p.chromium.launch(headless= False , slow_mo= 50)
    page = browser.new_page()
    page.goto("http://192.168.1.1/")
    page.get_by_placeholder("نام کاربری").click()
    page.get_by_placeholder("نام کاربری").fill(key.username)
    page.get_by_placeholder("رمز ورود").click()
    page.get_by_placeholder("رمز ورود").fill(key.password)

    page.get_by_role("button", name="ورود").click()
    # page.get_by_text("Credit has finished")
    sleep(5)
    # if(page.content().find("div>Credit has finished</div>")):
    #     print("Your credit has finished")
    
    # page.pause()