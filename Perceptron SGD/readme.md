**Perceptron**:

A perceptron is basically a single neuron. This is modeled using a *weight matrix* `w`. Our goal is to update the matrix `w`, so that given a input vector $\vec{x}$, we want to correctly predict its label $y$.
The algorithm we use is as follows:  

Step 1: Choose a random input vector $\vec{x_i}$ and compute the predicted label $w^T\vec{x_i}$.   
Step 2: If the predicted label is same as the true label:  
          &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;do nothing.  
         &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else:  
          &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update the weight by the rule  
          $$w \to w - \eta y_ix_i,$$
           &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;where $\eta$ is the learning rate.  
Step 3: Go back to Step 1.  
We can rewrite this update strategy succintly as follows:  
$$w \to w + \eta \mathbb{1}(y_iw^Tx_i < 0)y_ix_i$$

You can easily adapt this code to obtain SGD for different loss functions like SVM, logistic regression, and more.
For instance, if you want to use logistic regression just use the following update function.
$$w \to w + \eta \sigma(-y_iw^Tx_i)y_ix_i,$$
where $\sigma$ is the sigmoid function.
