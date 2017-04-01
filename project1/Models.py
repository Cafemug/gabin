from peewee import *


from datetime import datetime, timedelta

db = SqliteDatabase('database.db')

class MyModel(Model):
    class Meta:
        database = db

class User(MyModel):
    email = CharField(unique = True)
    password = CharField()
    auth_token = CharField(null = True)
    token_expiration_date = DateTimeField(default=datetime.now()+timedelta(days=30))
    banned = BooleanField(default = False)

class Note(MyModel):
    user = ForeignKeyField(User, related_name='notes')
    last_edit = DateTimeField(default=datetime.now)
    title = TextField(null = True)
    body = TextField(null = True)
    image = TextField(null = True)
    public_id = CharField(null = True, max_length=8)
    hidden = BooleanField(default = False)

