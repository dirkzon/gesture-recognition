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
  - [Installation](#installation)
  - [Usage](#Usage)


## About
Made for my fourth semester with Python. The goal of this project was to create a real time gesture recognition app which is able to recognize american sign language gestures. The [model](./model) that this app uses is able to recognize gestures for digits '0' to '9'. The [notebook](Gesture%20recognition.ipynb) explains how this model was made.

## Features
- __real time:__ gesture recognition in real time
- __multiple hands:__ multiple hands can be recognized at once
- __ambidextrous:__ recognize gestures on both left and right hand
- __debug:__ visualize hand skeleton, confidence & more

## Getting started

### Installation
To install all the dependencies run this command in the command line
```
pip install -r requirements.txt
```
### Usage
To start the app you will need to run the `gesture.py` file
```
python gesture.py
```
Press 'd' to enter debug mode

## Dataset
The *[Sign-Language-Digits-Dataset](https://github.com/ardamavi/Sign-Language-Digits-Dataset) was used to train and test the model. 
The dataset is __not__ contained within this repository. So, if you want to process the images yourself you will have to download the dataset and put all the subfolders into a folder called `images`. If you wish to use your own dataset click here to see how.

>*Mavi, A., (2020), “A New Dataset and Proposed Convolutional  Neural Network Architecture for Classification of American Sign Language Digits”, arXiv:2011.08927

