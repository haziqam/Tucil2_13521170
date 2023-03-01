import time
import closest_pair as cp


print("====================== INPUTS =======================")
while (True):
    num_points = int(input("Number of points: "))
    if (num_points >=2):
        break
    print("Number of points must be greater than or equal to 2")

while (True):
    dim = int(input("Dimensions: "))
    if (dim >= 1):
        break
    print("Dimensions must be greater than or equal to 1")


print("=====================================================")
print("\n")

arr_points = cp.generate_random_points(num_points, dim, threshold=1000)

bf_start_time = time.time()
bf_min_dist, bf_closest_pair, bf_operations = cp.bf_closest_pair(arr_points, dim)
bf_finish_time = time.time()

print("==================== BRUTE FORCE ====================")
print("Min distance:", bf_min_dist)
print("Closest pair:", bf_closest_pair)
print("Execution time:", bf_finish_time - bf_start_time)
print("Total operations:", bf_operations)
print("=====================================================")

print("\n")
         
dnc_start_time = time.time()
cp.quick_sort_by_x(arr_points, 0, len(arr_points) - 1)
dnc_min_dist, dnc_closest_pair, dnc_operations = cp.dnc_closest_pair(arr_points, dim)
dnc_finish_time = time.time()

print("================ DIVIDE AND CONQUER =================")
print("Min distance:", dnc_min_dist)
print("Closest pair: ", dnc_closest_pair)
print("Execution time:", dnc_finish_time - dnc_start_time)
print("Total operations:", dnc_operations)
print("=====================================================")

if (dim == 3):
    ans = input("Plot results? (y/n): ")
    if (ans == "y"):
        cp.plot_results(arr_points, dnc_closest_pair)