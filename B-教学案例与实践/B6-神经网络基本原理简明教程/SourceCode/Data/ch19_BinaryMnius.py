# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import numpy as np

train_data_name = "../../data/ch19.train_minus.npz"
test_data_name = "../../data/ch19.test_minus.npz"

def create_data():
    count = 1
    a = []
    b = []
    c = []
    for i in range(0,16):
        for j in range(0,i+1):
            print(count,i,j)
            count+=1
            k = i - j
            a.append(i)
            b.append(j)
            c.append(k)
    return a,b,c

if __name__=='__main__':
    a,b,c = create_data()
    count = len(a)
    binary8 = np.unpackbits(np.array([range(16)],dtype=np.uint8).T,axis=1)
    bin4 = binary8[:,4:8]
    print(bin4)
    X = np.zeros((count,4,2))
    Y = np.zeros((count,4))
    for i in range(count):
        bin_a = bin4[a[i]]
        bin_b = bin4[b[i]]
        bin_c = bin4[c[i]]
        for j in range(4):
            X[i,j] = [bin_a[j],bin_b[j]]
            Y[i,j] = bin_c[j]

    np.savez(train_data_name, data=X, label=Y)
    np.savez(test_data_name, data=X, label=Y)

    print("done")

