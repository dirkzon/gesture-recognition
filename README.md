# gesture recognition

<div align="center">
Real time gesture recognition using OpenCV & Mediapipe
<br />
</div>
<div align="center">
<br />

[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f)](https://www.python.org/) 
</div>

<p align="center">
  <img src="./examples/example.gif" width="640">
</p>

## Contents
- [About](#about)
- [Features](#features)
- [Setup](#setup)
  - [Installation](#installation)
  - [Usage](#Usage)
- [Dataset](#dataset)
- [Try it yourself](#try-it-yourself)
- [Use your own data](#use-your-own-data)

s
## About
Made for my fourth semester with Python. The goal of this project was to create a real time gesture recognition app which is able to recognize american sign language gestures. The [model](./model) that this app uses is able to recognize gestures for digits '0' to '9'. The [notebook](Gesture%20recognition.ipynb) explains how this model was made.

## Features
- __real time:__ gesture recognition in real time
- __multiple hands:__ multiple hands can be recognized at once
- __ambidextrous:__ recognize gestures on both left and right hand
- __debug:__ visualize hand skeleton, confidence & more

## Setup

### Installation
To install all the dependencies run this command in the command line
```
pip install -r requirements.txt
```
### Usage
To start the app run the `gesture.py` file
```
python gesture.py
```

## Dataset
The *[Sign-Language-Digits-Dataset](https://github.com/ardamavi/Sign-Language-Digits-Dataset) was used to train and test the model. 
This repository does __NOT__ contain this data. So, if you want to process the images yourself you will have to download the dataset and put all the subfolders into a folder called `images`.
#### The structure should look like this:
```
. 
├─ 🗋 Gesture recognition.ipynb 
├─ 🗁 images/
│  ├─🗀 0/ 
│  ├─🗀 1/ 
│  ├─🗀 2/ 
│  ├─🗀 4/ 
│  ├─🗀 5/ 
│  ├─...
```

If you wish to use your own dataset click [Here](#use-your-own-data) to see how.

>*Mavi, A., (2020), “A New Dataset and Proposed Convolutional  Neural Network Architecture for Classification of American Sign Language Digits”, arXiv:2011.08927

## Try it yourself
If you want to work on pre-processing the dataset yourself you can use the [notebook](Gesture%20recognition.ipynb). It's not necessary to process all the images yourself. the [dataframes](dataframes) directory contains both the raw points data from the processing method and the pre-processed data.

The [gesture-points-raw](gesture-points-raw.csv) data is not yet cleaned and still contains a large number of missing values. This dataframe can be used if you want to try your own technique of pre-processing the data.

The [gesture-points-processed](gesture-points-processed.csv) contains the pre-processed dataframe. This is the pre-processed version of the raw dataframe. All missing values have been fixed, the data has been normalized. And a flipped version of the dataframe has been appeded. This dataset can be used if you want to try out your own technique in the modeling part of the notebook.

## Use your own data
If you have your own set of gesture images you can use the [notebook](Gesture%20recognition.ipynb) as a starting point. But you have to make sure that the images are put into a folder called 'images'. The structure should look [the same](#dataset) as if you were using the original dataset.


