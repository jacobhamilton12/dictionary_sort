from dictionary_sort import __version__, numsort
import random
import time
import heapq


def test_version():
    assert __version__ == '0.1.0'
    
def test_simple_pop_push():
    ns = numsort.NumberSort()
    ns.push(3)
    ns.push(5)
    length = len(ns.grid[0])
    num = ns.pop()
    assert num == 3
    assert len(ns.grid[0]) == length - 1
    
def test_medium_pop_push():
    ns = numsort.NumberSort()
    random.seed(10)
    nums = [random.randint(0, 9999) for _ in range(10)]
    print(nums)
    for num in nums:
        ns.push(num)
    print(ns.grid)
    nums.sort(reverse=True)
    while num := ns.pop():
        print(f"popped: {num}")
        assert num == nums.pop()
        
def test_large_pop_push():
    ns = numsort.NumberSort()
    #TODO test duplicates after fix for it
    nums = list({random.randint(0, 2**32) for _ in range(100000)})
    for num in nums:
        ns.push(num)
    nums.sort(reverse=True)
    while num := ns.pop():
        assert num == nums.pop()
        
def test_performance_vs_heap():
    ns = numsort.NumberSort()
    #TODO test duplicates after fix for it
    nums = list({random.randint(0, 2**32) for _ in range(10000000)})
    nums2 = list(nums)
        
    #test heap
    start = time.time()
    heapq.heapify(nums2)
    while nums2:
        heapq.heappop(nums2)
    print(f"heap: {time.time() - start}")
    
    #test dict sort / fenwick
    nums.sort(reverse=True)
    start = time.time()
    for num in nums:
        ns.push(num)
    while num := ns.pop():
        assert num == nums.pop()
    print(f"ours: {time.time() - start}")