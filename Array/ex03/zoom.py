import cv2
import numpy as np
from sys import exit

def zoom_roi(image, x, y, width, height)-> np.ndarray:
    '''
    Extract region of interest then scall this region
    '''
     # Extract ROI
    roi = image[y:y+height, x:x+width]
    
    zoomed = cv2.resize(roi, (400, 400), interpolation=cv2.INTER_LINEAR)
    return zoomed

def main():
    # Load an image
    img = cv2.imread('/home/morpheus/PPFD/day01/ex03/animal.jpeg')
    if img is None:
        exit('Could not open image.')
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Define ROI parameters
    x, y = 480, 200  # Top-left corner of ROI
    width, height = 300, 300  # Size of ROI
    # Apply zoom to ROI
    zoomed_roi = zoom_roi(img_gray, x, y, width, height)
    # Display or save the result
    cv2.imshow('Zoomed animal', zoomed_roi)
    print(f"The shape of image is: {zoomed_roi.shape}", zoomed_roi, sep='\n')
    key = cv2.waitKey(0)
    if key is ord('c'):
        cv2.destroyAllWindows()
    

if __name__ == '__main__':
    main()
