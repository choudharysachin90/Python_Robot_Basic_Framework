*** Settings ***
Documentation  This is my first Robot
Resource  ../Resources/ApplicationResource.robot
Resource  ../Resources/Base.robot


Test Setup  OpenDefaultBrowser
Test Teardown  Close Browser

*** Variables ***

*** Test Cases ***
User should be able to add a searched product to cart
    #GotoSitePage
    OpenGrofersSite
    SearchForProductInNav



    #CLick the searched product
    Wait Until Page Contains  “Salt” from Super Store
    sleep  5s
    Click Element  xpath=//img[@alt="Aashirvaad 1 kg Salt"]/following-sibling::span

   #add the product to cart
    Wait Until Element Is Visible  xpath=//span[text()="Add To Cart"]/ancestor::div[@class="pdp-product"]
    Click Element  xpath=//span[text()="Add To Cart"]/ancestor::div[@class="pdp-product"]





*** Keywords ***
