import cv2
import numpy as np

def add_label(image, label, position=(10, 180)):
    labeled_image = image.copy()
    cv2.putText(labeled_image, label, position, cv2.FONT_HERSHEY_SIMPLEX, 8, (255, 255, 255), 3, cv2.LINE_AA)
    return labeled_image

def grayscale_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply adaptive histogram equalization for better contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray = clahe.apply(gray)
    return gray

def bilateral_filter_image(image, d=5, sigmaColor=50, sigmaSpace=50):
    # Apply bilateral filtering to reduce noise while preserving edges
    bilateral_filtered = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)
    return bilateral_filtered

def blur_image(image, kernel_size=(5, 5)):
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(image, kernel_size, 0)
    return blurred
    
def find_edges(image):
    # Apply Canny edge detection with adjusted thresholds
    edges = cv2.Canny(image, 30, 100)  # You can tweak these values
    return edges
    
def morphological_transform(image, kernel_size=(20, 20)):
    # Morphological transformations
    kernel = np.ones(kernel_size, np.uint8)
    morph_transformed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return morph_transformed

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = grayscale_image(image)
    edges_post_gray = find_edges(gray)
    filtered = bilateral_filter_image(gray)
    edges_post_filter = find_edges(filtered)
    blurred = blur_image(filtered, (5, 5))
    edges_post_blurred = find_edges(blurred)
    morphed_edges = morphological_transform(edges_post_blurred)
    
    gray_labeled = add_label(edges_post_gray, 'Edges Post Grayscale')
    filtered_labeled = add_label(edges_post_filter, 'Edges Post Bilateral Filter')
    blurred_labeled = add_label(edges_post_blurred, 'Edges Post Blur')
    morphed_edges_labeled = add_label(morphed_edges, 'Morphed Edges')
    
    return gray_labeled, filtered_labeled, blurred_labeled, morphed_edges_labeled

def stack_images(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0][0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


# Example usage
image_path = 'empty_board.png' 
gray, filtered, blurred, edges = preprocess_image(image_path) 
stacked_images = stack_images(0.5, [[gray, filtered], [blurred, edges]])
cv2.imshow('Process Stages', stacked_images)
cv2.imwrite('edges.png', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
