from icalendar import Calendar, Event
from datetime import datetime, timedelta, date
from pytz import timezone
import configparser
import sys
import telebot
import urllib.request

config = configparser.ConfigParser()
config.sections()
config.read('configfile.conf')

CALENDAR = sys.argv[1]

TOKEN = config[CALENDAR]['token']
dest = config[CALENDAR]['dest']
calics = config[CALENDAR]['ics']

bot = telebot.TeleBot(TOKEN)

def open_file(file_url):
    file_name, headers = urllib.request.urlretrieve(file_url,
        'cal.ics')
    return file_name


if __name__ == '__main__':
    url = calics
    g = open(open_file(url),'rb')
    gcal = Calendar.from_ical(g.read())
    tomorrow = str(date.today() + timedelta(days=1))
    message = ''
    for component in reversed(gcal.walk('vevent')):
        if tomorrow in str(component.get('dtstart').dt):
            hstart = component.get('dtstart').dt
            hstart = hstart.astimezone(timezone('America/Sao_Paulo'))
            hend = component.get('dtend').dt
            hend = hend.astimezone(timezone('America/Sao_Paulo'))
            hstart = hstart.strftime('%H:%M')
            hend = hend.strftime('%H:%M')
            message = (message + str(component.get('summary')) +
                '\nInício:\t' + hstart + 
                '\nFim:\t' + hend + '\n\n'
            )
    g.close()
    if len(message) > 5:
        message = '<b>Amanhã</b>:\n' + message
        bot.send_message(dest, message, parse_mode='HTML')
