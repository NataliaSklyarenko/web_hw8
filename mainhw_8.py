from mongoengine import connect
from models import Quote, Author

# Підключення до бази даних MongoDB
connect('quotes_db', host='localhost', port=27017)

while True:
    command = input("Введіть команду (name: автор, tag: тег, tags: теги): ").strip()

    if command.lower() == 'exit':
        break

    parts = command.split(':')
    if len(parts) != 2:
        print("Неправильний формат команди.")
        continue

    action, value = parts[0].strip().lower(), parts[1].strip()

    if action == 'name':
        quotes = Quote.objects(author__name=value)
    elif action == 'tag':
        quotes = Quote.objects(tags=value)
    elif action == 'tags':
        tags = value.split(',')
        quotes = Quote.objects(tags__in=tags)
    else:
        print("Непідтримувана команда.")
        continue

    # Виведення результатів пошуку в форматі UTF-8
    for quote in quotes:
        print(f"Цитата: {quote.text.encode('utf-8')} Автор: {quote.author.name.encode('utf-8')} Теги: {', '.join(quote.tags).encode('utf-8')}")