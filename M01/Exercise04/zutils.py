import sys 
import cv2
import numpy as np


def load_vocab(filename):
    try:
        
        with open(filename) as f:
            lines = f.readlines()
        
        words = sorted(set([line.strip().lower() for line in lines]))
        
        return  words 
    
    except FileNotFoundError:
        print("File does not exist!")


def count_char(words):
    '''
    Description: count the number of time of a letter appears in a word.
    Input: a word or string
    Output: return a dictionary with key is the charactor and value is 
            the number of char repetitive in the word or string.
    '''
    d = {}

    for char in words:

        if char not in d: 
            d[char] = 1
        else:
            d[char] += 1

    return d


def count_word(s:str):
    '''
    Description: count the number of time of a word appears in a string.
    Input: a word or string
    Output: return a dictionary with key is the word and value is 
            the number of times the word appears on the string.
    '''
    
    d = {}
    words = s.lower().split()

    for w in words:

        if w not in d: 
            d[w] = 1
        else:
            d[w] += 1

    return d


def levenshtein_distance(s1, s2):
    """
    Calculate the Levenshtein distance between two strings.

    Parameters:
    s1 (str): The first string.
    s2 (str): The second string.

    Returns:
    int: The Levenshtein distance between the two strings.
    """
    # Initialize a matrix to store the distances
    distance_matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    # Initialize the first row and column with incremental values
    for i in range(len(s1) + 1):
        distance_matrix[i][0] = i
    for j in range(len(s2) + 1):
        distance_matrix[0][j] = j

    # Fill in the matrix based on the minimum cost of edit operations
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            distance_matrix[i][j] = min(distance_matrix[i - 1][j] + 1,  # Deletion
                                        distance_matrix[i][j - 1] + 1,  # Insertion
                                        distance_matrix[i - 1][j - 1] + cost)  # Substitution

    # Return the Levenshtein distance (value at the bottom-right corner of the matrix)
    return distance_matrix[len(s1)][len(s2)]


MODEL = "F:/AIO/AIO2024/M01/Exercise04/model/MobileNetSSD_deploy.caffemodel"
PROTOTXT = "F:/AIO/AIO2024/M01/Exercise04/model/MobileNetSSD_deploy.prototxt.txt"

def process_image ( image ):
    blob = cv2.dnn . blobFromImage (
    cv2 . resize (image , (300 , 300) ), 0.007843 , (300 , 300) , 127.5)
    net = cv2.dnn. readNetFromCaffe ( PROTOTXT , MODEL )
    net . setInput ( blob )
    detections = net. forward ()
    return detections


def annotate_image (image , detections , confidence_threshold =0.5):
    # loop over the detections
    (h, w) = image . shape [:2]
    conf_score = []
    for i in np. arange (0, detections . shape [2]) :
        confidence = detections [0, 0, i, 2]

        if confidence > confidence_threshold :
            # extract the index of the class label from the 'detections',
            # then compute the (x, y)-coordinates of the bounding box for the object
            idx = int( detections [0, 0, i, 1])
            box = detections [0, 0, i, 3:7] * np. array ([w, h, w, h])
            (startX , startY , endX , endY ) = box.astype("int")
            #Print the lable ID
            cv2.putText(image, f"ObjectID: {i}",(startX + 10, startY + 25),fontFace=1, fontScale=1.5, color=(255,0,0), thickness=2)
            #Draw the rectangle surround object
            cv2 . rectangle (image , (startX , startY ), (endX , endY ), (0,255,0), 3)
            conf_score.append(confidence)
    return image, conf_score