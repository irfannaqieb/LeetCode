# Two Sum problem from LeetCode


def twoSum(array, target):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                return [i, j]


# function run in O(n^2)

# print(twoSum([3, 2, 4], 6)) ---> Output: [1, 2]
# print(twoSum([3, 3], 6)) ---> Output: [0, 1]
# print(twoSum([2, 7, 11, 15], 9)) ---> Output: [0, 1]
