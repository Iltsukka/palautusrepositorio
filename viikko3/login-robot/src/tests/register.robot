*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  testaaja  salainen1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  uusisalasana12
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ak  salasana12
    Output Should Contain  Min length for username is three characters

Register With Enough Long But Invald Username And Valid Password
    Input Credentials  KALLE  salainen12
    Output Should Contain  Username must contain only lowercase letters

Register With Valid Username And Too Short Password
    Input Credentials  kalleboi  seitsem
    Output Should Contain  Min length for password is eight characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ilari  salasanani
    Output Should Contain  Password cannot consist of letters only



*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input  new