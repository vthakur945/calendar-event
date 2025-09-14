from calendar import calendar
import requests
import json
import os
from gcsa.google_calendar import GoogleCalendar
from datetime import datetime
from gcsa.event import Event

CREDENTIALS_PATH = "/Users/vaidehithakur/project/client_secret.json"

def get_calendar():
    calendar = GoogleCalendar('learnawsvedu@gmail.com', credentials_path = CREDENTIALS_PATH)
    return calendar

def get_events():
    calendar = get_calendar()
    for event in calendar:
        print(event)

def create_event():
    calendar = get_calendar()
    attendees_list = ['shardul.27591@gmail.com', 'vaidehi.thakur.vt@gmail.com']
    event_dict = {
        'summary': 'Wedding Anniversary <3',
        'location': 'Sunnyvale Home Sweet Home',
        'description': 'Celebrating our special day ',
        'start': datetime(2025, 9, 15, 9, 0, 0),
        'end':datetime(2025, 9, 15, 6, 0, 0),
        'color_id': '11'
        # 'start': {
        #     'dateTime': '2025-09-13T09:00:00-07:00',
        #     'timeZone': 'America/Los_Angeles',
        # },
        # 'reminders': {
        #     'useDefault': False,
        #     'overrides': [
        #         {'method': 'email', 'minutes': 24 * 60},
        #         {'method': 'popup', 'minutes': 10},
        #     ],
        # },
        # 'attendees': [
        #     {'email': 'shardul.27591@gmail.com'}s
        #     ]
    }
    event = Event(
    summary=event_dict['summary'],
    location=event_dict['location'],
    description=event_dict['description'],
    start=event_dict['start'],
    color_id = event_dict['color_id'],
    attendees=attendees_list
)
    created_event = calendar.add_event(event)
    if created_event.html_link:
        print(f"Your event is succesfully created with the following link: {created_event.html_link}")




# def get_credentials():
#     creds = None
#     if os.path.exists(file_path):
#         creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

#     # file = open(file_path, "r")
#     # data = json.load(file)
#     # client_id = data["web"]["client_id"]
#     # project_id = data["web"]["project_id"]
#     # client_secret = data["web"]["client_secret"]
#     # return client_id, project_id, client_secret


def main():
    print(f"Welcome to the Calendar App: With this app you can create, edit, delete an event on your calendar\n What would you like to do today?")
    # create_event()

if __name__ == "__main__":
    main()
