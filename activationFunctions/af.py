#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   af.py    
@Github  :   https://github.com/StrikerCC

@Modify Time      @Author       @Version    @Desciption
------------      -------       --------    -----------
5/10/2021 1:29 PM   Cheng Chen    1.0         None
'''

# import lib
import numpy as np
import matplotlib.pyplot as plt


def mish(x):
    """
    mish function value step by step
    :param x:
    :type x:
    :return:
    :rtype:
    """
    assert isinstance(x, np.ndarray)
    x0 = 1 + np.exp(x)
    x1 = np.log(x0)
    x2 = np.tanh(x1)
    x3 = x * x2
    return x0, x1, x2, x3


def main():
    x = np.arange(-5, 5, 0.1)
    x0, x1, x2, x3 = mish(x)

    ax0 = plt.subplot(3, 2, 1)
    plt.plot(x, x0)
    plt.ylabel('1 + np.exp(x)')

    ax1 = plt.subplot(3, 2, 2)
    plt.plot(x, x1)
    plt.ylabel('np.log(x0)')

    ax2 = plt.subplot(3, 2, 3)
    plt.plot(x, x2)
    plt.ylabel('np.tanh(x1)')

    ax3 = plt.subplot(3, 2, 4)
    plt.plot(x1, x2)
    plt.xlabel('x1')
    plt.ylabel('np.tanh(x1)')

    ax4 = plt.subplot(3, 2, 5)
    plt.plot(x, x3)
    plt.ylabel('x * x2')

    ax6 = plt.subplot(3, 2, 6)
    plt.plot(x2, x3)
    plt.xlabel('x2')
    plt.ylabel('x * x2')

    plt.subplots_adjust(wspace=0.6, hspace=1.6, left=0.1, bottom=0.22, right=0.96, top=0.96)
    plt.show()


if __name__ == '__main__':
    main()
