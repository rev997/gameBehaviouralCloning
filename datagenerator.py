import time
import cv2
import mss
import numpy
from inputs import get_gamepad
from threading import Thread
from keys import key_check

value=0.0
lefts=0
rights=0
straight=0

def func1():
  global straight,rights,lefts
  training_data = []
  with mss.mss() as sct:
    # Part of the screen to capture
    time.sleep(10)
    monitor = {'top': 200, 'left': 120, 'width': 770, 'height': 250}
    i=0
    paused=True
    while True:
        i=i+1
        last_time = time.time()
        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))
        # resize and convert rgb2gray
        img=cv2.resize(img,(300,100),interpolation = cv2.INTER_AREA)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #applying gaussian blur to remove noise from image  
        img = cv2.blur(img,(2,2))
        if value==0:
            straight=straight+1
        if value<0:
            lefts=lefts+1
        if value>0:
            rights=rights+1
        time.sleep(0.020) #to limit fps
        #print(str(i),'fps: {0}'.format(1 / (time.time()-last_time)),str(value))
        if not paused:
            training_data.append([img,value])
            print(i,value,[lefts,straight,rights])
        cv2.imshow('OpenCV/Numpy normal', img)
        #Pausing
        keys = key_check()
        if 'P' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)
        #Saving collected data
        if 'S' in keys:
            print('saving')
            numpy.save('dataset.npy',training_data)
            print('saved')
            break
            break
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            print('saving')
            numpy.save('dataset.npy',training_data)
            print('saved')
            break

#function to get xbox input
def func2():
    global value
    while 1:
        events=get_gamepad()
        for event in events:
            a=event.ev_type+event.code+str(event.state)
            if 'AbsoluteABS_X' in a:
                value=round(int(a[13:])/32767,2)#input rounded between 0,1
                if value>1:
                    value=1
                if value<-1:
                    value=-1





#launching 2 functions
if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()
