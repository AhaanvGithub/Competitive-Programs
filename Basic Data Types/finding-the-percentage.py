# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    query_score = 0

    for i in student_marks[query_name]:
        query_score = query_score + i

    print("{0:.2f}".format(query_score / (len(student_marks[query_name]))))
