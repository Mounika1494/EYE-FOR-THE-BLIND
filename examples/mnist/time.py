import time
import os,sys

start_time=time.time()
os.system("sh ./train_lenet.sh")
print ("---time %s ---" %(time.time()-start_time))
