Motion_Template


### Prerequisites

Python 3 and Conda (for Python 3) are the only externals requirement for this: https://www.anaconda.com/download/

### Installing


##### Anaconda Environment

Open the Anaconda Prompt window (refer to this [Getting Started page](https://conda.io/docs/user-guide/getting-started.html)).

In the Anaconda Prompt window, type

```
cd [/path/to/DancingRobot]
```

Install the Conda environment via

```
conda env create -f environment.yml
```

For Windows, activate the environment via

```
activate deeplearning
```

For Linux / OS X, activate the environment via

```
source activate deeplearning
```

##### Models

In addition, the pose and model parameters must be downloaded from the internet. [Please download the repository here](https://www.dropbox.com/s/56r5fe80a23jlks/model.zip?dl=0)


## Getting Started

After installing the environment, make sure the OpenCV works by running the video capture system:

```
python OpenPoseImage.py
```

For Jupyter projects, **activate the environment first**, THEN run JupyterLab with the following command in the repository:

```
jupyter lab
```
