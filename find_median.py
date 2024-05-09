#Author: Jovane Cano
#GitHub Username: jovanecano
#Date: 05/08/2024
#Description:
"""This function takes a list of numbers as a parameter and returns the median value"""


def find_median(values):
    """find_median function will first sort the values, count the length of the list and then determine what calculation to
    perform based on whether the number of values in the list is odd or even"""
    sorted_vals = sorted(values)

    length = len(sorted_vals)

    if length % 2 == 0:
        """if statement that if the number of sorted values in length is even
        it will add the two middle values and divide by two, otherwise just divide the middle"""
        middle_ind = length // 2
        median = sorted_vals[middle_ind - 1] + sorted_vals[middle_ind] / 2

    else:
        middle_ind = length // 2
        median = sorted_vals[middle_ind]

    return median #returns the median when the function is called


#list_nums_even = [13, 7, -3, 82, 4, 234, 32, 234]
#list_nums_odd = [13, 7, -3, 82, 4, 234, 32]
#results = find_median(list_nums_even)
#print(results)
