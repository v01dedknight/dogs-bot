import mysql.connector
from config import DB_CONFIG

# Функция для подключения к базе данных
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# Функция для загрузки собак
def get_dogs(limit=10, offset=0):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, gender, birthday FROM dogs LIMIT %s OFFSET %s", (limit, offset))
    dogs = cursor.fetchall()
    conn.close()
    return dogs

# Функция для загрузки данных о собаке по ID
def get_dog_info(dog_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, birthday, color, gender, weight, free, delivery, 
               picture1, picture2, picture3, picture4, picture5, picture6, 
               picture7, picture8, picture9, picture10 
        FROM dogs WHERE id = %s
    """, (dog_id,))
    dog = cursor.fetchone()
    conn.close()
    return dog
