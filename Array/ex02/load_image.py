import numpy as np
import cv2
import sys

def ft_load(path: str)-> np.ndarray:
    img_cv = cv2.imread(path)
    if img_cv is None:
        sys.exit('Could not open image.')
    return img_cv

def main():

    img_cv = ft_load('/home/morpheus/PPFD/day01/ex02/animal.jpeg')
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    cv2.imshow("Display window", img_cv)
    k = cv2.waitKey(0)
    if k == ord('s'):
        cv2.imwrite('lol.png', img_cv)

    print("The shape of image is : ", img_cv.shape)

if __name__ == '__main__':
    main()
