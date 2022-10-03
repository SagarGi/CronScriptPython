import math
from nis import match
from symbol import power
import psutil
from datetime import datetime
from notify import notification


now = datetime.now()
current_day_name = now.strftime("%A")
# monday to friday home plan time (thing i might forget)
break_fast_time = '08:00'
ready_for_office_time = '08:45'
morning_brush_time = '08:30'
evening_brush_time = '21:15'
off_your_device = '22:30'
drink_water_time = []
free_time = []

# time for weekend
if current_day_name == 'Saturday' or current_day_name == 'Sunday':
    morning_brush_time = '10:30'
    drink_water_time = ['11:00', '12:00','13:00', '14:00', '15:00', '16:00', '17:00']
    free_time = ['12:15', '14:15', '20:15']
    
# pop up notification
def pop_up_notification(notificationTitle, notificationMessage):
    notification(notificationTitle, message=notificationMessage)

def check_bettery_of_system():
    # returns a tuple containing battery information
    battery = psutil.sensors_battery()
    my_battery_percentage = math.trunc(battery.percent)
    is_charger_plugged_in = battery.power_plugged;
    if(my_battery_percentage < 25):
        title = "Battery Alert !!!"
        message = "Battery is getting low." + " Charger plug state = " + str(is_charger_plugged_in)
        pop_up_notification(title, message)


def morning_script(current_time):
    if current_time == break_fast_time:
        pop_up_notification("Breakfast !!", "Time to have your breakfast sagar")
    elif current_time == ready_for_office_time:
        pop_up_notification("Office Time !!", "Hurry you are geetting late for office !!")
    elif current_time == morning_brush_time:
        pop_up_notification("Brush Time !!", "Please brush your Teeth !!")

def evening_script(current_time):
    if current_time == evening_brush_time:
        pop_up_notification("Brush Time !!", "Please brush your Teeth !!")
    elif current_time == off_your_device:
        pop_up_notification("Still Awake Sagar?", "Time to go to bed, Have a good sleep !!")

    
def drink_water(current_time):
    if(len(drink_water_time) != 0):
        for time in drink_water_time:
            if(current_time == time):
                pop_up_notification("Drink Water !!", "Sagar Hydrate yourself by drinking water !!")


def free_time_script(current_time):
    if(len(free_time) != 0):
        for time in free_time:
            if(current_time == time):
                pop_up_notification("Free Time Sagar ?", "NETFLIX AND CHILL !!")
