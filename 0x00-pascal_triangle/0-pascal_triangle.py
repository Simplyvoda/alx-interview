#!/usr/bin/python3
'''
This module creates an array that represents Pascal's triangle.
'''


def pascal_triangle(n):
  '''
  This function creates a parent list that represents Pascal's triangle
  and smaller lists
  '''
  # Create a list that represents Pascal's triangle.
  parent_list = []
  # If n is zero or less, return empty list that prints nothing
  if n <= 0:
      return parent_list
  # If n is greater than zero create first list with element 1
  parent_list.append([1])
  # To create lists in case n is greater than 1
  for i in range(1, n):
      # Creating outer loop and initializing first element to 1
      child_list = [1]
      for j in range(1, i):
          sum_val = parent_list[i-1][j-1] + parent_list[i-1][j]
          child_list.append(sum_val)
      # Each row ends with 1
      child_list.append(1)
      parent_list.append(child_list)
  return parent_list