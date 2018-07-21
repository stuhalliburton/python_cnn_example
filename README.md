# Python CNN Example

## Tutorial

https://www.learnopencv.com/image-classification-using-convolutional-neural-networks-in-keras/

## Requirements

- `python 2.7.*`


## Setup

```bash
git clone git@github.com:stuhalliburton/python_cnn_example.git
cd python_cnn_example
pip install requirements.txt
```

## Docker

```bash
docker build -t python-cnn .
docker run -v $(pwd)/saved_models:/src/saved_models python-cnn python train_cnn.py
docker run -v $(pwd)/saved_models:/src/saved_models python-cnn python predict_cnn.py
```
