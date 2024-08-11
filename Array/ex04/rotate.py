import matplotlib.pylab as plt
import numpy as np
from PIL import Image
import cv2




def ft_load(path: str)->np.ndarray:
    try:
        f = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path.split('/')[-1]} not found. ")
    except OSError:
        raise OSError(f"OS error occurred trying to open {path}")
    except Exception as err:
        raise Exception(f"Unexpected error opening {path} is",repr(err))
    else:
        img_plt = plt.imread(path)
        return cv2.cvtColor(img_plt, cv2.COLOR_RGB2GRAY)

# def transpose_matrix(arr: np.ndarray)->np.ndarray:
#     cols, raws = arr.shape[:2]
#     transposed = np.zeros((raws, cols))
#     for i in range(cols):
#         for j in range(raws):
#             transposed[j][i] = arr[i][j]
#     return transposed

def rotate(img: np.ndarray):
    '''
    Select a region of intress then Transpose and flip it 90 conter clockwise the matrix
    '''
    def roi(x, y, **kw):
        roi = img[y:y+kw['height'], x:x+kw['width']]
        return roi
    def transpose_matrix(x, y, **kw)->np.ndarray:
        img = roi(x, y, **kw)
        cols, raws = img.shape
        transposed = np.zeros((raws, cols))
        for i in range(cols):
            for j in range(raws):
                transposed[j][cols -1 - i] = img[cols - 1 - i][raws - 1 - j]
        return transposed
    return transpose_matrix

try:
    plt_arr = ft_load('/home/morpheus/PPFD/day01/ex04/animal.jpeg')
    plt_arr = rotate(plt_arr)(500, 290, height=400, width=400)
    plt_arr = rotate(plt_arr)(0, 0, height=400, width=400)
    plt_arr = rotate(plt_arr)(0, 0, height=400, width=400)
    print(plt_arr.shape)
    plt.imshow(plt_arr, cmap='gray')
    plt.show()
except (FileNotFoundError, OSError, Exception) as err:
    print("Error: ",err)