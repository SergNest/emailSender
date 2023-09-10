import configparser
import pathlib

from mongoengine import connect

file_config = pathlib.Path(__file__).parent.parent.joinpath("config.ini")
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DB_DEV', 'user')
password = config.get('DB_DEV', 'password')
db_name = config.get('DB_DEV', 'db_name')
domain = config.get('DB_DEV', 'domain')

connect(host=f"mongodb+srv://{username}:{password}@{domain}{db_name}", ssl=True)
