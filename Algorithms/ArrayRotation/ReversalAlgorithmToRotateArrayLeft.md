# To rotate an array in left by k index

- value goes from left to rigth

- handing k

if k > len(arr) we need to make sure we rotate it more then 360*

k %= len(arr)

- handling rotation

let arr = [1,2,3,4,5]

we need to rotate it 2 postions

Step 1 : first reverese k postion from beinging

[`2,1`,3,4,5]


Step 2 : reverese till len(arr) from k

[2,1,`5,4,3`]

Step 3 : Rotate Complete Arr

`[3,4,5,1,2]`

which is req Ans