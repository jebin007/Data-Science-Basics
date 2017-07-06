import numpy
 
FIELDNAMES = ['', 'id', 'priceLabel', 'name', 'brandId', 'brandName', 'imageLink', 'desc', 'vendor', 'patterned', 'material']
DATATYPES = [('myint', 'a'), ('myid', 'i'), ('price', 'f8'), ('name', 'a200'), ('brandId', '<i8'), ('brandName', 'a200'), ('imageUrl', '|S500'), ('description', '|900'), ('vendor', '|S100'), ('pattern', '|S50'), ('material', '|S500')]

def load_data(filename):
  my_csv = numpy.genfromtxt(filename, delimiter='\t', skip_header=1, names=FIELDNAMES, invalid_raise=False, dtype=DATATYPES)
  return my_csv

sample_file = 'data.csv'
my_csv = load_data(sample_file)
print(my_csv[0])