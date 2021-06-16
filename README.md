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
  - [Run the app](#run-the-app)


## About
Made for my fourth semester with Python and Jupyter Notebook. The goal of this project was to create a real time gesture recognition app which is able to recognize american sign language gestures. The [model](./model) that this app uses is able to recognize gestures for digits '0' to '9'. The [notebook](Gesture%20recognition.ipynb) created for this project is flexible, meaning that you are able to use it to create a model with different datasets.

## Features
- __real time:__ gesture recognition in real time
- __multiple hands:__ multiple hands can be recognized at once
- __ambidextrous:__ recognize gestures on both left and right hand
- __debug:__ visualize hand skeleton, confidence & more

## Getting started
### Prerequisites
To run this program you will first need to have python installed. Version 3.92 was used to develop this project. And pip was used to handle the dependencies. These dependencies will need to be installed. This can be done with the [requirements.txt](requirements.txt) file.
```
pip install -r requirements.txt
```
### Run the app
To run the app you will need to run the `gesture.py` file like this
```
python gesture.py
```
