from mongoengine import Document
from mongoengine.fields import (BooleanField, DateTimeField, EmbeddedDocumentField, ListField, StringField,
                                IntField, ReferenceField)

import database.db


class Contact(Document):
    fullname = StringField()
    email = StringField()
    delivered = BooleanField(default=False)
