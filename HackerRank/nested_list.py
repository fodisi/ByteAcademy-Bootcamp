# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format

# The first line contains an integer, , the number of students. 
# The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.


from operator import itemgetter

def nested_list():
    i_name, i_score = 0, 1
    students = []
    #students = [('z', 10), ('y', 4), ('x', 5), ('w', 4), ('t', 5)]

    #gets the inputs
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score))

    # sorts the list by grade[1] and name[0], in ascending order
    students.sort(key=itemgetter(i_score, i_name))
    #print(students)

    #gets the lowest score
    lowest = students[0][i_score]
    # gets the second lowest score, which is the NEXT score bigger than the lowest.
    second_lowest = float(next(
            (s[i_score] for s in students if s[i_score] > lowest)
        ))

    # gets the student names with the second lowest score
    selection = list(s[i_name] for s in students if s[i_score] == second_lowest)
    
    #prints names
    for s in selection:
        print(s)

if __name__ == '__main__':
    nested_list()

