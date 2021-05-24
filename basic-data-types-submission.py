# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print (
        [[a, b, c] 
        for a in range(x + 1) 
        for b in range(y + 1) 
        for c in range(z + 1)
        if a + b + c != n ]
        )


# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = sorted(set(arr))[-2]
    print(arr)


# Nested Lists
dic = {}
l = []

if __name__ == '__main__':
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        if score in dic: dic[score].append(name)
        else: dic[score] = [name]
        
        if score not in l: l.append(score)
            
    l.remove(min(l))
    
    m = min(l)
    dic[m].sort()
    
    for i in dic[m]:
        print(i)


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
        
    print("{0:.2f}".format(query_score/(len(student_marks[query_name]))))


# Lists
if __name__ == '__main__':
    n = int(input())
    ls = []
    
    for _ in range(n):
        
        s = input().split()
        
        if s[0] != "print":
            s[0] = s[0] + "(" + ",".join(s[1:]) + ")"
            eval("ls."+s[0])
        else: 
            print(ls)


# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    tup = ()
    
    for x in integer_list: tup = tup + (x, )
    print(hash(tup))
