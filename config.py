import os

SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key-jihad-ai")
SQLALCHEMY_DATABASE_URI = "sqlite:///jihad_ai.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
