class Solution:
    def groupThePeople(self, groupSizes):
        sizes = {}
        for idx, size in enumerate(groupSizes):
            sizes[size] = sizes.get(size, [])
            sizes[size].append(idx)
        print(sizes)

        groups = []

        for size in sizes:
            group = []
            for ID in sizes[size]:
                group.append(ID)
                if len(group) == size:
                    groups.append(group)
                    group = []

        return groups



solution = Solution()

groupSizes = [3,3,3,3,3,1,3]

print(solution.groupThePeople(groupSizes))