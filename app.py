import requests
import telebot
from flask import Flask, render_template, redirect, request
from db import get_price, create_info, get_info
import string
import random


app = Flask(__name__)





def send_message(chat_id, text):
    method = "sendMessage"
    token = 'Bitta botfatherdan bot ochib token quyish kere '
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


@app.route('/', methods=['POST', 'GET'])
def first_page():
    return render_template('index.html')



def code_generator(code_length=10):
    a = [string.digits, string.ascii_uppercase]
    codes =''.join([random.choice(random.choice(a)) for i in range(code_length)])
    return codes


@app.route('/forma', methods=['POST', 'GET'])
def forma():
    if request.method == 'GET':
        key = request.args
        for i in key:
            data = i
            return render_template('forma.html', data=data, price=get_price(data))
    if request.method == 'POST':
        user_cod = code_generator()
        key = request.args
        user_id = 1226450233
        for i in key:
            user_cod = code_generator()
            data = i
            servise = data
            price = get_price(data)
            name = request.form.get('username')
            adres = request.form.get('adres')
            phone = request.form.get('phone')
            if data and servise and price and name and adres and phone:
                create_info(user_cod,data, price, name, adres, phone)
                asd = get_info(user_cod=user_cod)
                for i in list(asd):
                    servise_name = i[0]
                    price = i[1]
                    user_name = i[2]
                    adres = i[3]
                    phone = i[4]
                    text = f"Yangi buyurtma\nXizmat turi: {servise_name}\nNarxi: {price}\nMijoz: {user_name}\nManzil: {adres}\nTel nomer: {phone}"
                    send_message(chat_id=user_id , text=text)
                    return render_template('index.html')


@app.route('/location')
def location():
    return render_template('location.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')



if __name__ == '__main__':
    app.run(debug=True, port=5000)
