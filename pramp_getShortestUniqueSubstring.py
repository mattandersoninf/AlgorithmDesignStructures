# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:56:13 2017

@author: mattanderson
"""

# Interesting Pramp problem
# this function takes a string and an array of characters tries to find the
# shortest unique substring consisting of the characters from the array
# ideally you want a linear time complexity.
# if N is the length of the string and M is the length o the array
# the way this function is written, you achieve a time complxity of O(N+M)
# you achieve a space complexity of O(M) since the hash table is composed of
# elements from the array and their counters

def get_shortest_unique_substring(arr, string):
  # use this index to keep track of the starting index of substrings
  head_index = 0
  # unique character counter
  unique_counter = 0
  # base case
  output = ""
  # dict containing all values from arr
  unique_chars = {}
  # fill dictionary with unique characters from arr
  for i in range(len(arr)):
    unique_chars[arr[i]] = 0
  # loop thorugh the string to get all of substring indexes
  for tail_index in range(len(string)):
    tail_char = string[tail_index]
    # if the character you're looking at isn't in the arr, skip it
    if tail_char not in unique_chars.keys():
      #print("value was skipped",)
      continue
    # set tailCount to the value held in the unique chars dictionary
    tailCount = unique_chars[tail_char]
    # if you have not visited the specified value before, the number unique values you've visted increases
    if tailCount == 0:
      unique_counter += 1
    # increment the value associated with the key
    unique_chars[tail_char] = tailCount + 1
    # now that you've found a substring with all of the
    while unique_counter == len(arr):
      # get the length of the substring you're comparing against
      temp_len = tail_index - head_index + 1
      # if the temp length is the same as the length of arr, you found your answer
      if temp_len == len(arr): return string[head_index:tail_index+1]
      # if your substring is less than the length of the current ouput or if the current output is an empty string, now it's equal to the current substring from string
      if output == "" or temp_len < len(output): output = string[head_index:(tail_index+1)]
      # hold the character at the head index
      head_char = string[head_index]
      # if the current element that you're looking at is a key in the dictionary, decrement it's value
      if head_char in unique_chars.keys():
        headcount = unique_chars[head_char] - 1
        # if the key's value is 0, decrement the unique counter so that you can search for a new instance of this key
        if headcount == 0: unique_counter -= 1
        # modify the headcount in the dictionary to this key
        unique_chars[head_char] = headcount
      # increment the pointer fo rhte subrstring  
      head_index += 1
      
  return output
# sample input: arr = ['x','y','z'], string = "xyyzyzyx"
# sample output: "zyx"