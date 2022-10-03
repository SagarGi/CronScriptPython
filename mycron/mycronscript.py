import cronhelper.home as home
from datetime import datetime


now = datetime.now()
current_time = now.strftime("%H:%M")



def main():
    # make all the function run here
    home.check_bettery_of_system()
    home.morning_script(current_time)
    home.evening_script(current_time)
    home.drink_water(current_time)
    home.free_time_script(current_time)

   
if __name__ == "__main__":
    main()