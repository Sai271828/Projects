
# Project Repository

This repository contains several machine learning projects that I worked on as part of a Deep Learning course.


## Perceptron
This was my first introduction to machine learning, focusing on a single neuron model. The weights are adjusted using stochastic gradient descent. You can apply this model to the [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) dataset.

## Pascal Dataset Classification
In this project, Convolutional Neural Networks (CNNs) are used to classify images from the [Pascal dataset](http://host.robots.ox.ac.uk/pascal/VOC/voc2007/).

- **AlexNet**: Utilizing a pretrained AlexNet model ([AlexNet](#ref2)), we fine-tune it to classify images in the Pascal dataset. See the implementation [here](https://github.com/Sai271828/Projects/blob/master/Pascal%20dataset%20detection/Alex_net.ipynb).
  
- **Custom CNN**: We designed a custom CNN to classify images in the Pascal dataset. Training this network requires significant computational resources, so I used Google Cloud Platform (GCP) instances. Training on a personal computer may take considerably longer. The implementation can be found [here](https://github.com/Sai271828/Projects/blob/master/Pascal%20dataset%20detection/customCNN.ipynb).


## YOLO Loss Function Project

This repository contains a project where I implemented the YOLO (You Only Look Once) loss function ([Redmon et al. 2016](#ref1)) for object detection tasks.

### Overview
YOLO is a state-of-the-art object detection system known for its speed and accuracy. This project focuses on implementing the YOLO loss function and applying it to the [Pascal dataset](http://host.robots.ox.ac.uk/pascal/VOC/voc2007/).

### Results
The repository includes sample results obtained from training the YOLO model using the implemented loss function in the [Yolo Notebook](https://github.com/Sai271828/Projects/blob/master/YOLO/Yolo%20notebook.pdf).

## References


<a name="ref1"></a>Redmon, J., Divvala, S., Girshick, R., & Farhadi, A. (2016). You Only Look Once: Unified, Real-Time Object Detection. *arXiv preprint arXiv:1506.02640*. Retrieved from https://arxiv.org/abs/1506.02640 

<a name="ref2"></a>Krizhevsky, Alex; Sutskever, Ilya; Hinton, Geoffrey E. (2017-05-24). "ImageNet classification with deep convolutional neural networks" (PDF). *Communications of the ACM*. 60 (6): 84–90. doi:[10.1145/3065386](https://doi.org/10.1145/3065386). ISSN 0001-0782. S2CID [195908774](https://www.semanticscholar.org/paper/195908774).






