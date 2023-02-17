# ross-technical-test
Solution to the software developer pre-interview quiz

## Strategy 1
[3,2,4,1] min = 1, max = 4\
[1,4,2,3] min = 2, max = 4\
[4,1,2,3] min = 2, max = 3\
max is at first index implies flip from last\
last --\
[3,2,1,4]\
max is at first index implies flip from last\
[1,2,3,4]\

## Strategy 2 (implemented)
Flip from the maximum number index. Bring max num to index 0\
then flip from last element so that the max is at the end of list\
Decrement max and last everytime they are used as index for flipping\
[3,2,4,1] max = 4 ; last = 4\
[4,2,3,1] max = 3 ; last = 4\
[1,3,2,4] max = 3 ; last = 3\
[3,1,2,4] max = 2 ; last = 3\
[2,1,3,4] max = 2 ; last = 2\
[1,2,3,4] max = 1\