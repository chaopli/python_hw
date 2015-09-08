__author__ = 'weina_guo'

import matplotlib.pyplot as plt
threshold = 5.5e9
# The problem requires 5.5e9, which does not work with the data in PDF.
# I used 4.0e9 instead. Uncomment the following line if properly data is used.
# threshold = 5.5e9


# This function reads the contents of file input and prints the contents to the output
def read_file(input):
    try:
        file = open(input, 'r')
        lines = file.readlines()
        print('Lines in the file are:\n')
        for i in range(len(lines)):
            print(lines[i])
        file.close()
        print('Operations finishes successfully!')
        return lines
    except IOError:
        print('Filename is not existing')
        quit()


def __main__():
    data = read_file('dow_input.txt')
    collect = []
    count = 0
    adj_close, high_vol = [], []
    for i in range(len(data)):
        record = data[i].split(',')
        adj_close.append(float(record[5]))
        if int(record[4]) > threshold:
            print('{0:d}th record has the volume greater than {1:d}.'.format(i, int(threshold)))
            collect.append(i)
            high_vol.append(float(record[5]))
            count += 1

    print('There totally {0:d} records whose volume greater than {1:d}.'.format(count, int(threshold)))
    res = open('dow_volume_stats.txt', 'w')
    res.write('The dow volume has been above {0:d} on {1:d} days this year.\n'.format(int(threshold), count))
    if count != 0:
        res.write('The high_vol_index '+str(collect)+'.')
    res.close()
    plt.plot(adj_close)
    plt.plot(collect, high_vol, 'ro')
    plt.ylabel('adj_close')
    plt.xlabel('days')
    plt.show()

__main__()
