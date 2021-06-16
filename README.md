# gesture recognition

<div align="center">
Real time gesture recognition using OpenCV & Mediapipe
<br />
</div>

<div align="center">
<br />

[![license](https://img.shields.io/github/license/dec0dOS/amazing-github-template.svg?style=flat-square)](LICENSE)
</div>

<p align="center">
  <img src="./examples/example.gif" width="640">
</p>

## Contents
- [About](#about)
- [Features](#features)
- [Getting started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#Usage)
- [Dataset](#dataset)
  - [Details](#details)
  - [Dataframes](#dataframes)
- [Train your own model](#train-your-own-model)
- [Citations](#citations)


## About
Made for my fourth semester with Python. The goal of this project was to create a real time gesture recognition app which is able to recognize american sign language gestures. The [model](./model) that this app uses is able to recognize gestures for digits '0' to '9'. The [notebook](Gesture%20recognition.ipynb) created for this project is flexible, meaning that you are able to use it to create a model with different datasets.

## Features
- __real time:__ gesture recognition in real time
- __multiple hands:__ multiple hands can be recognized at once
- __ambidextrous:__ recognize gestures on both left and right hand
- __debug:__ visualize hand skeleton, confidence & more

## Getting started
### Prerequisites
- Python < 3.0
- A webcam
- pip

### Installation
To install all the dependencies run this command in the command line:
```
pip install -r requirements.txt
```
### Usage
To start the app you will need to run the `gesture.py` file like this
```
python gesture.py
```

## Dataset
The [*](#citataions) [Sign-Language-Digits-Dataset](https://github.com/ardamavi/Sign-Language-Digits-Dataset) was used to train and test the model. 
### Details:
- __Image size:__ 100 x 100 pixels
- __Color space:__ RGB
- __Number of classes:__ 10 (Digits: 0-9)
- __Number of images:__ 2062

The dataset is __not__ contained within this repository. So, if you want to process the images yourself you will have to download the dataset and put all the subfolders into a folder called `images`.


### Dataframes
In the [dataframes](dataframes) direcotry there are two dataframes. The [gesture-points-raw](gesture-points-raw.csv) dataframe contains the raw points data from the processing of the images. This data is not yet cleaned and still contains a large number of missing values. This dataframe can be used if you want to try your own technique of pre-processing the data, without having to download  the dataset and run the processing method. The [gesture-points-processed](gesture-points-processed.csv) contains the pre-processed dataframe. This is the pre-processed version of the [gesture-points-raw](gesture-points-raw.csv) dataframe. All missing values have been fixed, the data has been normalized. And a flipped version of the dataframe has been appeded. This dataset can be used if you want to try your own technique in the modeling part of the notebook.


## Citations
1. Mavi, A., (2020), “A New Dataset and Proposed Convolutional  Neural Network Architecture for Classification of American Sign Language Digits”, arXiv:2011.08927
