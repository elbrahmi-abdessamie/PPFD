import matplotlib.pylab as plt
import numpy as np
from PIL import Image
import cv2
from ft_load_image import ft_load

def ft_invert(array: np.ndarray) -> np.ndarray:
    invert_img = array[:,:,:3]
    return (255 - invert_img)

def ft_red(array: np.ndarray)->np.ndarray:
    
    red_filter = np.zeros_like(array)
    red_channel = array[:,:,0]
    red_filter[:,:,0] = red_channel
    return red_filter

def ft_green(array: np.ndarray)->np.ndarray:
    green_filter = np.zeros_like(array)
    green_channel = array[:,:,1]
    green_filter[:,:,1] = green_channel
    return green_filter

def ft_blue(array: np.ndarray)->np.ndarray:
    blue_filter = np.zeros_like(array)
    blue_channel = array[:,:,2]
    blue_filter[:,:,2] = blue_channel
    return blue_filter

def ft_grey(array:np.ndarray)->np.ndarray:
    red_channel = array[:,:,0] / 3
    green_channel = array[:,:,1] / 3
    blue_channel = array[:,:,2] / 3
    grey_scale = red_channel + green_channel + blue_channel
    grey_channel = np.asarray(grey_scale, dtype=int)
    grey_filter = np.stack([grey_channel, grey_channel, grey_channel], axis=-1)
    print(grey_filter.shape)

    # grey_scale = np.stack([grey_channel, grey_channel, grey_channel], axis=-1)
    # print(grey_scale.shape)
    # return grey_scale
    
    return grey_filter

def main():
    try:
        img_arr = ft_load("landscape.jpg")
        img_arr = ft_grey(img_arr)
        plt.imshow(img_arr)
        plt.show()
    except(FileNotFoundError, OSError, Exception) as err:
        print("Error: ", err)

if __name__ == "__main__":
    main()