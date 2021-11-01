*** Settings ***
Documentation  This is the base class with common functions
Library  SeleniumLibrary

*** Variables ***



*** Keywords ***
OpenDefaultBrowser
    Open Browser  about://blank
    Maximize Browser Window

CloseBrowser
    Close Browser