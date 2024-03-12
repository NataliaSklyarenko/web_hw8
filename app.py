from mongoengine import Document, StringField, ListField, ReferenceField

class Author(Document):
    name = StringField(required=True, max_length=100, unique=True)
    nationality = StringField(max_length=100)

class Quote(Document):
    text = StringField(required=True)
    author = ReferenceField(Author, reverse_delete_rule=True)
    tags = ListField(StringField(max_length=50))

    meta = {'collection': 'quotes'}  # Вказуємо назву колекції у базі даних MongoDB
  