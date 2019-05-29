import keras
import numpy as np
import cv2
import mss
import time
import pyxinput
from keys import key_check

width=300
height=100
channels=1
MyVirtual = pyxinput.vController()
MyRead = pyxinput.rController(1)
MyVirtual.set_value('TriggerR',1)
model=keras.models.load_model('models2')
paused=False
with mss.mss() as sct:
    last_time = time.time()
    monitor = {'top': 200, 'left': 120, 'width': 770, 'height': 250}
    i=1
    while 1:
        keys = key_check()
        if not paused:
            img = np.array(sct.grab(monitor))
            img=cv2.resize(img,(width,height),interpolation = cv2.INTER_AREA)
            img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.blur(img,(2,2))
            X=np.array([img]).reshape(-1,width,height,channels)
            predictions=model.predict(X)
            MyVirtual.set_value('AxisLx',predictions[0][0])
            print("steering predcition:",predictions[0],"   fps:",str(1/(time.time()-last_time)))
            last_time=time.time()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)
