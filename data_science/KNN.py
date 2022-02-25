import math
from collections import Counter
'''
Given a query point X, calculate all distances (Euclidian) from X to all points and
select the top K nearest points to X. 
If regression, return mean of the labels of those K points.
If classification, return mean of the labels of those K points
'''

def mean(labels):
    return sum(labels) / len(labels)

# the value that appears most often
def mode(labels):
    return Counter(labels).most_common(1)[0][0] # if 2 or more values appear, get the first


def euclidean_distance(point1, point2):
    sum = 0
    for i in range(len(point1)):
        sum += (point1[i] - point2[i]) ** 2
    return math.sqrt(sum)


def knn(data, query, k, distance_fn, choice_fn):
    neighbor_distances_and_indices = []

    for index, example in enumerate(data):
        # calculate the distance between the query example and the current example from the data
        distance = distance_fn(example[:-1], query)

        # add the distance and the index of the example to an ordered collection
        neighbor_distances_and_indices.append((distance, index))

    # sort the  distances and indices from in ascending order by the distances
    # neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)
    neighbor_distances_and_indices.sort(key=lambda x: x[0])

    # pick the first K entries from the sorted collection
    k_nearest_distances_and_indices = neighbor_distances_and_indices[:k]

    # get the labels of the selected K entries
    k_nearest_labels = [data[idx][1] for distance, idx in k_nearest_distances_and_indices]

    # if regression (choice_fn = mean), return the average of the K labels
    # if classification (choice_fn = mode), return the mode of the K labels
    return choice_fn(k_nearest_labels)


def main():
    '''
    # Regression Data
    #
    # Column 0: height (inches)
    # Column 1: weight (pounds)
    '''
    reg_data = [
        [65.75, 112.99],
        [71.52, 136.49],
        [69.40, 153.03],
        [68.22, 142.34],
        [67.79, 144.30],
        [68.70, 123.30],
        [69.80, 141.49],
        [70.01, 136.46],
        [67.90, 112.37],
        [66.49, 127.45],
    ]

    # Question:
    # Given the data we have, what's the best-guess at someone's weight if they are 60 inches tall?
    reg_query = [60]
    reg_prediction = knn(
        reg_data, reg_query, k=3, distance_fn=euclidean_distance, choice_fn=mean)
    print("If they are 60 inches tall, their weight is probably " + str(reg_prediction))

    '''   
    # Classification Data
    # 
    # Column 0: age
    # Column 1: likes pineapple
    '''
    clf_data = [
        [22, 1],
        [23, 1],
        [21, 1],
        [18, 1],
        [19, 1],
        [25, 0],
        [27, 0],
        [29, 0],
        [31, 0],
        [45, 0],
    ]
    # Question:
    # Given the data we have, does a 33 year old like pineapples on their pizza?
    clf_query = [33]
    clf_prediction = knn(
        clf_data, clf_query, k=3, distance_fn=euclidean_distance, choice_fn=mode
    )

    if clf_prediction == 0:
        print("No, a 33 year old does not like pineapples on their pizza")
    else:
        print("Yes, a 33 year old likes pineapples on their pizza")


if __name__ == '__main__':
    main()
