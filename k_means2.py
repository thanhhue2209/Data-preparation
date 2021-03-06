# -*- coding: utf-8 -*-
"""K_MEANS2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x_Wa8C-M6WVfkVENSb82j6YGhzigae22
"""

from __future__ import print_function 
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist 
import random
import math
np.random.seed(11)

means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)

X = np.concatenate((X0, X1, X2), axis = 0)
K = 3

original_label = np.asarray([0]*N + [1]*N + [2]*N).T

def kmeans_display(X, label):
    K = np.amax(label) + 1
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]
    
    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize = 4, alpha = .8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize = 4, alpha = .8)
    plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize = 4, alpha = .8)

    plt.axis('equal')
    plt.plot()
    plt.show()
    
kmeans_display(X, original_label)

X = np.vstack((X0, X1, X2))
plt.scatter(X[:,0], X[:,1])

"""Hàm khởi tạo tâm """

def kmeans_init_centers(X, k):
    # randomly pick k rows of X as initial centers
    return X[np.random.choice(X.shape[0], k, replace=False)]

plt.scatter(X[:, 0], X[:, 1])
centers = kmeans_init_centers(X, 3)
plt.scatter(centers[:,0], centers[:,1], c  ="y",s = 100)

"""Hàm xác định tâm """

def kmeans_assign_labels(X, centers):
    # calculate pairwise distances btw data and centers
    D = cdist(X, centers)
    # return index of the closest center
    return np.argmin(D, axis = 1)

"""Hàm cập nhật vị trí tâm"""

def kmeans_update_centers(X, labels, centers):
    centers = np.zeros((K, X.shape[1]))
    for k in range(K):
        # collect all points assigned to the k-th cluster 
        Xk = X[labels == k, :]
        # take average
        centers[k,:] = np.mean(Xk, axis = 0)
    return centers

"""Hàm kiểm tra tính hội tụ"""

def kmeans(X, K):
    centers = kmeans_init_centers(X, K)
    while True:
        nearest = kmeans_assign_labels(X, centers)
        old_centers = centers
        new_centers = kmeans_update_centers(X, nearest, centers)
        if np.all(old_centers == centers):
            break
        centers.append(new_centers)
    return nearest, centers

def kmeans_visuallize(X, nearest, centers):
  plt.scatter(X[:,0], X[:,1], c = nearest)
  plt.scatter(centers[:,0], centers[:,1], c = "y", s = 100)
  plt.show()

nearest, centers = kmeans(X, 2)
kmeans_visuallize(X, nearest, centers)

nearest, centers = kmeans(X, 3)
kmeans_visuallize(X, nearest, centers)

nearest, centers = kmeans(X, 4)
kmeans_visuallize(X, nearest, centers)