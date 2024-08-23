# Bone Age Predictor

This repository contains a web-based application designed to predict bone age from hand radiographs using deep learning. The project leverages the [RSNA Bone Age Dataset](https://www.kaggle.com/datasets/kmader/rsna-bone-age), a widely recognized dataset in medical imaging, to train and validate a Convolutional Neural Network (CNN) model. The interface, built with `Gradio`, allows users to interactively upload hand radiographs and receive bone age predictions.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training and Architecture](#model-training-and-architecture)
- [Evaluation](#evaluation)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Interactive Web Interface:** Upload hand radiographs and get real-time bone age predictions.
- **Deep Learning:** Utilizes a CNN trained on the RSNA Bone Age Dataset.
- **Easy Deployment:** Built using `Gradio`, making it simple to run locally or deploy on cloud platforms.
- **Comprehensive Dataset:** Trained on a dataset with 12,000+ images, ensuring robust predictions.

## Demo

![Bone Age Predictor](demo_screenshot.png)

Experience the live demo of the application [here](http://localhost:8501/).

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/bone-age-predictor.git
cd bone-age-predictor

### File struture
bone-age-predictor/
├── app.py                 # Main application script
├── bone_age_model.h5      # Trained deep learning model
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── demo_screenshot.png    # Screenshot for the README
