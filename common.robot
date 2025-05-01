*** Settings ***

# Variables
Variables   environment/${env}.py

# Libraries
Library  OperatingSystem
Library  robot.libraries.String
Library  robot.libraries.Collections
Library  services/ProfileService.py         ${data}     ${user1}     ${user2}
