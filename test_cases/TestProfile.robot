*** Settings ***

Resource   ../common.robot

*** Keywords ***
Convert To Integer
    [Arguments]      ${value}
    ${int_value}=    Evaluate    int(${value})
    RETURN           ${int_value}

*** Variables ***

# User Information
@{renauto1}               &{data}[${user1}]
${profile_uuid_get}       ${renauto1[0]['profile_uuid_get']}

*** Test Cases ***

# TEST_1 Create profile details and see the response
# 	[Tags]         smoke
# 	${response}    Create profile    profile_name=profile_1    first_name=David    last_name=Harris    phone=14152671237    country=US    postal_code="98136"    email=davidharris@example.com
# 	Verify create profile    ${response}    profile_name=profile_1    first_name=Samantha    last_name=Nguyen    phone=16135551234   postal_code="K2C 3H1"   

TEST_2 Get profile details and see the response
	[Tags]                 smoke
	${response}            Get profile    ${profile_uuid_get}
	${status_code_200}     Convert To Integer    200
	Verify get profile     ${response}    ${False}    ${status_code_200}    profile_name=profile_2    first_name=Samantha    last_name=Nguyen    phone=16135551234   postal_code=K2C 3H1

# TEST_3 Get profile details and see the response
# 	[Tags]         smoke
# 	${response}    Get profile    ${profile_uuid_get}
# 	Verify get profile    ${response}    is_negative=${False}    exp_status_code=${status_code_200}    profile_name=profile_2    first_name=Samantha    last_name=Prabhu    phone=16135551234   postal_code="K2C 3H1"  
