# Boyer–Moore Voting Algorithm (Majority Element)

- Used to find the **majority element**
- Majority element = element that appears **more than n/2 times**
- Time: **O(n)**
- Space: **O(1)**

## Key Idea

- Maintain a **candidate** and a **count**

- Same element → increase count  
- Different element → decrease count  
- When count becomes 0 → change candidate


## Example

```

arr = [2,2,1,1,1,2,2]

````
step - first candidate = 2

votes for 2 = I I

step - remove 2 times as diff candidate appered ! 

votes for 2 = - 

step - chnage candidate as curr candidate is 1 and votes are 0

votes for 1 = I

step - remove vote as diff appered

vote for 1 = - 

step - as 0 votes and diff candidate appered

vote for 2 = I

step - last candidate is 2 and have votes 1

ans = `most freq is 2`