
# calculate the entropy for a dataset
from math import log2

def calculate_entropy():
    # proportion of examples in each class
    class0 = 10/100
    class1 = 90/100
    # calculate entropy
    entropy = -(class0 * log2(class0) + class1 * log2(class1))
    # print the result
    print('entropy skewed distribution: %.3f bits' % entropy)
    print('entropy skewed distribution -> no surprise -> entropy low')

    # proportion of examples in each class
    class0 = 50/100
    class1 = 50/100
    # calculate entropy
    entropy = -(class0 * log2(class0) + class1 * log2(class1))
    print('entropy balanced distribution: %.3f bits' % entropy)
    print('entropy balanced distribution -> high surprise -> entropy high')



if __name__ == "__main__":
    calculate_entropy()