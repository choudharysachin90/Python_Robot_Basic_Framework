from selenium import webdriver

class Browser:
    browserObj = None

    def __new__(cls):
        if cls.browserObj is None:
          cls.browserObj = super(Browser, cls).__new__(cls)
        return cls.browserObj


    def LaunchBrowser(self, BrowserType):
        if BrowserType == BrowserType.Chrome:
            print("Chrome {}".format(BrowserType))
            self.browser = webdriver.Chrome('D:\selenium\chromedriver_win32\chromedriver.exe')
            self.browser.get('https://www.youtube.com')

        elif BrowserType == BrowserType.IE:
            print("IE {}".format(BrowserType))
            self.browser = webdriver.Edge('D:\selenium\edgedriver_win64\msedgedriver.exe')
            self.browser.get('https://www.youtube.com')
        else:
            print("Firefox {}".format(BrowserType))
            self.browser = webdriver.Firefox(executable_path=r'D:\selenium\geckodriver\geckodriver.exe')
            self.browser.get('https://www.youtube.com')

        return self.browser



    def ClickElement(self, xpathValue):
        self.browser.find_element_by_xpath(xpathValue).click()

    def SendKeys(self, xpathValue, textValue):
        self.browser.find_element_by_xpath(xpathValue).send_keys(textValue)
