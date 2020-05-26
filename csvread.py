import json
from csv import DictReader

with open('files/books.csv', newline='') as file:
    reader = DictReader(file)
    book_list = []
    for row in reader:
        books = {'title': row['Title'], 'author': row['Author'], 'height': row['Height']}
        book_list.append(books)

with open('files/users.json', 'r') as file:
    users_data = json.loads(file.read())
    user_list = []
    for user in users_data:
        new_users = {'name': user['name'], 'gender': user['gender'], 'address': user['address']}
        user_list.append(new_users)

result_data = []
for user, book in zip(user_list, book_list):
    result_data.append({'name': user['name'], 'gender': user['gender'], 'address': user['address'], 'books': [book]})

with open('my_json.json', 'w') as file:
    s = json.dumps(result_data, indent=4)
    file.write(s)
