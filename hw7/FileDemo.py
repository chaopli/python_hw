__author__ = 'Noha'

import matplotlib.pyplot as plt


# This function counts the total number of line in the input filename
def file_operations_test(filename, mode):   # default mode is 'r'
    try:
        handle = open(filename, mode)
        # print(handle)
        count = 0
        for line in handle:
            count += 1
        print('Line Count:', count)
    except IOError:
        print('Filename is not existing')
        quit()
# file_operations_test('mbox-short.txt', 'r')
# file_operations_test('noha.txt', 'r')


# This function reads the contents of file input and prints the contents to the output
def file_ex2_test2(in_filename):
    try:
        handle = open(in_filename, 'r')
        for line in handle.readline():
            print('Line Data:', line)
        handle.close()
        print('Operations finishes successfully!')
    except IOError:
        print('Filename is not existing')
        quit()


# This function reads the contents of file input and write the contents to file output
def file_ex2_test(in_filename, out_filename):
    try:
        handle = open(in_filename, 'r')
        handle_out = open(out_filename, 'w')
        for line in handle:
            print('Line Data:', line)
            handle_out.write('Line Data: '.lower() + line.upper())
        handle.close()
        handle_out.close()
        print('Operations finishes successfully!')
    except IOError:
        print('Filename is not existing')
        quit()
file_ex2_test('input.txt', 'output.txt')
# file_Ex2_test('input.txt', 'output_new.txt')


# This function prints only the first line of file input1.txt  and close the file
def file_ex3_test(in_filename):
    try:
        count = 0
        handle = open(in_filename, 'r')
        for line in handle:
           print('Line Data:', line)
           handle.close()
           break
    except IOError:
        print('Filename is not existing')
        quit()


def file_ex4_test(zoo):
    f = open("haixia.txt", "w")
    for i in zoo:
        # add the whole zoo to the output.txt
        print('The current element is:', i)
        f.write(i+'\n')
    f.close()   # close the file
zoo = ['lion', "elephant", 'monkey']


# file_Ex4_test(zoo)
def file_ex5_test():
    f = open("mbox-short.txt")
    for line in f:
        print(line.strip().upper())
        # print('The current element is:', line.strip().upper())
    f.close()   # close the file
# file_Ex5_test()


# This function prompts for a file name, read through the file, and look for lines of the form: X-DSPAM
# -Confidence: 0.8475
# When you encounter a line that starts with X-DSPAM-Confidence:
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.
# Test your file on the mbox.txt and mbox-short.txt files.
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
def file_ex6_test():    # filename_input = 'mbox-short.txt'):
    import statistics
    list_floats = []
    filename_input = input("Enter the file name:")
    f = open(filename_input, "r")
    for line in f:
        if line.startswith('X-DSPAM-Confidence:'):
            cur_elements_list = line.split()
            print('current elements are:', cur_elements_list)
            list_floats.append(float(cur_elements_list[1]))
    print('Total number of lines parsed are:', len(list_floats))
    print('Average spam confidence are:', round(statistics.mean(list_floats),4))
    f.close()   # close the file


file_ex6_test()
