import cv2
import os

def plot_voltage():
    file_name = 'src/signal.PNG'
    img = cv2.imread(file_name)
    print(img.shape)
    leftup_corner = [200, 200]  # left up corner to wipe out h-bridge picture

    # plot parameters
    start_a = (int(200), int(120))     # start of pmw at a
    offset = int(237)   # offset between start of pmw at b
    mag = int(100)    # height of wave
    width = int(100)  # period of ware
    img[0:leftup_corner[0], leftup_corner[1]:] = (255, 255, 255)
    color = (155,0, 155)
    thick = 5
    duty_cycle = 0.7

    forward = False

    # plot wave
    for i in range(0, 450, width):
        if forward:
            # plot b
            cv2.line(img, (start_a[0]+offset, start_a[1] + i)[::-1], (start_a[0]+offset - mag, start_a[1] + i)[::-1], color=color,
                     thickness=thick)
            cv2.line(img, (start_a[0]+offset - mag, start_a[1] + i)[::-1],
                     (start_a[0]+offset - mag, start_a[1] + i + int(width*duty_cycle))[::-1], color=color, thickness=thick)
            cv2.line(img, (start_a[0]+offset - mag, start_a[1] + i + int(width*duty_cycle))[::-1],
                     (start_a[0]+offset, start_a[1] + i + int(width*duty_cycle))[::-1], color=color, thickness=thick)
            cv2.line(img, (start_a[0]+offset, start_a[1] + i + int(width*duty_cycle))[::-1], (start_a[0]+offset, start_a[1] + i + width)[::-1],
                     color=color, thickness=thick)
        else:
            # plot a
            cv2.line(img, (start_a[0], start_a[1]+i)[::-1], (start_a[0]-mag, start_a[1]+i)[::-1], color=color, thickness=thick)
            cv2.line(img, (start_a[0]-mag, start_a[1]+i)[::-1], (start_a[0]- mag, start_a[1]+i+int(width*duty_cycle))[::-1], color=color, thickness=thick)
            cv2.line(img, (start_a[0]- mag, start_a[1]+i+int(width*duty_cycle))[::-1], (start_a[0], start_a[1]+i + int(width*duty_cycle))[::-1], color=color, thickness=thick)
            cv2.line(img, (start_a[0], start_a[1]+i+int(width*duty_cycle))[::-1], (start_a[0], start_a[1]+i + width)[::-1], color=color, thickness=thick)



    # put text one
    if forward:
        cv2.putText(img, '3', (start_a[0]-100+offset, start_a[1]-40)[::-1], cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 0), thickness=2)
        cv2.putText(img, str(duty_cycle), (start_a[0]+25+offset, start_a[1]-10+int(width*duty_cycle))[::-1], cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0), thickness=2)
        cv2.putText(img, '1', (start_a[0]+25+offset, start_a[1]-5+width)[::-1], cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0), thickness=2)
        cv2.imshow('forward', img)
        cv2.waitKey(0)
        print(os.path.exists('src'))
        cv2.imwrite('src/forward.png', img)
    else:
        cv2.putText(img, '3', (start_a[0] - 100, start_a[1] - 40)[::-1], cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                    color=(255, 0, 0), thickness=2)
        cv2.putText(img, str(duty_cycle), (start_a[0] + 25, start_a[1] - 10 + int(width * duty_cycle))[::-1],
                    cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 0, 0), thickness=2)
        cv2.putText(img, '1', (start_a[0] + 25, start_a[1] - 5 + width)[::-1], cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5,
                    color=(255, 0, 0), thickness=2)
        cv2.imshow('reverse', img)
        cv2.waitKey(0)
        print(os.path.exists('src'))
        cv2.imwrite('src/reverse.png', img)

