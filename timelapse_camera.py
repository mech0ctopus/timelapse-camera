from time import sleep
from picamera import PiCamera
from datetime import datetime

MORNING_START_HOUR=7
EVENING_END_HOUR=19

def day_or_night(datetime):
    hour=datetime.hour
    if hour>=MORNING_START_HOUR and hour<EVENING_END_HOUR:
        return 'day'
    else:
        return 'night'
    
def take_picture():
    camera.start_preview()
    sleep(2)
    now=datetime.now().strftime("%Y-%m-%d-%H-%M")
    label='timelapse_' + now + '.jpg'
    camera.capture('/home/pi/Pictures/'+label)
    camera.stop_preview()
    print('Image captured at '+now)
    
if __name__=='__main__':
    camera = PiCamera()
    
    while True:
        now=datetime.now()
        if day_or_night(now) is 'day':
            try:
                take_picture()
            except:
                pass
		sleep(900) #15 minutes
            
