import json
import requests
import unittest

from robot.api import logger
from requests.auth import HTTPBasicAuth
from robot.libraries.BuiltIn import BuiltIn


class ProfileService:
    def __init__(self, data, user1, user2):
        logger.info("Initialising ProfileService", also_console=True)
        # Evnironment Data is referenced from the environment file. For Eg: prod.py
        self.data = data
        self.user1 = user1
        self.user2 = user2
        # self.env = data['env']
        self.user1_dict = self.data[self.user1]
        self.user2_dict = self.data[self.user2]
        try:
            self.api_basepath = self.data['API_BASEPATH']
            logger.info(self.api_basepath, also_console=True)
        except KeyError:
            logger.error("API_BASEPATH not found in env file")
        self.user1_auth_id = self.user1_dict['auth_id']
        self.user1_auth_token = self.user1_dict['auth_token']  
        self.user2_auth_id = self.user2_dict['auth_id']
        self.user2_auth_token = self.user2_dict['auth_token']  


    def create_profile(self, **kwargs):
        """
        This API is used for creating a profile

        :param kwargs: key-value pairs for profile creation - Eg: profile_name, firstname, lastname, etc
        """

        logger.info("Performing POST request to create a profile")

        # Make the HTTP GET request using requests
        url = self.api_basepath + "profile/"
        json_data = json.dumps(kwargs)
        logger.info(url)

        # Use authentication in the headers (if needed for authentication)
        response = requests.post(url, 
                                 auth=HTTPBasicAuth(self.user1_auth_id, self.user1_auth_token), 
                                 data=json_data, 
                                 headers={"Content-Type": "application/json"})
    
        
        logger.info(response.status_code)
        
        # Check if the request was successful
        if response.status_code == 200:
            logger.info(response.content)
            return response
        else:
            BuiltIn.fail(f"Error: {response.status_code} - {response.content}")

    
    def verify_create_profile(self, profile_data, **kwargs):
        """
        This API is used for validating create profile request

        :param profile_data: profile data required for validation
        """

        logger.info("Performing validation for create profile response", also_console=True)

        profile_data = profile_data.json()
        logger.info(profile_data)

        for key in kwargs:
            if key in profile_data:
                assert profile_data[key] == kwargs[key], "Key - '{}' does not match. Expected: {}, Actual: {}".format(key, kwargs[key],profile_data[key])   
                logger.info("Key validation - {} successfully. Expected: {}, Actual: {}".format(key, kwargs[key],profile_data[key]))  
            else:
                BuiltIn.fail("Key {} not found in profile_data".format(key))

    def get_profile(self, profile_uuid):
        """
        This API is used for fetching profile details using the profile_uuid

        :param profile_uuid: The UUID of the profile to fetch
        """

        logger.info("Performing GET request to fetch profile details")

        # Make the HTTP GET request using requests
        url = self.api_basepath + "profile/" + profile_uuid + "/"
        logger.info(url)
        
        # Use authentication in the headers (if needed for authentication)
        response = requests.get(url, auth=HTTPBasicAuth(self.user1_auth_id, self.user1_auth_token))
        
        logger.info(response.status_code)
        logger.info(response.content)

        return response
        

    def verify_get_profile(self, response, is_negative, exp_status_code, **kwargs):
        """
        This API is used for validating create profile request

        :param profile_data: profile data required for validation
        """

        logger.info("Performing validation for create profile response", also_console=True)
        logger.info(response.content)

        logger.info(type(is_negative))

        # Status Code Assertion - Basic
        assert exp_status_code == response.status_code, "Expected: {}, Actual: {}".format(exp_status_code, response.status_code)

        # Positive Validation Logic
        if is_negative is False and response.status_code == 200:
            logger.info("Validating Positive Case - Get Profile")
            profile_data = response.json()
            logger.info(profile_data)
            
            for key in kwargs:
                if key in profile_data:
                    assert profile_data[key] == kwargs[key], "Key - '{}' does not match. Expected: {}, Actual: {}".format(key, kwargs[key],profile_data[key])   
                    logger.info("Key validation - {} successfully. Expected: {}, Actual: {}".format(key, kwargs[key],profile_data[key]))  
                else:
                    logger.error("Key - {} not found in profile_data".format(key))
                    BuiltIn().fail("Key - {} not found in profile_data".format(key))
        elif is_negative is True:
            # Negative Validation Logic Comes Here
            logger.info("Validating Negative Case - Get Profile")
        else:
            logger.fail(f"Error: {response.status_code} - {response.content}")
