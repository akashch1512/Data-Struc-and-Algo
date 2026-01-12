# To rotate an array in rigth by k index

- value goes from rigth to left

- handing k

if k > len(arr) we need to make sure we rotate it more then 360*

k %= len(arr)

- handling rotation

let arr = [1,2,3,4,5]

let we need to rotate it k = 2 postions

ans = [4,5,1,2,3]

Step 1 : first Rotate Complete Arr

`[5,4,3,2,1]`

Step 2 : reverese till k from beinging

[`4,5`,3,2,1]

Step 3 : reverese next till len(arr) from k

[4,5,`1,2,3`]

which is req Ans