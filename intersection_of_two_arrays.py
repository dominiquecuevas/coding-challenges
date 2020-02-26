def intersection_of_two_arrays(nums1, nums2):
    largest = nums1 if len(nums1) >= len(nums2) else nums2
    smallest = nums1 if largest is nums2 else nums2

    intersection = []

    for i in range(len(smallest)):
        for j in range(len(largest)):
            if smallest[i] is not None and largest[j] is not None and smallest[i] == largest[j]:
                intersection.append(smallest[i])
                smallest[i] = None
                largest[j] = None

    return intersection

print(intersection_of_two_arrays([1,2,2,1], [2,2]))
print(intersection_of_two_arrays([4,9,5], [9,4,9,8,4]))
print(intersection_of_two_arrays([1,2], [1,1]))