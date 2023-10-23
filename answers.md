# CMPS 2200 Reciation 5
## Answers

**Name:** Collette Riviere

Place all written answers from `recitation-05.md` here for easier grading.

- **1b.**

# qsort-fixed-pivot: worst: O(n^2), average: O(n log(n))
# qsort-random-pivot: worst: O(n^2), average: O(n log(n))
# sel_sort: worst: O(n^2), average: O(n^2)

**Run times for random permutations of specified sizes (n).**
|    n |   qsort-fixed-pivot |   qsort-random-pivot |   sel_sort |
|------|---------------------|----------------------|------------|
|    5 |               0.012 |                0.009 |      0.005 |
|   10 |               0.018 |                0.021 |      0.006 |
|  100 |               0.210 |                0.227 |      0.172 |
|  200 |               0.450 |                0.532 |      0.611 |
|  500 |               1.148 |                1.381 |      3.508 |
| 1000 |               2.627 |                2.974 |     13.578 |
| 2000 |               5.584 |                6.286 |     53.141 |
| 3000 |               9.203 |                9.826 |    123.165 |
| 4000 |              12.030 |               13.465 |    223.800 |
| 5000 |              16.051 |               16.775 |    355.771 |


**Run times for already sorted permutations of specified sizes (n).**
|    n |   qsort-fixed-pivot |   qsort-random-pivot |   sel_sort |
|------|---------------------|----------------------|------------|
|    5 |               0.014 |                0.013 |      0.005 |
|   10 |               0.023 |                0.017 |      0.005 |
|  100 |               1.519 |                0.228 |      0.142 |
|  200 |               3.730 |                0.463 |      0.503 |
|  500 |              21.454 |                1.391 |      2.895 |
| 1000 |              83.835 |                2.907 |     11.088 |
| 2000 |             331.294 |                6.104 |     43.951 |
| 3000 |             758.727 |                9.968 |    100.202 |
| 4000 |            1356.000 |               12.926 |    181.654 |
| 5000 |            2104.633 |               16.292 |    284.262 |


**Here, quicksort with a fixed pivot is best. For unorganized lists, the run times are similar to the asymptotic bounds (seen above) as both quicksort have similar run times but selection sort has a much worse runtime. This makes sense looking at the average asymptotic bounds. But for already sorted permutations, quicksort with a fixed pivot performs much worst than the random pivot. This is because the pivot being the first element, which is the smallest element in the already sorted list, this is the worst case senario for quicksort to the asymptotic runtime is then O(n^2) while the random pivot stays the same and performs the best. Also, nothing should happen when quicksort is performed on a list of a differnt type because there will still be an order. For example, a list of characters (like the alphabet) can still be sorted like integers.**



- **1c.**

# qsort-random-pivot: O(n^2)
# tim_sort: O(n log n)

**Run times for random permutations of specified sizes (n).**
|    n |   qsort-random-pivot |   tim_sort |
|------|----------------------|------------|
|    5 |                0.014 |      0.000 |
|   10 |                0.018 |      0.001 |
|  100 |                0.253 |      0.008 |
|  200 |                0.474 |      0.016 |
|  500 |                1.395 |      0.046 |
| 1000 |                2.858 |      0.099 |
| 2000 |                6.261 |      0.214 |
| 3000 |                9.728 |      0.341 |
| 4000 |               13.715 |      0.478 |
| 5000 |               18.087 |      0.603 |

**Run times for already sorted permutations of specified sizes (n).**
|    n |   qsort-random-pivot |   tim_sort |
|------|----------------------|------------|
|    5 |                0.019 |      0.001 |
|   10 |                0.018 |      0.000 |
|  100 |                0.240 |      0.001 |
|  200 |                0.484 |      0.002 |
|  500 |                1.369 |      0.004 |
| 1000 |                2.965 |      0.007 |
| 2000 |                7.201 |      0.014 |
| 3000 |               11.236 |      0.023 |
| 4000 |               16.829 |      0.031 |
| 5000 |               20.091 |      0.042 |


**tim_sort is by far the best and takes the least amount of time. The runtime follows the asympotic bounds because quicksort is O(n^2) which is much slower than O(n log n) for tim_sort. It also should not matter what type the input list is for either of these methods.**
