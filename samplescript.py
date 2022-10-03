# This is the cron job that is used myself for my system written in python script

# Pop a notification in your linux system by scheduling a cron job
from notify import notification

notification("This is the Notification Title", message='This message is scheduled from cron')