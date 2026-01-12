# Find element Target from an list 

l = [1,2,3,4,5,6,7,8,9,10]
Target = 11

Start = 0
End = len(l) - 1

while Start <= End:
    Mid = (Start + End) // 2

    if Target == Mid:
        print(f"Element Found At Index {Mid}")
    
    elif Target > Mid:
        Start = Mid + 1

    elif Target < Mid:
        End = Mid - 1

else:
    print(f"{Target} not found , can be inserted on postion {Start}")