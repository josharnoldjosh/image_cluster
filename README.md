# Image Cluster
Clusters similar images into specified sets.

## Requirements
* Keras
* Pandas
* Tensorflow
* Python3

## Usage
1. Make sure the python files are in the same directory as all the images you want to cluster
2. Run `python3 cluster.py -h` to find out more (optional)
3. Run `python3 cluster.py`

## Example
`python3 cluster.py -i 20 -g 5000 -s y`
In this example, the code will cluster the first 5,000 images it finds into image sets that each contain 20 similar images.
In the `output/` folder, `1` is the most similar image set, `2` is the second most similar image set and so on.
