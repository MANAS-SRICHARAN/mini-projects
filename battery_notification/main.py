import psutil
import os
def secs_formatter(time):
	min,sec = divmod(time,60)
	hr,min = divmod(min,60)
	return f"{hr}:{min}:{sec} left"

def sensor_formatter(sensor):
	percent = sensor.percent
	if sensor.power_plugged:
		time = "infinity as it is plugged in"
	else:
		time = sensor.secsleft
		time = secs_formatter(time)
	return [percent,time]
percent,time =sensor_formatter(psutil.sensors_battery()) 
print(f"% is {percent}")
print(f"{time}") 
if int(percent)<20:
	os.system("terminal-notifier -title 'battery down' -message 'charge up'")
	
