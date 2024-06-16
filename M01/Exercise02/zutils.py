import sys 


def slicing_window(num_list, k):
    '''
    input:
        - num_list: an integer list
        - k: the slicer window, for instance k=0: it's mean the each time window moving it will be covered 3 elements.
    output:
        - Return a list of max numbers of the window.
    
    Description:
        Moving the window on the list, each time pick up the max number and record until end of list.
    '''
    if k <= 0:
        print(f"k must be greater than zero.")
        sys.exit()

    max_num = []
    l = len(num_list)

    for i in range(l):
        
        if i + k >= l:
            max_num.append(max(num_list))
            return max_num
        else:
            max_num.append(max(num_list[i : i + k]))
    return max_num


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

# Example usage:
s1 = "kitten"
s2 = "sitting"
distance = levenshtein_distance(s1, s2)
print(f"The Levenshtein distance between '{s1}' and '{s2}' is {distance}.")


    