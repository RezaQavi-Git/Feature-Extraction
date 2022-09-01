
def difference_from_value(column, value):
    diff = [0] * len(column)
    for i in range(len(column)):
        diff[i] = column[i] - value
    
    return diff