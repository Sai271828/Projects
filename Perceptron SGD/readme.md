**Perceptron**:

A perceptron is basically a single neuron. This is modeled using a *weight matrix* `w`. Let us say 
$$w \to w + \eta \mathbb{1}(y_iw^Tx_i < 0)y_ix_i$$
$$w \to w + \eta \sigma(-y_iw^Tx_i)y_ix_i$$
Here is the code I've written for implementing Stochastic Gradient Descent (SGD) for a perceptron. You can easily adapt this code to obtain SGD for different loss functions like SVM, logistic regression, and more.
