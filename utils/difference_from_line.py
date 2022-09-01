
def difference_from_line(column, line):
    diff = [0] * len(column)
    for i in range(len(column)):
        diff[i] = (column[i] - line[i]) / 100
    
    return diff