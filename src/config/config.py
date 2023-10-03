import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DB_NAME: os.getenv("DB_NAME")
DB_USER: os.getenv("DB_USER")
DB_PASS: os.getenv("DB_PASS")
DB_HOST: os.getenv("DB_HOST")
DB_PORT: os.getenv("DB_PORT")

# platform = "match360",
# name = os.environ.get("APP_NAME") | "Match360"
# port = os.environ.get("PORT") | "5432"
