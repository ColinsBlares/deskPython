import sqlite3

# Подключение к базе данных (или создание, если она не существует)
conn = sqlite3.connect('products.db')
c = conn.cursor()

# Создание таблицы
c.execute('''CREATE TABLE products
             (id INTEGER PRIMARY KEY, name TEXT, amount INT, price REAL, image_path TEXT)''')

# Вставка тестовых данных
products = [
    (1, 'Яблоки', 15, 60, 'images/apple.jpeg'),
    (2, 'Бананы', 15, 50, 'images/bananas.jpg'),
    (3, 'Апельсины', 15, 70, 'images/Oranges.png'),
    (4, 'Груши', 15, 80, 'images/grusha.jpeg'),
    (5, 'Клубника', 15, 50, 'images/klubnika.jpg'),
    (6, 'Крыжовник', 0, 70, 'images/krizhovnik.jpg'),
]

c.executemany('INSERT INTO products VALUES (?,?,?,?,?)', products)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()

print("База данных успешно создана и заполнена!")
