*** Settings ***

Resource   ../common.robot

*** Variables ***

# User Information
@{renauto1}       &{data}[${user1}]

${profile_uuid}   ${renauto1[0]['profile_uuid']}

*** Test Cases ***

TEST_1: Get profile details and see the response
	[Tags]          smoke
	Get Profile     ${profile_uuid}

