 import math


def distance(p1, p2):
    """
    :return: distance between two points
    """
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


def greedyTSP(G, start):
    """
    :param G: list of tuples with x and y coordinates of a city in the tuple
    :param start: The city/point from which the journey will start
    :return: The path taken and the distance covered.
    """
    memory = 0

    n = len(G)
    memory += 1

    visited = [0 for e in G]  # keeping in record the cities visited
    memory += len(G)

    path = []

    total_dist = 0
    current = start

    memory += 2

    for i in range(n):
        min_dist = float("inf")
        min_k = -1
        dist_ = 0
        # Above lines take 3 units of memory

        for k in range(n):
            if visited[k] == 0:
                dist_ = distance(current, G[k])  # calculating the distance between current point and kth point

                if dist_ < min_dist:
                    min_dist = dist_  # if the distance is less than the minimum distance we will go to that city
                    min_k = k
        visited[min_k] = 1
        current = G[min_k]
        path.append(G[min_k])
        total_dist += dist_

    memory += 3
    memory += len(path)

    return path, total_dist, memory



