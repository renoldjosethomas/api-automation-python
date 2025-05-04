*** Settings ***

Resource   ../LibraryMap.robot

*** Variables ***

# User Information
${renauto1}               &{data}[${user1}]
${profile_uuid_get}       ${renauto1['profile']['get']}

*** Test Cases ***

Print User Data
    [Tags]     smoke
    Log    Full user data: ${renauto1}
    Log    Profile UUID: ${profile_uuid_get}

TEST_1 Create profile details and see the response
	[Tags]         smoke
	${response}    Create profile    profile_name=profile_1    first_name=David    last_name=Harris    phone=14152671237    country=US    postal_code=98136    email=davidharris@example.com
	Verify create profile    ${response}    profile_name=profile_1    first_name=David    last_name=Harris    phone=14152671237   postal_code=98136   

TEST_2 Get profile details and see the response
	[Tags]                 smoke    sanity
	${response}            Get profile    ${profile_uuid_get}
	Verify get profile     ${response}    ${False}    ${200}    profile_name=profile_2    first_name=Samantha    last_name=Prabhu    phone=16135551234   postal_code=K2C 3H1    email=samantha.prabhu@example.ca

TEST_3 Get profile details and see the response - Validation failure sample
	[Tags]         smoke    sanity
	${response}    Get profile    ${profile_uuid_get}
	Verify get profile    ${response}    is_negative=${False}    exp_status_code=${200}    profile_name=profile_2    first_name=Samantha    last_name=Joseph    phone=16135551234   postal_code="K2C 3H1"  
