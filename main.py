import time
import closest_pair as cp


arr_points = cp.generate_random_points(1000, 3, threshold=1000)

bf_start_time = time.time()
bf_min_dist, bf_closest_pair = cp.bf_closest_pair(arr_points, 3)
bf_finish_time = time.time()

print("Brute Force: ")
print("Min distance:", bf_min_dist)
print("Closest pair:", bf_closest_pair)
print("Execution time:", bf_finish_time - bf_start_time)

dnc_start_time = time.time()
cp.quick_sort_by_x(arr_points, 0, len(arr_points) - 1)
dnc_min_dist, dnc_closest_pair = cp.dnc_closest_pair(arr_points, 3)
dnc_finish_time = time.time()

print("Divide and Conquer: ")
print("Min distance:", dnc_min_dist)
print("Closest pair: ", dnc_closest_pair)
print("Execution time:", dnc_finish_time - dnc_start_time)

#cp.plot_results(arr_points, dnc_closest_pair)