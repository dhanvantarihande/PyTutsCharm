# Base Page And Two Child Class

class BasePage:

    def __init__(self):
        self.driver = driver
        print("Default Cons")


    def go_to_url(self,url):
        pass


    def read_file(self):
        pass


    def write_file(self):
        pass


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    def enter_username(self,username):
        print("Enter Username Here")
        pass


    def enter_password(self,password):
        print("Enter Password!")
        pass


    def click_login_button(self):
        print("Login Button")
        pass


class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    def verify_login_success(self):
        print("Verify")


    def click_logout_button(self):
        print("Logout Button")
        pass


# This is all Selenium Part

# driver = ChromeDriver()
# login = LoginPage(driver)
# login.go_to_url("http://app.vwo.com")
# login.enter_password("admin")
# login.enter_username("admin")
# login.click_login_button()