#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   regression.py    
@Github  :   https://github.com/StrikerCC

@Modify Time      @Author       @Version    @Desciption
------------      -------       --------    -----------
5/4/2021 1:34 PM   Cheng Chen    1.0         None
'''

# import lib
import numpy as np
import matplotlib.pyplot as plt


def linear_regression(data):
    fit = np.zeros(data.shape[1], data.shape[1])



    print(fit)
    plt.scatter(data[:, 0], data[:, 1])
    plt.show()
    pass


def polynomial_regression(data):
    pass


def incline(data):
    trans = np.array([[1, 1],
                      [0, 1]])
    data = np.matmul(data, trans)
    return data


def main():
    x = np.expand_dims(np.arange(-10, 10, 0.1), axis=1)
    y = np.random.rand(x.shape[0], x.shape[1])
    data = np.concatenate((x, y), axis=1)
    data = incline(data)

    print(data.shape)
    print(x.shape)
    print(y.shape)

    linear_regression(data)


if __name__ == '__main__':
    main()
