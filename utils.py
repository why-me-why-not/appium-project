from datetime import datetime, timedelta
import os
import sqlite3
import random


def db_init():
    if not os.path.exists('demo_data.db'):
        try:
            conn = sqlite3.connect('demo_data.db')
            cursor = conn.cursor()
            with open('db_init.sql', mode='r', encoding='utf8') as f:
                db_init = f.read()
            cursor.executescript(db_init)
            conn.commit()
            conn.close()
        except Exception as e:
            print(f'An error occur during database initializing: {e}')

def name_gen():
    try:
        with sqlite3.connect('demo_data.db') as conn:
            cursor = conn.cursor()
            last_name = cursor.execute('''SELECT * FROM last_names
                                        ORDER BY RANDOM() LIMIT 1;''').fetchone()[0]
            first_name = cursor.execute('''SELECT * FROM first_names
                                        'ORDER BY RANDOM() LIMIT 1;''').fetchone()[0]
            second_name = cursor.execute('''SELECT * FROM second_names
                                         'ORDER BY RANDOM() LIMIT 1;''').fetchone()[0]
        return ' '.join([last_name, first_name, second_name])
    except Exception as e:
        print(f'An error occur: {e}')

def date_gen():
    days = random.randint(1, 18000)
    date =  datetime(2000, 1, 1) - timedelta(days=days)
    return date.strftime('%d.%m.%Y')

def passport_serie_gen():
    return ''.join(str(random.randint(1, 9)) for _ in range(4))

def six_number_gen():
    return ''.join(str(random.randint(1, 9)) for _ in range(6))

def birth_place_gen():
    city = random.choice(['Москва', 'Нижний Новгород', 'Казань', 'Краснодар'])
    return ' '.join(['гор.', city])

def snils_gen():
    return ''.join(str(random.randint(1, 9)) for _ in range(11))