from enum import Enum
from dotenv import load_dotenv
import os

ML_PROJECT = 'AMAZON_GAIRS'
RELEASE_VERSION = '0.0.0'

def _get_env(var: str, default=None):
    """
    Helper function to properly handle environment variable loading
    """
    result = os.getenv(var, default)
    if not result:
        return default
    return result.replace("'", "")

class Directory(str, Enum):
    """
    Enumeration of common directories
    """
    ROOT = os.path.dirname(os.path.realpath(__file__))
    SRC = os.path.join(ROOT, 'src')
    DATA = os.path.join(ROOT, 'data')
    RAW_DATA = os.path.join(DATA, 'raw')
    PROCESSED_DATA = os.path.join(DATA, 'processed')
    INTERIM_DATA = os.path.join(DATA, 'interim')
    LOGS = os.path.join(ROOT, 'logs')
    REPORTS = os.path.join(ROOT,'reports')
    FIGURES = os.path.join(REPORTS, 'figures')


class Config:
    """
    Global configurations class.
    """
    def __init__(self):
        load_dotenv()
        # Reviews file to read in
        self.data_source:str = _get_env('DATA_SOURCE', 'McAuley-Lab/Amazon-Reviews-2023')
        self.product_category: str = _get_env('PRODUCT_CATEGORY', 'raw_review_Electronics')
    

