import numpy as np
import matplotlib.pyplot as plt



def plot_data():
    data = np.loadtxt('hw3data.txt')
    data = data[2:150] * 1000
    print(data)


    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle('processing time')
    ax1.plot(data)
    ax1.set(xlabel ='processing time [msec]', ylabel = 'frame')
    ax1.set_title('Object Tracking \nProcessing Time')

    ax2.hist(data, width=0.95)
    ax1.set(ylabel='processing time [msec]', xlabel='frame')
    ax1.set_title('Object Tracking \nProcessing Time')

    plt.show()




