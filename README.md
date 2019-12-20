# Color Reducer

Script use K-Means algorithm to reduce color palette

## Getting Started

Upload your image to directory "images" 


#### Built With

* [Scikit-learn](https://scikit-learn.org/) - a set of python modules for machine learning
* [CV2](https://opencv.org) - module for working with images
* [Matplotlib](https://matplotlib.org/) - for interactive graphing

#### Installing
Download packages
```
pip install scikit-learn 
pip install opencv-python
pip install matplotlib
```

#### Running script
```
python main.py -start filename n_colors
```

#### Example
```
python main.py -start rainbow.jpg 5
```

##### Input
![Image](https://github.com/boyfromasia/reduce_color_script/raw/master/images/rainbow.png)

##### Output
* Recolored image

![Image](https://github.com/boyfromasia/reduce_color_script/raw/master/output/recolored.png)

* Visualize the results by plotting the data colored by these labels. 

![Image](https://github.com/boyfromasia/reduce_color_script/raw/master/images/plot.png)


## Authors

* **Nguen Za Chong** - *Initial work* - [boyfromasia](https://github.com/boyfromasia)
