# gameBehaviouralCloning

![](Driving.gif)\
**Note: Only steering values are predicted keeping speed constant**\
 I have collected the data and trained it on FH3(forza horizon 3).In the game difficulty setting,the gear shifting was set to manual(this acts as car speed control).The gear was set to 1 and throttle was set to full through out the process.A Xbox controller is used to control the car and these inputs are recorded for training.
 
## Dataset Collection
 To collect the data run **datasetgenerator.py** and don't forget to change gear shifting mode to manual.And set the screen monitor values as per your requirement.
 <pre>
 While collecting data use:         'P' key to pause
                                    'S' key to save collected data</pre>
## Training 
 To train model run **train.py**.
 
 ## Testing 
 To test the model run **test.py**\
 **Note:** While testing, first start test.py  then start the game.Else the you might encounter with CUBLAS_HANDLING error.
                                  
 ## Environment
 My rig:<pre> Ryzen 3 1200 (not OC)
        GTX 1050Ti (not OC)
        2x8gb Ram @ 3100Mhz</pre>
With my rig I am able to predict around 45 fps for the used model.If you have a better card  use a complex model(or RGB channels instead of grayscale).\
\
Game Settings: Very low                                    
