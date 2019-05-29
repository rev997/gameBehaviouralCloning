import keras
import numpy as np
import cv2
import mss
import time


width=300
height=100
channels=1
model=keras.models.load_model('models')
paused=False
with mss.mss() as sct:
    last_time = time.time()
    monitor = {'top': 200, 'left': 120, 'width': 770, 'height': 250}
    i=1
    while i:
        i=i+1
        img = np.array(sct.grab(monitor))
        img=cv2.resize(img,(width,height),interpolation = cv2.INTER_AREA)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.blur(img,(2,2))
        X=np.array([img]).reshape(-1,width,height,channels)/255
        predictions=model.predict(X)
        print("steering predcition:",predictions[0],"   fps:",str(1/(time.time()-last_time)))
        last_time=time.time()
