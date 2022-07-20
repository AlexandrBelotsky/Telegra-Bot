from pyowm import OWM
import telebot

owm = OWM('862e8f25190a38f5cb47d3b24823611d')
bot = telebot.TeleBot('TOKEN')

@bot.message_handler(content_types = ['text'])
def where(message):
    try:
        mgr = owm.weather_manager()
        ob = mgr.weather_at_place(message.text)
        w = ob.weather
        t = w.temperature('celsius')
        s = {0: t['temp'],
        1: t['feels_like'],
        2: w.wind()['speed'],
        3: w.humidity,
        4: w.clouds,
        5: w.pressure['press']
            }
        answer = "В городе " + message.text + " сейчас: \n"
        answer += "Температура " + str(s[0]) + '°C\n'
        answer += "Ощущается: " + str(s[1]) + '°C\n'
        answer += "Скорость ветра: " + str(s[2]) + ' км/ч\n'
        answer += "Влажность: " + str(s[3]) + '%\n'
        answer += "Облачность: " + str(s[4]) + '\n'
        answer += "Давление: " + str(s[5]) + 'mbar\n'
        bot.send_message(message.chat.id, answer)
    except:
        answer = "По месту " + message.text + " нет результата."
        bot.send_message(message.chat.id, answer)

bot.polling(none_stop=True)
