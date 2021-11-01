*** Settings ***

*** Variables ***
${url}

*** Keywords ***
OpenSiteHomePage
    Go To  http://grofers.com


SelectDefaultLocation
    Click Button  Detect my location
    Wait Until Element Is Visible  xpath=//div[@title="Bengaluru"]