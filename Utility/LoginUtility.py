
from PageObject.LoginPageElements import LoginPageElements
from BrowserUtil.BrowserFunction import Browser


class LoginUtil(LoginPageElements):

    def Login(self, username, password):
        browser=Browser()
        browser.SendKeys(self.txt_username,username)
        browser.SendKeys(self.txt_password,password)
        browser.ClickElement(self.btn_Login)


