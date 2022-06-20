import unittest
from time import sleep
from BrowserUtil.BrowserFunction import Browser
from DataReader.DataAccess import DataAccess
from ExecutionLogs.Logger import Logger
from ProjectEnums.ProjectEnum import BrowserType, MsgType
from Utility.LoginUtility import LoginUtil


class TestLoginMethods(unittest.TestCase):

    # run this before every class
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        dataAccess=DataAccess()
        cls.credentials = DataAccess.getLoginDetails(dataAccess)
        cls.username = list(cls.credentials.keys())
        cls.password = list(cls.credentials.values())
        cls.logger = Logger()
        cls.loginutil = LoginUtil()
        cls.browser=Browser()

    def setUp(self):

        pass

    def test_LoginValid(self):
        Logger.Initialize(self.logger, "Test_LoginValid")
        self.Driver=self.browser.LaunchBrowser(BrowserType.Chrome)
        self.Driver.get("https://www.flipkart.com")
        Logger.WriteStepInfo(self.logger, MsgType.Info, "Browser successfully Launched")
        sleep(10)
        self.loginutil.Login(self.username[0], self.password[0])

    def test_LoginMyntraValid(self):
        Logger.Initialize(self.logger, "test_LoginMyntraValid")
        self.Driver=self.browser.LaunchBrowser(BrowserType.Chrome)
        Logger.WriteStepInfo(self.logger,MsgType.Info,"Browser successfully Launched")
        self.Driver.get("https://www.Myntra.com")
        sleep(10)
        self.loginutil.Login(self.username[0], self.password[0])





    def tearDown(self):
        print("Tear down")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")








