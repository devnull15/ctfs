import numpy as np
import sys


###VARS###
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789_{}"

ciphertext = "7Nv7}dI9hD9qGmP}CR_5wJDdkj4CKxd45rko1cj51DpHPnNDb__EXDotSRCP8ZCQ"

mod = len(alphabet)

ciphertext_nums = []

plaintext_nums = []

inv_matrix = [[31, 44, 13, 33, 47, 24, 12, 21],
              [37, 22, 19, 37, 40, 1, 59, 55],
              [45, 59, 63, 4, 27, 63, 20, 50],
              [44, 10, 0, 9, 11, 1, 14, 16],
              [54, 47, 14, 7, 31, 25, 48, 48],
              [39, 2, 56, 48, 38, 27, 48, 34],
              [38, 1, 12, 40, 40, 13, 34, 5],
              [27, 22, 5, 21, 22, 20, 7, 59]]

msize = len(inv_matrix)
###/VARS###

###MAIN###

## 1) ciphertext to matrix
for j in xrange(0,msize):
    temparray = []
    for i in xrange(0,msize):
        temparray.append(alphabet.find(ciphertext[i+(j*msize)]))
    ciphertext_nums.append(temparray)
#print ciphertext_nums #DEBUG

## 2) Multiply matrices to and store in plaintext_nums
for i in xrange(0,msize):
    plaintext_nums += np.remainder(np.dot(inv_matrix, ciphertext_nums[i]), mod).tolist()

print plaintext_nums

## 3) Convert plaintext_nums to characters

for x in plaintext_nums:
    sys.stdout.write(alphabet[x])
    

###/MAIN###
