import math
import numpy as np
import matplotlib.pyplot as plt



def generate_random_points(N, dimensions, threshold=1000):
    """
    Mengembalikan numpy.NDArray berisi N buah titik acak dengan dimensi sebesar dimensions.
    Seluruh titik akan berada pada range
    -1 * threshold <= x < threshold,
    -1 * threshold <= y < threshold,
    -1 * threshold <= z < threshold, 
    dst.
    """
    arr_points = np.empty(N, dtype=object)
    
    for i in range(N):
        arr_points[i] = []

        for _ in range(dimensions):
            value = round(np.random.uniform(-1 * threshold, threshold), 2)
            arr_points[i].append(value) 

        arr_points[i] = tuple(arr_points[i])

    return arr_points



def euclidean_dist(point_a, point_b, dimensions): 
    """
    Mengembalikan jarak euclidean antara titik a dan titik b dengan dimensi sebesar dimensions
    """
    result = 0
    for i in range(dimensions):
        result += (point_a[i] - point_b[i])**2

    result = math.sqrt(result)
    return result



def bf_closest_pair(arr_points, dimensions): 
    """
    Mengembalikan jarak terpendek, pasangan titik terdekat, serta banyaknya operasi 
    perhitungan jarak euclidean yang dilakukan dengan algoritma brute force
    Prekondisi: 
    len(arr_points) >= 2 dan dimensions >=1
    """
    closest_pair = None
    min_dist = float('inf')
    operations = 0

    for i in range(0, len(arr_points)):
        for j in range(i+1, len(arr_points)):
            current_dist = euclidean_dist(arr_points[i], arr_points[j], dimensions) 
            operations += 1
            if (current_dist < min_dist):
                min_dist = current_dist
                closest_pair = (arr_points[i], arr_points[j])

    return min_dist, closest_pair, operations



def dnc_closest_pair(arr_points, dimensions):
    """
    Mengembalikan jarak terpendek, pasangan titik terdekat, serta banyaknya operasi 
    perhitungan jarak euclidean yang dilakukan dengan algoritma divide and conquer.
    Prekondisi: 
    len(arr_points) >= 2, dimensions >=1, dan arr_points
    sudah terurut berdasarkan absis 
    """
    num_points = len(arr_points)

    if (num_points <= 3):
        return bf_closest_pair(arr_points, dimensions)

    # Pengambilan titik tengah yang dapat membagi array menjadi partisi kiri dan kanan sama rata
    # dengan elemen tengah array sebagai acuan.
    mid = num_points // 2
    mid_x = arr_points[mid][0]
    left_arr_points = arr_points[:mid]
    right_arr_points = arr_points[mid:]

    # Pencarian pasangan terdekat pada partisi kiri dan kanan secara rekursif
    left_min_dist, left_closest_pair, left_operations = dnc_closest_pair(left_arr_points, dimensions)
    right_min_dist, right_closest_pair, right_operations = dnc_closest_pair(right_arr_points, dimensions)

    # Jarak terpendek sementara adalah min(left_min_dist, right_min_dist)
    if (left_min_dist <= right_min_dist):
        closest_pair = left_closest_pair
        min_dist = left_min_dist
    else:
        closest_pair = right_closest_pair
        min_dist = right_min_dist

    # Titik-titik yang jarak absisnya dengan mid_x <= min_dist akan dimasukkan ke dalam slab
    slab = []
    slab_width = min_dist
    slab_operations = 0

    for point in arr_points:
        if (abs(point[0] - mid_x) <= slab_width):
            slab.append(point)

    # Pencarian pasangan terdekat untuk titik-titik yang berada dalam slab
    for i in range(0, len(slab)):
        for j in range(i + 1, len(slab)):
            # Jika terdapat sepasang titik di dalam slab yang tidak memenuhi kriteria close_enough 
            # (lihat fungsi di bawah) maka tidak perlu dilakukan perhitungan 
            # jarak euclidean, karena sudah pasti jaraknya > min_dist
            if (close_enough(slab[i], slab[j], slab_width, dimensions)):
                current_dist = euclidean_dist(slab[i], slab[j], dimensions)
                slab_operations += 1
                if (current_dist < min_dist):
                    min_dist = current_dist
                    closest_pair = (slab[i], slab[j])
        
    total_operations = left_operations + right_operations + slab_operations
    return min_dist, closest_pair, total_operations



def close_enough(point_a, point_b, dist_limit, dimensions):
    """
    Menentukan apakah titik a (x1, y1, z1) dan titik b (x2, y2, z2) 
    cukup dekat dengan kriteria berikut:
    |x1 - x2| < dist_limit,
    |y1 - y2| < dist_limit,
    |z1 - z2| < dist_limit,
    dst.
    Digunakan untuk mengurangi jumlah perhitungan pada algoritma divide and conquer
    """
    for i in range(1, dimensions):
        if (abs(point_a[i] - point_b[i]) > dist_limit):
            return False
    
    return True



def plot_results(arr_points, closest_pair):
    """
    Melakukan plotting terhadap titik-titik yang ada pada arr_points. pasangan titik 
    yang merupakan pasangan terdekat diberi warna merah, sedangkan yang lainnya
    diberi warna hijau

    """
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
    """
    Melakukan sorting pada arr_points dengan algoritma quick sort
    """
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











        