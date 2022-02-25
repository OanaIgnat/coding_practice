import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')


def euclidean_distance(point1, point2):
    return math.sqrt(sum((point1 - point2) ** 2))


def kmeans(data_points, nb_iterations, k):
    # assign random centroids
    centroids = np.zeros((k, data_points.shape[1]))  # (#points, #coordinates)

    for _ in range(nb_iterations):
        dict_centroid_points = {}

        # assign each point to it's nearest centroid
        for point in data_points:
            min_distance = 1000
            c_min = -1
            for index, centroid in enumerate(centroids):
                dist = euclidean_distance(centroid, point)
                if dist <= min_distance:
                    min_distance = dist
                    c_min = index
            if c_min not in dict_centroid_points.keys():
                dict_centroid_points[c_min] = []
            dict_centroid_points[c_min].append(point)


        # recompute the centroids
        for c in dict_centroid_points.keys():
            new_centroid = np.mean(dict_centroid_points[c], axis=0)  # mean over the coordinates
            centroids[c] = new_centroid

        # update again the points after centroids are updated
        for p in data_points:
            min_distance = 1000
            c_min = -1
            for index_c, c in enumerate(centroids):
                dist = euclidean_distance(c, p)
                if dist <= min_distance:
                    min_distance = dist
                    c_min = index_c
            if c_min not in dict_centroid_points.keys():
                dict_centroid_points[c_min] = []
            dict_centroid_points[c_min].append(p)

    return dict_centroid_points, centroids


if __name__ == "__main__":
    k = 2
    nb_iterations = 300
    points = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
    print(points.shape)

    dict_centroid_points, centroids = kmeans(points, nb_iterations, k)
    print(centroids)
    print(dict_centroid_points)
