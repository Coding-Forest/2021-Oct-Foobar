# Employees salute when they "cross".
# Hallway exits do not count.

# Key algorithms: regular expression, counting, indexing

# For each  > (right-going employee),
# count < (left-going employee).
# Then double the total encounters (because they greet "each other").

# string.count("char")
# list.index(element)
# string.capitalize()

example_salute = "--->-><-><-->-"
test_salute1 = ">----<"
test_salute2 = "<<>><"



# Actual Code submitted ---------------------------------------

def solution(s):
    hall = s.replace("-", "")
    crosses = 0

    for i, char in enumerate(hall):
        if (char == ">"):
            crosses += hall[i:].count("<")

    salutes = crosses * 2
    return salutes

print(solution(example_salute))
print(solution(test_salute1))
print(solution(test_salute2))




# Visible Quality Assuarance Check ------------------------------

hall = example_salute.replace("-", "")
crosses = 0

for i, char in enumerate(hall):
    if (char == ">"):
        print(f"lefts for each right ({i}): {hall[i:].count('<')}")
        crosses += hall[i:].count("<")
        print(f"cross count: {crosses}")

salutes = crosses * 2
print(f"total salute count: {salutes}")
