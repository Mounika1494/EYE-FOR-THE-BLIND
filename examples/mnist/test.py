caffe_root = '../../'  # this file should be run from {caffe_root}/examples (otherwise change this line)
from pylab import *
import matplotlib.pyplot as plt
import time

#%matplotlib inline
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe
caffe.set_mode_cpu()

### load the solver and create train and test nets
solver = None  # ignore this workaround for lmdb data (can't instantiate two solvers on the same data)
solver = caffe.SGDSolver('lenet_auto_solver.prototxt')

[(k, v.data.shape) for k, v in solver.net.blobs.items()]
[(k, v[0].data.shape) for k, v in solver.net.params.items()]

solver.net.forward()  # train net
solver.test_nets[0].forward()  # test net (there can be more than one)

# we use a little trick to tile the first eight images
imshow(solver.net.blobs['data'].data[:8, 0].transpose(1, 0, 2).reshape(28, 8*28), cmap='gray'); axis('off')
print 'train labels:', solver.net.blobs['label'].data[:8]

solver.step(1)

imshow(solver.net.params['conv1'][0].diff[:, 0].reshape(4, 5, 5, 5)
       .transpose(0, 2, 1, 3).reshape(4*5, 5*5), cmap='gray'); axis('off')

#%%time
niter = 10000
test_interval = 500
# losses will also be stored in the log
train_loss = zeros(niter)
test_acc = zeros(int(np.ceil(niter / test_interval)))
output = zeros((niter, 8, 10))
train_time = zeros(niter)
test_time = zeros(int(np.ceil(niter / test_interval)))
i=0 
# the main solver loop
for it in range(niter):
    solver.step(1)  # SGD by Caffe
    
    # store the train loss
    train_loss[it] = solver.net.blobs['loss'].data
    train_time[it] = time.clock() 
    #print time  
    # store the output on the first test batch
    # (start the forward pass at conv1 to avoid loading new data)
    solver.test_nets[0].forward(start='conv1')
    output[it] = solver.test_nets[0].blobs['score'].data[:8]
    
    # run a full test every so often
    # (Caffe can also do this for us and write to a log, but we show here
    #  how to do it directly in Python, where more complicated things are easier.)
    if it % test_interval == 0:
	test_time[i]=time.clock()
        i = i+1
        print 'Iteration', it, 'testing...'
        correct = 0
        for test_it in range(100):
            solver.test_nets[0].forward()
            correct += sum(solver.test_nets[0].blobs['score'].data.argmax(1)
                           == solver.test_nets[0].blobs['label'].data)
        test_acc[it // test_interval] = correct / 1e4

#print train_time
_, ax1 = subplots()
ax2 = ax1.twinx()
#ax1.plot(train_time, train_loss)
ax1.plot(arange(niter),train_loss, label='train loss')
ax2.plot(test_interval * arange(len(test_acc)), test_acc, 'r', label='test accuracy')
#ax2.plot(test_time, test_acc, 'r')
ax1.set_xlabel('ITERATION')
ax1.set_ylabel('TRAIN LOSS')
ax2.set_ylabel('TEST ACCURACY')
ax2.set_title('Test Accuracy: {:.2f}'.format(test_acc[-1]))

figLoss = plt.figure(3)
plt.plot(train_time, train_loss)
plt.xlabel('TIME')
plt.ylabel('TRAIN LOSS')
plt.title('Time VS Train loss')

figAccur = plt.figure(4)
plt.plot(test_time, test_acc, 'r')
plt.xlabel('TIME')
plt.ylabel('TEST ACCURACY')
plt.title('Time VS Test Accuracy')

plt.show()
