*** Settings ***

*** Variables ***

*** Test Cases ***
User is able to check cart is empty
    Open Browser  about://blank
    Go To  "https://flipkart.com"
    Click Button  Cart
