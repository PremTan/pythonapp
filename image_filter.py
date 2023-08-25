import cv2
import numpy as np

def apply_grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def apply_blur(image, kernel_size=5):
    blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return blurred

def main():
    # Load an image
    image_path = 'path_to_your_image.jpg'  # Provide the actual path to your image
    image = cv2.imread(image_path)

    while True:
        cv2.imshow('Original', image)

        key = cv2.waitKey(0)

        if key == ord('g'):
            gray_image = apply_grayscale(image)
            cv2.imshow('Grayscale', gray_image)

        elif key == ord('b'):
            blurred_image = apply_blur(image)
            cv2.imshow('Blurred', blurred_image)

        elif key == 27:  # Esc key to exit
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
