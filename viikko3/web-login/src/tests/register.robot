*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Check It Is Correct

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testaaja
    Set Password  salainen1
    Set Password2  salainen1
    Click Button  Register
    Register Should Succeed With Welcome Page Open

Register With Too Short Username And Valid Password
    Set Username  ak
    Set Password  salainen1
    Set Password2  salainen1
    Click Button  Register
    Register Should Fail With Message  Username must be atleast 3 characters


Register With Valid Username And Invalid Password
    Set Username  kirahvi
    Set Password  salainen
    Set Password2  salainen
    Click Button  Register
    Register Should Fail With Message  Password cannot contain only letters and min length is 8 

Register With Nonmatching Password And Password Confirmation
    Set Username  kirahvi
    Set Password  A1konen88
    Set Password2  2Bolavi7
    Click Button  Register
    Register Should Fail With Message  Passwords must match 

Login After Successful Registration
    Go To Login Page
    Set Username  testaaja
    Set Password  salainen1
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Go To Login Page
    Set Username  ak
    Set Password  salainen1
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Go To Register Page And Check It Is Correct
    Go To Register Page
    Register Page Should Be Open

Register Should Succeed With Welcome Page Open
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password2
    [Arguments]  ${password2}
    Input Password  password_confirmation  ${password2}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

