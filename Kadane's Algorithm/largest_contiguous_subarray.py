def findLargestSubarray(a):
    max_so_far = 0
    max_ending_here = 0
    for i in a:
        max_ending_here += i
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far

def main():
    a = [-1,-2]
    result = findLargestSubarray(a)
    print(result)

if __name__ == '__main__':
    main()
