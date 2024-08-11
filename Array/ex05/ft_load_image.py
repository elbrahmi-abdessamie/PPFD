import matplotlib.pylab as plt
import numpy as np
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
        return img_plt