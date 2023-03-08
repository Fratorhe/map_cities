import ast
import json

import telebot
from telebot import formatting, types
from telebot.formatting import mbold, mitalic
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from get_information import get_cities, get_sections, get_places_section
from reader_places import place_reader


def get_token(file):
    with open(file, "r") as f:
        token = f.readline()
    return token


def set_telegram_bot():
    token = get_token(".TOKEN")
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start", "hello"])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")

    cities = get_cities()
    # print(cities)

    def makeKeyboard(iterable_element, element_type, **kwargs):
        s = ""
        for key, value in kwargs.items():
            s += f', "{key}": "{value}"'

        markup = types.InlineKeyboardMarkup()
        for element in iterable_element:
            markup.add(
                types.InlineKeyboardButton(
                    text=element,
                    callback_data="{" + f'"{element_type}": "{element}"{s}' + "}",
                )
            )
        return markup

    @bot.message_handler(commands=["test"])
    def handle_command_adminwindow(message):
        bot.send_message(
            chat_id=message.chat.id,
            text="Here are the values of stringList",
            reply_markup=makeKeyboard(cities, "city"),
            parse_mode="HTML",
        )

    # def makeKeyboard1(iterable_element, city):
    #     markup = types.InlineKeyboardMarkup()
    #     for element in iterable_element:
    #         markup.add(types.InlineKeyboardButton(text=element,
    #                                               callback_data=f"section: {element}, city: {city}"))
    #     print(markup)
    #     return markup

    @bot.callback_query_handler(lambda call: True)
    def handle_query_city(call):
        # print(call.data)
        dict_data_call = json.loads(call.data)

        # bot.answer_callback_query(
        #     callback_query_id=call.id, show_alert=True, text="You chose " + call.data
        # ) # use for debugging

        if call.data.startswith('{"city":'):
            handle_city(call, dict_data_call)

        if call.data.startswith('{"section":'):
            handle_section(call, dict_data_call)

    def handle_city(call, dict_data_call):
        city_name = dict_data_call["city"]

        city_data = place_reader(f"places/{city_name}.yaml")["data"]
        sections = get_sections(city_data)

        bot.send_message(
            chat_id=call.from_user.id,
            text="Here there are the sections",
            reply_markup=makeKeyboard(sections, "section", city=city_name),
            parse_mode="HTML",
        )

    def handle_section(call, dict_data_call):
        city_name = dict_data_call["city"]
        section = dict_data_call["section"]

        city_data = place_reader(f"places/{city_name}.yaml")["data"]
        places_section = get_places_section(city_data, section)
        # print(places_section)
        if places_section:
            # print("list is not emtpy")
            s = ""
            for place in places_section:
                s += f'{mbold(place["name"].title())}: {mitalic(place["comment"])} \n'
        else:
            s = "No places found"  # added space to avoid blowing up if empty

        bot.send_message(call.from_user.id, s, parse_mode="MarkdownV2")

    return bot


if __name__ == "__main__":
    bot = set_telegram_bot()
    bot.infinity_polling()
