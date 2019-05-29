
import numpy as np

original=np.load('dataset.npy')
final=[]
for values in original:
    if values[1]>0:
        final.append([values[0],values[1]])
    if values[1]<0:
        final.append([values[0],values[1]])
np.save('final_no_zeros.npy',final)
