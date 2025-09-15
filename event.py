from calendar import calendar
import dataclasses
import json
import os
import string
from gcsa.google_calendar import GoogleCalendar
from datetime import datetime
from gcsa.event import Event

CREDENTIALS_PATH = "/Users/vaidehithakur/project/client_secret.json"
color_ids = {
    'Pale blue (Peacock)': '1',
    'Pale green (Sage)': '2',
    'Mauve (Grape)': '3',
    'Pale red (Flamingo)': '4',
    'Yellow (Banana)': '5',
    'Orange (Tangerine)': '6',
    'Turquoise (Lime)': '7',
    'Gray (Graphite)': '8',
    'Bold blue (Blueberry)': '9',
    'Bold green (Basil)': '10',
    'Bold red (Tomato)': '11'
}

@dataclasses.dataclass
class EventData:
    summary: str
    location: str
    description: str
    start: datetime
    color_id: str
    attendees: list = dataclasses.field(default_factory=list)
    end: datetime | None = None

def get_color_by_id(color):
    if color in color_ids:
        return color_ids[color]
    else:
        return 0
def get_calendar():
    calendar = GoogleCalendar('learnawsvedu@gmail.com', credentials_path = CREDENTIALS_PATH)
    return calendar

def get_events():
    calendar = get_calendar()
    for event in calendar:
        print(event)

def create_event(event_data: EventData):
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
        summary=event_data.summary,
        location=event_data.location,
        description=event_data.description,
        start=event_data.start,
        color_id=event_data.color_id,
        attendees=event_data.attendees
    )
    created_event = calendar.add_event(event)
    if created_event.html_link:
        print(f"Your event is succesfully created with the following link: {created_event.html_link}")

def get_input_to_create_event():
    summary= input("Provide title of the event: ")
    location = input("Specify location of the event like online or specify a place: ")
    description = input("Enter description for your event: ")
    start_date = input("Provide start date of the event in the following format MM/DD/YYYY: ")
    
    color = input ("Pick a color of your choice: Pale blue (Peacock), Pale green (Sage), Yellow (Banana), Turquoise (Lime), Bold red (Tomato): ")
    color_id = get_color_by_id(color)
    if color_id == 0:
        print(f"{color} is not a valid color name, please enter a valid color from the choice: ")
    attendees_list = input ("Provide a list of email addresses of all the attendees separated by comma: ")
    event_data = EventData(
        summary=summary,
        location=location,
        description=description,
        start=datetime.now(),
        color_id=color_id,
        attendees=attendees_list.split(",")
    )
    create_event(event_data)
    print(f"{summary}, {description}, {description}, {color_id}, {attendees_list}")


def main():
    print(f"Welcome to the Calendar App: \n What would you like to do today?")
    print(f"Enter your choices:\n 1. Create an event\n 2. Delete an event\n 3. View all the events\n")
    choice = int(input(f"Enter your choice here: "))
    match choice:
        case 1:
            print(f"To create an event, please provide the following details:")
            get_input_to_create_event()
        case 2:
            print(choice)
        case 3:
            print(choice)

    # create_event()

if __name__ == "__main__":
    main()
