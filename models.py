from mongoengine import Document, StringField, IntField, ListField
from db import init_db

init_db()  # 🔌 Підключення через config.ini

class Cat(Document):
    name = StringField(required=True, unique=True)
    age = IntField(min_value=0)
    features = ListField(StringField())

    def __str__(self):
        return f"😺 {self.name}, {self.age} років, особливості: {', '.join(self.features)}"
