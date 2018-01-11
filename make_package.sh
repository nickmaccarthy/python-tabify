#!/bin/bash

# builds our packages for pypi
echo "building virtualenv..."
virtualenv env 
source env/bin/activate
echo "installing requirements..."
pip install -r requirements.txt

echo "Removing any previous build dir..."
rm -rf build
echo "Removing any previous dist dir..."
rm -rf dist

echo "Building for python 2.x..."
python setup.py sdist bdist_wheel
echo "Building for python 3.x..."
python3 setup.py sdist bdist_wheel

echo "Running twine upload..."
twine upload dist/*
