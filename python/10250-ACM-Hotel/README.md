| #     | Name                                               | Difficulty |
| ----- | -------------------------------------------------- | ---------- |
| 10250 | [ACM Hotel](https://www.acmicpc.net/problem/10250) | Bronze III |

---

| #   | Memory   | Time  |
| --- | -------- | ----- |
| 1   | 31256 KB | 44 ms |

---

## Task

Jiwoo, the manager of the ACM Hotel, is about to assign the vacant rooms to the guests upon their arrival. According to customers’ survey, the customers prefer the rooms which are close to the main entrance on-walk. Jiwoo likes to assign the rooms on this policy. Write a program to help Jiwoo on assigning the rooms for the guests.

For simplicity, let’s assume that the ACM hotel is a rectangular shape, an H story building with W rooms on each floor (1 ≤ H, W ≤ 99) and that the only one elevator is on the leftmost side (see Figure 1). Let’s call this kind of hotel as H × W shaped. The main entrance is located on the first floor near the elevator. You may ignore the distance between the gate and the elevator. Also assume that the distances between neighboring rooms are all the same, the unit distance, and that all the rooms only in the front side of the hotel.

<img src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/upload/images2/elevator.png" width=70%>

The rooms are numbered in YXX or YYXX style where Y or YY denotes the number of the floor and XX, the index of the room counted from the left. Therefore the room shaded in Figure 1 should be 305.

The customers do not concern the distance moved in the elevator though the room on the lower floor is preferred than that on the higher floor if the walking distance is same. For instance, the room 301 is preferred than the room 102 since the customer should walk for two units for the latter but one unit, for the former. Additionally, the room 2101 is preferred than the room 102.

Your program should compute the room number which should be assigned for the N-th guest according to this policy assuming that all the rooms are vacant initially. The first guest should be assigned to 101, the second guest to 201, and so on. In Figure 1, for example, the 10th guest should be assigned to the room 402 since H = 6.

---

## Input Format
Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case consists of a single line containing and integers H, W, and N: the number of floors, the number of rooms on each floor, and the index of the arrival time of the guest to be assigned a room, respectively, where 1 ≤ H, W ≤ 99 and 1 ≤ N ≤ H × W.

---

## Output Format
Your program is to write to standard output. Print exactly one line for each test case. The line should contain the room number of the given hotel, where the N-th guest should be assigned.

---

## Sample Input

<pre>
2
6 12 10
30 50 72
</pre>

---

## Sample Output

<pre>
402
1203
</pre>
