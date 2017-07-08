from s2v4 import *

#funciton to find the maximum value from the data
def find_max(data_sample, col):
    temp_list = []
    for row in data_sample:
        price = float(row[col])
        temp_list.append(price)
    return max(temp_list)

#function to find the minimum value from the data
def find_min(data_sample, col):
    temp_list = []
    for row in data_sample:
        price = float(row[col])
        temp_list.append(price)
    return min(temp_list)

#combining max and min to one function since it iterates through the same range to be more efficient
def find_max_min(data_sample, col, m='max'):    #m='max' is setting deafault value of the attribute to be max
    temp_list = []
    val = 0
    for row in data_sample:
        price = float(row[col])
        temp_list.append(price)
    if m == "max":
        val = max(temp_list)
    elif m == "min":
        val =  min(temp_list)
    else: #hopefully we don't come to this
        pass
    return val

#print(find_max_min(data_from_csv[1:], 2, 'max'))
#print(find_max_min(data_from_csv[1:], 2, 'min'))

#numpy max and min
price = my_csv['priceLabel']
price_in_float = [float(x) for x in price]
numpy_max = numpy.amax(price_in_float)
numpy_min = numpy.amin(price_in_float)
#print("min =", numpy_min , "max =", numpy_max)




#print(find_max(data_from_csv[1:], 2)) #2nd row = price
#print(find_min(data_from_csv[1:], 2)) #2nd row = price
