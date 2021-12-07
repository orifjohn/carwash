import string , random

import psycopg2
import telebot

TOKEN = 'your_token'
bot = telebot.TeleBot(token=TOKEN)



def get_price(price2):
    conn = psycopg2.connect(dbname="carwash", user="postgres", password="123", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT price FROM price WHERE service = '{price2}' ")
    price_tup = cursor.fetchall()
    cursor.close()
    price = list(price_tup[0])
    return price[0]



def create_info(user_cod,service,price,name,adres,phone):
    conn = psycopg2.connect(dbname="carwash", user="postgres", password="123", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders(user_cod,service_name,price,user_name,adres,phone) VALUES (%s,%s,%s,%s,%s,%s) ",
        (user_cod,service,price,name,adres,phone))
    conn.commit()
    cursor.close()


def get_info(user_cod):
    conn = psycopg2.connect(dbname="carwash", user="postgres", password="123", host="localhost", port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT service_name,price,user_name,adres,phone FROM orders WHERE user_cod='{user_cod}' ")
    info = cursor.fetchall()
    return info


