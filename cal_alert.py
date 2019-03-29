from icalendar import Calendar, Event
from datetime import datetime, timedelta, date
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
    for component in gcal.walk('vevent'):
        if tomorrow in str(component.get('dtstart').dt):
            hstart = component.get('dtstart').dt
            hend = component.get('dtend').dt
            hstart = str(hstart).split(' ')[1].split('+')[0]
            hend = str(hend).split(' ')[1].split('+')[0]
            message = (message + str(component.get('summary')) +
                '\nInício:\t' + hstart + 
                '\nFim:\t' + hend + '\n\n'
            )
    g.close()
    if len(message) > 5:
        message = '<b>Amanhã</b>:\n' + message
        bot.send_message(dest, message, parse_mode='HTML')