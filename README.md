# EYE-FOR-THE-BLIND
## Prepare Datasets

Make sure to download and convert the data format from the MNIST website. 
To do this, simply run the following commands:

	cd $CAFFE_ROOT
	./data/mnist/get_mnist.sh
	./create_mnist.sh (converts the MNISt dataset into lmdb formats)

After running the script there should be two datasets (folders), `mnist_train_lmdb`, and `mnist_test_lmdb`


## Creating the training model

Run ./train_lenet_adam.sh
	Prerequisites for this:
	1. lenet_solver_adam.prototxt (very important)
	2. lenet_train_test.prototxt
You can change the paramenets in the above two files for different results
 
lenet_solver_adam.prototxt:
	This file is like main.c, contains all the necesssary initilization parameters

lenet_train_test.prototxt:
	This file contains the necessary paramentets that detertmines the TRAIN and TEST models
	Make sure to have the following files in you current working dorectory
		'mnist_train_lmdb'
		'mnist_test_lmdb'
		 mnist_mean.binatyproto

By default the training is carried for 10000 iterartions with a test interval of 500

At the end you would find .caffemeodel files genereted. These files are trained models


## Extracting numbers from SUDOKU

Now you have trained model in the form lenet_iter_<NumOfIteration>.caffemodel. 

Navigate to /featureExtraction/sudoku and run sudoko_main.py for generation of images with numbers
The current code takes input as sudoko1.png and generates 9 images with numbers <1-9>

Read the instructions in /featureExtraction/sudoku for detailed steps


## Calssification of images

Now we have reached the final stage i,e, classifying the images
Copy the images from /featureExtraction/sudoku to /classification

Navigate to /classification and Run classifier_NN.py
You will find the final results 

Read the instructions in /classification for detailed steps

NOTE: You the repeat the above steps for train_lenet_adam.prototxt and train_lenet_rmsprop.prototxt. But make sure to have appropriate solvers beforehand. If you find the necessity for any additional files please refer to: https://github.com/BVLC/caffe

## Our Results:

Time taken for recognising each digit

FOR GPU
Time Stamps
[ 0.03394318  0.00645399  0.00808978  0.00613308  0.00570107  0.00552392
  0.00721097  0.00913405  0.0076139 ]

FOR CPU

[ 0.16581893  0.15843511  0.157794    0.15803909  0.1583581   0.15892315
  0.15843081  0.15809584  0.15785909]

	
	
   
