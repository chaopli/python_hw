import matplotlib.pyplot as plt
import numpy as np
threshold = 5.5e9
# The problem requires 5.5e9, which does not work with the data in PDF.
# I used 4.0e9 instead. Uncomment the following line if properly data is used.
# threshold = 5.5e9


# This function reads the contents of file input and prints the contents to the output
def read_file(input):
    try:
        file = open(input, 'r')
        lines = file.readlines()
        print('Load file successfully!')
        return lines
    except IOError:
        print('File is not existing')
        quit()


def __main__():
    data = read_file('dow_input.txt')
    data_array = []
    nrow = len(data)
    for record in data:
        data_array.append(np.fromstring(record, sep=','))
    ncol = len(data_array[0])
    data_array = np.array(data_array)
    print(data_array)
    mask = [[1 if data_array[i, j] > threshold else 0 for j in range(ncol)] for i in range(nrow)]
    mask = np.array(mask)
    nrows_greater = mask.sum()
    print(nrows_greater)
    rows = np.where(data_array[:, 4] > threshold)
    print('The mask indicates the rows which have volumes greater than {0:e} is:\n'.format(threshold))
    print(mask)
    print('Number of rows with volume greater than {0:e} is {1:d}\n'.format(threshold, nrows_greater))
    print('Rows have a volume greater than {0:e} are:\n'.format(threshold))
    print(rows)
    print('And the subarray is:\n')
    print(data_array[rows])
    plt.plot(data_array[:, 5])
    plt.plot(rows, data_array[rows, 5], 'ro')
    plt.ylabel('adj_close')
    plt.xlabel('days')
    plt.show()

__main__()
