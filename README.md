# Motion_Template


OpenPose code based on the following code repository: https://github.com/spmallick/learnopencv/tree/master/OpenPose

### Prerequisites

Python 3 and Conda (for Python 3) are the only externals requirement for this: https://www.anaconda.com/download/

### Installing


##### Anaconda Environment

Open the Anaconda Prompt window (refer to this [Getting Started page](https://conda.io/docs/user-guide/getting-started.html)).

In the Anaconda Prompt window, type

```
cd [/path/to/Motion_Template]
```

Install the Conda environment via

```
conda env create -f environment.yml
```

For Windows, activate the environment via

```
conda activate deeplearning
```

For Linux / OS X, activate the environment via

```
source activate deeplearning
```


**NOTE:** if *deeplearning* already exists as an environment, two things can be done:

1. Change the *name* field in ```environment.yml``` to a unique name. In the above commands, change *deeplearning*  to the unique name given in environment.yml
2. Remove the current *deeplearning* environment by typing ```conda env remove -n deeplearning```.

##### Models

In addition, the pose and model parameters must be downloaded from the internet. [Please download the model ZIP file here](https://www.dropbox.com/s/56r5fe80a23jlks/model.zip?dl=0)

Move the ```model.zip``` file into the ```OpenPose``` directory, then unzip the contents within the directory. You should see three directories appear: ```head```, ```face```, and ```pose``.

To clear space on your system, remove the ZIP file afterwards:

```
rm model.zip
```

## Getting Started

After installing the environment, make sure the OpenCV works by running the video capture system:

```
cd OpenPose
python OpenPoseImage.py
```

This should output a pair of images, one showing the labelled joints and the other the predicted skeleton. After this, type ```cd ..``` to get back to the main directory and run the main program:

```
python main.py
```

Right now, it ouptuts the results of the image as a series of commands for the serial module and prints to stdout. 

**TODO:** make sure this works on the robot end
