import os
from dotenv import load_dotenv

print(os.environ)
load_dotenv()

print(os.getenv('SECRET_KEY'))
