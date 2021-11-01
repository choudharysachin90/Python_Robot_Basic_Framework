*** Settings ***


*** Variables ***


*** Keywords ***
SelectTheProduct
    WaitPageLoad
    sleep  5s
    SelectSearchedProduct


#CLick the searched product
WaitPageLoad
    Wait Until Page Contains  “Salt” from Super Store


SelectSearchedProduct
    Click Element  xpath=//img[@alt="Aashirvaad 1 kg Salt"]/following-sibling::span
