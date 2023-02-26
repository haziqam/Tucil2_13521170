import math
import numpy as np
import matplotlib.pyplot as plt



def generate_random_points(N, dimensions, threshold=1000):
    arr_points = np.empty(N, dtype=object)
    
    for i in range(N):
        arr_points[i] = []

        for _ in range(dimensions):
            value = round(np.random.uniform(-1 * threshold, threshold), 2)
            arr_points[i].append(value) 

        arr_points[i] = tuple(arr_points[i])

    return arr_points



def euclidean_dist(point_a, point_b, dimensions): 
    result = 0
    for i in range(dimensions):
        result += (point_a[i] - point_b[i])**2

    result = math.sqrt(result)
    return result



def bf_closest_pair(arr_points, dimensions): 
    closest_pair = None
    min_dist = float('inf')

    for i in range(0, len(arr_points)):
        for j in range(i+1, len(arr_points)):
            current_dist = euclidean_dist(arr_points[i], arr_points[j], dimensions) 
            if (current_dist < min_dist):
                min_dist = current_dist
                closest_pair = (arr_points[i], arr_points[j])

    return min_dist, closest_pair



def dnc_closest_pair(arr_points, dimensions):
    num_points = len(arr_points)

    if (num_points <= 3):
        return bf_closest_pair(arr_points, dimensions)

    mid = num_points // 2
    mid_x = arr_points[mid][0]
    left_arr_points = arr_points[:mid]
    right_arr_points = arr_points[mid:]

    left_min_dist, left_closest_pair = dnc_closest_pair(left_arr_points, dimensions)
    right_min_dist, right_closest_pair = dnc_closest_pair(right_arr_points, dimensions)

    if (left_min_dist <= right_min_dist):
        closest_pair = left_closest_pair
        min_dist = left_min_dist
    else:
        closest_pair = right_closest_pair
        min_dist = right_min_dist

    slab = []
    slab_width = min_dist

    for point in arr_points:
        if (abs(point[0] - mid_x) <= slab_width):
            slab.append(point)

    for i in range(0, len(slab)):
        for j in range(i + 1, len(slab)):
            if (close_enough(slab[i], slab[j], slab_width, dimensions)):
                current_dist = euclidean_dist(slab[i], slab[j], dimensions)
                if (current_dist < min_dist):
                    min_dist = current_dist
                    closest_pair = (slab[i], slab[j])
        
    return min_dist, closest_pair



def close_enough(point_a, point_b, dist_limit, dimensions):
    for i in range(1, dimensions):
        if (abs(point_a[i] - point_b[i]) > dist_limit):
            return False
    
    return True



def plot_results(arr_points, closest_pair):
    fig = plt.figure(figsize = (16, 9))
    ax = plt.axes(projection ="3d")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    for point in arr_points:
        if point in closest_pair: 
            ax.scatter3D(point[0], point[1], point[2], color = "red")
        else:
            ax.scatter3D(point[0], point[1], point[2], color = "green")
    
    plt.show()



def quick_sort_by_x(arr_points, left, right):
    if (left < right):
        pivot = arr_points[right][0]
        i = left - 1
        for j in range(left, right):
            if (arr_points[j][0] <= pivot):
                i += 1
                arr_points[i], arr_points[j] = arr_points[j], arr_points[i]

        pivotIdx = i + 1
        arr_points[pivotIdx], arr_points[right] = arr_points[right], arr_points[pivotIdx]
        quick_sort_by_x(arr_points, left, pivotIdx-1)
        quick_sort_by_x(arr_points, pivotIdx + 1, right)











        