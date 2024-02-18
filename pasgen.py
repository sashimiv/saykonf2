import time
import string
import random
import sqlite3
class PasswordGenerator:
    def __init__(self):
        self.conn = sqlite3.connect('db/passwords.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS results
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           link TEXT,
                           login TEXT,
                           password TEXT)''')
    
    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def create_password(self):
        link = input("Введите ваш сервис: ")
        login = input("Ваш логин: ")
        chrast = input("Введите нужное кол-во символов, оставьте пустым, для рекомендуемого формата: ")
        if chrast == "":
            chrast = "24"
        password = self.generate_password(int(chrast))
        print("сервис: " + link)
        print("Логин: " + login)
        print("Пароль: " + password)
        
        self.c.execute("INSERT INTO results (link, login, password) VALUES (?, ?, ?)", (link, login, password))
        self.conn.commit()
        self.conn.close()
password_generator = PasswordGenerator()
password_generator.create_password()
