"""Perceptron model."""

from operator import matmul
import numpy as np


class Perceptron:
    def __init__(self, n_class: int, lr: float, epochs: int):
        """Initialize a new classifier.

        Parameters:
            n_class: the number of classes
            lr: the learning rate
            epochs: the number of epochs to train for
        """
        
        self.lr = lr
        self.epochs = epochs
        self.n_class = n_class

    def train(self, X_train: np.ndarray, y_train: np.ndarray):
        """Train the classifier.

        Use the perceptron update rule as introduced in the Lecture.

        Parameters:
            X_train: a number array of shape (N, D) containing training data;
                N examples with D dimensions
            y_train: a numpy array of shape (N,) containing training labels
        """
        
        # TODO: implement me
        #code for binary clasfier
        if self.n_class==2:
          #initializing random weights
          self.w = np.random.rand(len(X_train[0]))
          for i in range(self.epochs):
            #introducing a small decay for the learning rate as a function of epochs
            self.lr=self.lr-(self.lr*i)/self.epochs

            #sampling a random index to perform SGD
            a=np.random.choice(len(X_train),1)
            r_array=np.dot(X_train[a[0]],self.w)
            corr_class=y_train[a[0]]

            #conditional statement to check whether it is classfied wrond
            if (r_array>=0 and corr_class!=1) or (r_array<0 and corr_class==1):
              #update weights
              if corr_class!=1:
                #update weights but multiply by -1
                self.w=self.w-self.lr*X_train[a[0]]
                
              else:
                
                self.w=self.w+self.lr*X_train[a[0]]
        #code for multiclass classifier
        if self.n_class>2:
          #initializing random weights
          self.w = np.random.rand(len(X_train[0]),self.n_class)
          lr=self.lr
          for i in range(self.epochs):
            #introducing a small decay for the learning rate as a function of epochs
            self.lr=lr-(i*lr)/(self.epochs)

            #sampling a random index to perform SGD
            a=np.random.choice(len(X_train),1)
            r_array=np.matmul(X_train[a[0]],self.w)

            #converting to list to get index of an item
            #numpy has no method index
            r=r_array.tolist()
            corr_class=y_train[a[0]]
            if r.index(max(r))!=corr_class:
              #update weights for a multiclass perceptron
              for j in range(self.n_class):
                if j!=corr_class and r[j]>r[corr_class]:
                  self.w[:,j]=self.w[:,j]-self.lr*X_train[a[0]]
                  self.w[: ,corr_class]=self.w[:,corr_class]+self.lr*X_train[a[0]]

      

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        """Use the trained weights to predict labels for test data points.

        Parameters:
            X_test: a numpy array of shape (N, D) containing testing data;
                N examples with D dimensions

        Returns:
            predicted labels for the data in X_test; a 1-dimensional array of
                length N, where each element is an integer giving the predicted
                class.
        """
        # TODO: implement me
        ans=np.zeros(len(X_test))
        for i in range(len(X_test)):
          #code for predicting binary classifier
          if self.n_class==2:
            r_array=np.dot(X_test[i],self.w)
            if r_array>=0:
              ans[i]=1
            else:
              ans[i]=0
          #code for predicting multiclass classifier
          else:
            r_array=np.matmul(X_test[i],self.w)
            r=r_array.tolist()
            ans[i]=r.index(max(r))
          #converting back to int from float
          int_ans=ans.astype(int)
        return int_ans
