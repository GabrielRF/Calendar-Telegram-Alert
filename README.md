# Google Calendar Alerts on Telegram

## About

Small python script that checks an `.ics` and notifies users what time the event will start on the following day.

## Setup

Create a `configfile.conf`

```
[NAME1]
token =
dest =
ics =
```

`token` = Telegram bot token

`dest` = Message destination

`ics` = Link to the `.ics`

## Run

```
python cal_alert.py NAME1
```
