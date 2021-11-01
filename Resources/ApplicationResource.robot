*** Settings ***
Resource  ../Resources/PageObjects/LandingPage.robot
Resource  ../Resources/PageObjects/TopNavigatgion.robot
Resource  ../Resources/PageObjects/SearchPage.robot

*** Variables ***


*** Keywords ***
OpenGrofersSite
    LandingPage.OpenSiteHomePage
    LandingPage.SelectDefaultLocation


SearchForProductInNav
    TopNavigation.SearchProduct
    SearchPage.SelectTheProduct






