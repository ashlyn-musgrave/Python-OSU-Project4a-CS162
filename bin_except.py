# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 7/16/2023
# Description: This program modifies the binary search from the Exploration so that it raises a
#TargetNotFound exception when the target value is not in the list instead of a -1

class TargetNotFound(Exception):
    pass

def bin_except(a_list, target):
      """Searches a_list for an occurrence of target
      If found, returns the index of its position in the list
      If not found, returns -1, indicating the target value isn't in the list"""
      first = 0
      last = len(a_list) - 1
      while first <= last:
        middle = (first + last) // 2
        if a_list[middle] == target:
          return middle
        if a_list[middle] > target:
          last = middle - 1
        else:
          first = middle + 1
      raise TargetNotFound("TargetNotFound")