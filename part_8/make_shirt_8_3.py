# coding=utf-8
# 详细说明见书P120

def shirt(size, word = 'NB'):
    """display the information of my shirt"""
    print("\nThe size of shirt is " + size + ".")
    print("Please print " + word + " on the shirt.")

shirt('M', 'love')
shirt('L')

def shirt(size, word = 'I love Python'):
    """display the information of my shirt"""
    print("\nThe size of shirt is " + size + ".")
    print("Please print '" + word + "' on the shirt.")

shirt('L')
