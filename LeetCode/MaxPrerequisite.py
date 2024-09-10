# Do not remove these imports. You may add others if you wish.
import sys


# Args:
#   disliked: a string, the course you want to avoid taking
#   prereqs: a list of list of strings, each list is a course pair
#            The first course must be taken before the second can be taken
#            ex: [["Algorithms", "AI"], ...] -> Take Algorithms before taking AI
# Returns:
#   an int, the number of courses you can take before taking disliked
def count_courses(disliked, prereqs):
    ptrs = [1] * len(prereqs)
    takenClasses = set()

    for row in prereqs:
        if len(row) != 0:
            takenClasses.add(row[0])

    if disliked in takenClasses:
        takenClasses.remove(disliked)

    count = len(takenClasses)
    while count != len(takenClasses):
        count = len(takenClasses)
        for rowIndex in range(prereqs):
            for colIndex in range(ptrs[rowIndex], len(prereqs[rowIndex])):
                if prereqs[rowIndex][colIndex - 1] in takenClasses:
                    takenClasses.add(prereqs[rowIndex][colIndex])
                    if disliked in takenClasses:
                        takenClasses.remove(disliked)

    return len(takenClasses)

# DO NOT MODIFY BELOW THIS LINE
def main():
    break_line = False
    disliked = ""
    prereqs = []

    for line in sys.stdin:
        line = line.strip()
        if len(line) == 0:
            break_line = True
            continue

        if break_line:
            prereqs.append(line.split(","))
        else:
            disliked = line.split(",")[0]

    print(count_courses(disliked, prereqs))


if __name__ == '__main__':
    main();
