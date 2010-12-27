from mongoengine.document import Document
from mongoengine.fields import StringField, DateTimeField, ListField, EmbeddedDocumentField
from datetime import datetime
from blok.models.Comment import Comment

__author__ = 'kilonet'

class Post(Document):
    text = StringField()
    title = StringField()
    user_name = StringField ()
    date = DateTimeField (default=datetime.now())
    comments = ListField(EmbeddedDocumentField(Comment))

  