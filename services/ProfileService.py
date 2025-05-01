import json
import requests

from robot.api import logger
from requests.auth import HTTPBasicAuth


class ProfileService:
    def __init__(self, data, user1, user2):
        logger.info("Initialising ProfileService", also_console=True)
        # Evnironment Data is referenced from the environment file. For Eg: prod.py
        self.data = data
        self.user1 = user1
        self.user2 = user2
        self.env = data['env']
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

    def get_profile(self, profile_uuid):
        """
        This API is used for fetching profile details using the profile_uuid

        :param profile_uuid: The UUID of the profile to fetch
        """

        logger.info("Performing GET request to fetch profile details")

        # Make the HTTP GET request using requests
        url = self.api_basepath + "/profile/" + profile_uuid
        
        # Use authentication in the headers (if needed for authentication)
        response = requests.get(url, auth=HTTPBasicAuth(self.user1_auth_id, self.user1_auth_token))
        
        logger.info(response.status_code )
        
        # Check if the request was successful
        if response.status_code == 200:
            logger.info(response.content)
            return response.json()  # Return the JSON response if successful
        else:
            return f"Error: {response.status_code} - {response.text}"  # Handle error response
