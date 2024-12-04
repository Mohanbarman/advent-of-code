import heapq

a = []
b = []
with open("day1.input", "r") as f:
    for line in f.readlines():
        x, y = list(map(int, line.split("   ")))
        a.append(x)
        b.append(y)


def find_distances(list1: list[int], list2: list[int]):
    heapq.heapify(list1)
    heapq.heapify(list2)

    total_distance = 0

    for _ in range(len(list1)):
        total_distance += abs(heapq.heappop(list1) - heapq.heappop(list2))

    return total_distance

def find_similarity_score(list1: list[int], list2: list[int]) -> int:
    score = 0

    occurence = {}
    for i in list2:
        occurence[i] = occurence.get(i, 0) + 1

    for i in list1:
        score += i * occurence.get(i, 0)

    return score

print(find_similarity_score(a, b))

