import uuid
from datetime import datetime

from robot.api import logger


def validate_uuid(value: str) -> bool:
    logger.info("Validating UUID: {value}", also_console=True)
    try:
        uuid_obj = uuid.UUID(value)
        return str(uuid_obj) == value
    except (ValueError, TypeError):
        return False
    


def validate_iso8601_date(date_str: str) -> bool:
    logger.info("Validating date_str: {date_str}", also_console=True)
    try:
        datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        return True
    except (ValueError, TypeError):
        return False
