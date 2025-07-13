from mongoengine import connect
import configparser

import configparser
from mongoengine import connect

def init_db():
    config = configparser.ConfigParser()
    config.read('config.ini')

    mongo_user = config.get('DB', 'user')
    mongodb_pass = config.get('DB', 'pass')
    db_name = config.get('DB', 'db_name')
    domain = config.get('DB', 'domain')

    connection_string = (
        f"mongodb+srv://{mongo_user}:{mongodb_pass}"
        f"@{domain}/{db_name}?retryWrites=true&w=majority"
    )

    connect(host=connection_string, ssl=True)
    print("✅ Підключення до MongoDB успішне!")
