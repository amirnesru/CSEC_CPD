t = int(input())
for _ in range(t):
    length = int(input())
    array = list(map(int, input().split()))
    
    count_of_ones = 0
    available_extra_units = 0
    
    for number in array:
        if number == 1:
            count_of_ones += 1
        else:
            available_extra_units += (number - 1)
    
    if length > 1 and available_extra_units >= count_of_ones:
        print("YES")
    else:
        print("NO") 
