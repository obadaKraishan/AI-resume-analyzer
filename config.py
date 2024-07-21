import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '4e5b4d1f2c3d4a2b5e6f7a8b9c0d1e2f'
