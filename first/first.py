# Question A 
 
'''Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. 

As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).'''

# Define the function is_overlapping that takes two lines as input.
def is_overlapping(line1, line2):
    '''
    Returns whether the two given lines overlap. 
    '''

    # Separate the endpoints of line1 and ensure x1 is the smaller number.
    x1, x2 = sorted(line1)  

    # Separate the endpoints of line2 and ensure x3 is the smaller number.
    x3, x4 = sorted(line2)  

    # Check if the lines overlap by checking if one of the end points of one line is in the other line.
    return (x1 <= x3 <= x2) or (x1 <= x4 <= x2) or (x3 <= x1 <= x4) or (x3 <= x2 <= x4)
