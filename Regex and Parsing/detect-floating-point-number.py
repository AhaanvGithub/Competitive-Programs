# Detect Floating Point Number
for i in range(int(input())):    
    try:
        n = input()        
        int(n.split('.')[1])
        if float(n):
            print('True')
    except:        
        print('False')
