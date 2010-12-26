from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import StringField, DateTimeField

__author__ = 'kilonet'

class Comment (EmbeddedDocument):
    text = StringField ()
    date = DateTimeField ()
  