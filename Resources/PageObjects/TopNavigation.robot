*** Settings ***


*** Variables ***


*** Keywords ***
SearchProduct
    InputTextForSearch
    WaitElementToBeEnabled
    sleep  5s
    ClickSearchButton



InputTextForSearch
    Input Text  xpath=//input[@placeholder="Search for products"]  Salt

WaitElementToBeEnabled
    Wait Until Element Is Enabled  xpath=//button[@class="btn search__btn"]

ClickSearchButton
    Click Button  xpath=//button[@class="btn search__btn"]