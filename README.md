# Bone Age Predictor

This repository contains a web-based application for predicting bone age using machine learning. The application is built using Python, `TensorFlow/Keras` for deep learning, and `Gradio` for the user interface. This project is designed to provide an accessible tool for estimating bone age from hand radiographs, utilizing the [RSNA Bone Age Dataset](https://www.kaggle.com/datasets/kmader/rsna-bone-age).

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)

## Features

- **Interactive Web Interface:** Users can upload hand radiographs to predict bone age.
- **Deep Learning Model:** The application uses a Convolutional Neural Network (CNN) trained on the RSNA Bone Age Dataset.
- **User-Friendly:** The interface is built with Gradio, making it accessible and easy to use.
- **Scalable:** Can be easily deployed in various environments, including cloud platforms.

## Demo

![Bone Age Predictor](demo_screenshot.png)

You can view a live demo of the application [http://localhost:8501/]().

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/bone-age-predictor.git
cd bone-age-predictor


