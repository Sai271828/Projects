**Perceptron**:

A perceptron is essentially a single neuron, We will first dicuss the case of a *binary classifier*, meaning it categorizes input into one of two classes: belonging to the class or not. To do this, we model the neuron using a *weight vector* denoted as `w`. The goal is to update this vector, `w`, in such a way that when given an input vector $\vec{x}$, we can accurately predict its label $y$.

Here's how the algorithm works:

Step 1: Choose a random input vector $\vec{x_i}$ and compute the predicted label $w^T\vec{x_i}$.

Step 2: If the predicted label matches the true label:

         &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Do nothing.
         
       &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Else:
       
         &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Update the weight vector using the rule:  
           $$w \to w - \eta y_ix_i,$$
         &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;where $\eta$ represents the learning rate.

Step 3: Go back to Step 1.

In a more concise form, we can express this update strategy as:
$$w \to w + \eta \mathbb{1}(y_iw^Tx_i < 0)y_ix_i$$

For multiclass classification, we make a simple change by using a "weight matrix" instead of a weight vector. Everything else in the algorithm remains largely the same.

This code can be adapted for Stochastic Gradient Descent (SGD) with different loss functions, such as Support Vector Machines (SVM) or logistic regression. For example, if you want to use logistic regression, you can apply the following update function:
$$w \to w + \eta \sigma(-y_iw^Tx_i)y_ix_i,$$
where $\sigma$ represents the sigmoid function.

