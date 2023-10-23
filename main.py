import random, time
import tabulate
import sys
sys.setrecursionlimit(6000)


def ssort(a):
    for i in range(len(a)):
        m = a.index(min(a[i:]))
        a[i], a[m] = a[m], a[i]
    return a

def qsort(a, pivot_fn):
    ## TO DO
    if len(a) <= 1:
        return a
    else:
        p = pivot_fn(a)
        a1 = list(filter(lambda x: x < p, a))
        a2 = list(filter(lambda x: x==p, a))
        a3 = list(filter(lambda x: x > p, a))

        s1, s3 = qsort(a1,pivot_fn), qsort(a3, pivot_fn)

        return s1 + a2 + s3

def time_search(sort_fn, mylist):
    """
    Return the number of milliseconds to run this
    sort function on this list.

    Note 1: `sort_fn` parameter is a function.
    Note 2: time.time() returns the current time in seconds. 
    You'll have to multiple by 1000 to get milliseconds.

    Params:
      sort_fn.....the search function
      mylist......the list to search
      key.........the search key 

    Returns:
      the number of milliseconds it takes to run this
      search function on this input.
    """
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000
    ### 

def selectfirst(a):
    return a[0]

def selectrandom(a):
    return random.choice(a)

def compare_sort(sizes=[5, 10, 100, 200, 500, 1000, 2000, 3000, 4000, 5000]):
    """
    Compare the running time of different sorting algorithms.

    Returns:
      A list of tuples of the form
      (n, linear_search_time, binary_search_time)
      indicating the number of milliseconds it takes
      for each method to run on each value of n
    """
    ### TODO - sorting algorithms for comparison 
    qsort_fixed_pivot =  lambda a: qsort(a, selectfirst)
    qsort_random_pivot = lambda a: qsort(a, selectrandom)
    sel_sort = lambda a: ssort(a)
    tim_sort = sorted
    result = []
    for size in sizes:
        # create list in ascending order 
        mylist = list(range(size))
        # shuffles list if needed
        #random.shuffle(mylist)
        result.append([
            len(mylist),
           #time_search(qsort_fixed_pivot, mylist),
            time_search(qsort_random_pivot, mylist),
            #time_search(sel_sort,mylist),
            time_search(tim_sort,mylist)
        ])
    return result
    

def print_results(results):
    """ change as needed for comparisons """
    print(tabulate.tabulate(results,
                            headers=['n', 'qsort-random-pivot', 'tim_sort'],
                            floatfmt=".3f",
                            tablefmt="github"))

def test_print():
    print_results(compare_sort())

random.seed()
test_print()
