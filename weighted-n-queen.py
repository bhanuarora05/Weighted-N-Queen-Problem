n=0
p=0
s=0
matrix=[]
city=[]
max_activity = 0

def check_pos(city,row,col):
    for i,j in city:
        if abs(row - i) == abs(col - j):
            return 0
    return 1

def solnps(city,starting,col_list):
    row = starting
    count = len(city)
    global matrix,p,n,max_activity
        
    
    while True:
        if (row+p-1)==(n+count):
            break
        col = 0
        while col<n:
            if col in col_list:
                col += 1
                continue
                
            if check_pos(city,row,col):
                if count == (p-1):
                    activity_points=matrix[row][col]
                    for i,j in city:
                        activity_points += matrix[i][j]
                    
                    if activity_points > max_activity:
                        max_activity = activity_points
                    
                    col += 1
                    continue
                
                city.append((row,col))
                col_list[col] = 1
                solnps(city,row+1,col_list)
                city.pop()
                col_list.pop(col)
                
            col += 1
            
        row += 1

file = open("input.txt","r")
i=0  
for line in file:
    line = line.replace('\n','')
    if i==0:
        n=int(line)
        for p in range(n):
           matrix.append([])
           for q in range(n):
            matrix[p].append(0)
            
    elif i==1:
        p=int(line)
    elif i==2:
        s=int(line)
    else:
        temporary=line
        arr=temporary.split(",")
        matrix[int(arr[1])][int(arr[0])] += 1
        
    i+=1
    
file.close()
    

col_list = {}
solnps(city,0,col_list)
file1 = open("output.txt","w")
file1.write(str(max_activity))
file1.write("\n")
file1.close()