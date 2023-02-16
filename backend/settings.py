from dotenv import load_dotenv
import os 

load_dotenv() 
TEST_DB_NAME = os.getenv('TEST_DB_NAME') 
TEST_DB_USER = os.getenv('TEST_DB_USER')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')