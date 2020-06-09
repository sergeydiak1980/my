#! /usr/bin/env python
# -*- coding: utf-8 -*-
import telebot

token = 'тут токен'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Консультация в промышленном шпионаже', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Консультация в кибербезопасности', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Консульатция в поиски людей и данных', callback_data=5))
    markup.add(telebot.types.InlineKeyboardButton(text='Консультация в получение нужных удостоверений', callback_data=6))
    markup.add(telebot.types.InlineKeyboardButton(text='Консульатция по системам безопасноти: информационная, техническая и физической', callback_data=7))
    bot.send_message(message.chat.id, text="Здравствуйте, Меня зовут Сергей, специалист специального направления (внештатный сотрудник СБ), осуществляю поиску данных из разных источников, не всегда интернет, работаю я по обычию с владельцами крупных компаний, которые хотят быть на шаг впереди. Ниже представлен список моих возможностей:", reply_markup=markup)
   

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Спасибо!')
    answer = ''
    if call.data == '3':
        answer = ' Физическая Охранна\n1. Вооружонная охрана;\n2. Охрана объектов;\n3. Личная охрана;\n3. Постовая охрана;\n4. Охрана и сопровождение грузов;\n5. Охрана массовых мероприятий'
    elif call.data == '4':
        answer = '1. Группа быстрого реагирования (ГБР);\n2. Тревожная кнопка;\n3. Охрана автомобилей'
    elif call.data == '5':
        answer = '1. Установка системы безопасности;\n2. Проектирование систем безопасности;\n3. Обслуживания системы безопасности;\n4. Установка видеонаблюдения.'
    elif call.data == '6':
    	answer = '1. Консультация по личной безопасности;\n2. Аудит безопасности;\n3. Аудит по пожарной безопасности.'
    elif call.data == '7':
    	answer = 'ул. Большая Пушкарская, д. 41;\nтел.: 8-800-555-88-02;\ninfo@bors.pro;\nс 9-00 до 17-00'

    bot.send_message(call.message.chat.id, answer)
    # bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id) #для отображения вкладки меню

bot.polling()
