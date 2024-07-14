# Pascal Dataset Classification
In this project, Convolutional Neural Networks (CNNs) are used to classify images from the [Pascal dataset](http://host.robots.ox.ac.uk/pascal/VOC/voc2007/).

- **AlexNet**: Utilizing a pretrained AlexNet model ([AlexNet](#ref2)), we fine-tune it to classify images in the Pascal dataset. See the implementation [here](https://github.com/Sai271828/Projects/blob/master/Pascal%20dataset%20detection/Alex_net.ipynb).
  
- **Custom CNN**: We designed a custom CNN to classify images in the Pascal dataset. Training this network requires significant computational resources, so I used Google Cloud Platform (GCP) instances. Training on a personal computer may take considerably longer. The implementation can be found [here](https://github.com/Sai271828/Projects/blob/master/Pascal%20dataset%20detection/customCNN.ipynb).


## References

<a name="ref2"></a>Krizhevsky, Alex; Sutskever, Ilya; Hinton, Geoffrey E. (2017-05-24). "ImageNet classification with deep convolutional neural networks" (PDF). *Communications of the ACM*. 60 (6): 84–90. doi:[10.1145/3065386](https://doi.org/10.1145/3065386). ISSN 0001-0782. S2CID [195908774](https://www.semanticscholar.org/paper/195908774).