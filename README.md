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
  - [Usage](#usage)
- [Dataset](#dataset)
- [Work with the data](#work-with-the-data)
- [Use your own data](#use-your-own-data)
- [License](#license)

## About
Made for my fourth semester with Python. The goal of this project was to create a real time gesture recognition app which is able to recognize american sign language gestures. The [model](./model) that this app uses is able to recognize gestures for digits '0' to '9'. The [notebook](Gesture%20recognition.ipynb) explains how this model was made.

## Features
- __real time:__ gesture recognition in real time
- __multiple hands:__ multiple hands can be recognized at once
- __ambidextrous:__ recognize gestures on both left and right hand
- __debug:__ visualize hand skeleton, confidence & more

## Setup
### Prerequisites
- Camera/Webcam
- [Python](https://www.python.org/) > 3.0

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
The *[Sign Language Digits Dataset](https://github.com/ardamavi/Sign-Language-Digits-Dataset) was used to train and test the model. 

>*Mavi, A., (2020), “A New Dataset and Proposed Convolutional  Neural Network Architecture for Classification of American Sign Language Digits”, arXiv:2011.08927

This repository does __NOT__ contain this data. So, if you want to process the images yourself you will have to download the dataset and put all the subfolders into a folder called `images`.
The structure should look like this:
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

## Work with the data
If you want to work on pre-processing the dataset yourself you can use the [notebook](Gesture%20recognition.ipynb). It's not necessary to process all the images yourself. the [`dataframes`](dataframes) directory contains both the raw points data and the pre-processed data.

The [gesture-points-raw](dataframes/gesture-points-raw.csv) data is not cleaned and contains a number of missing values. This dataframe can be used if you want to try your own technique of pre-processing.

The [gesture-points-processed](dataframes/gesture-points-processed.csv) contains the pre-processed dataframe. This is the pre-processed version of the raw dataframe. All missing values have been fixed, the data has been normalized and a flipped version of the dataframe has been appeded. This dataset can be used if you want to try out your own technique of modeling.

## Use your own data
The [notebook](Gesture%20recognition.ipynb) should also work with other datasets of gesture images. But you have to make sure that the images are put into a folder called `images`. The structure should look [the same](#dataset) as if you were using the original dataset. The openpose hand model is __NOT__ included inside this repository. This model can be downloaded [here](https://www.kaggle.com/changethetuneman/openpose-model?select=pose_iter_102000.caffemodel), and needs to be put in the [`openpose`](openpose) directory.

## License

This software is licensed under [MIT](LICENSE)
