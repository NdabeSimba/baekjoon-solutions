| #     | Name                                         | Difficulty |
| ----- | -------------------------------------------- | ---------- |
| 13241 | [LCM](https://www.acmicpc.net/problem/13241) | Silver V   |

---

| #   | Memory   | Time  |
| --- | -------- | ----- |
| 1   | 31256 KB | 44 ms |

---

## Task
The integer A is multiple of B if we can multiply B by some integer number bigger than 0 we get A. 

Examples:

- 10 is multiple of 5 because 5*2 is 10
- 10 is multiple of 10 because 10*1 is 10
- 6 is multiple of 1 because 1*6 is 6
- 20 is multiple of 1, 2, 4, 5, 10 and 20.
- We call the lowest common multiple of A and B to the the smallest positive integer C - that is a multiple of both A and B.

Some examples:

- The lowest common multiple of 2 and 5 is 10 because 10 is multiple of 2 and 5 and there is no other common multiple that is smaller.
- The lowest common multiple of 10 and 20 is 20.
- The lowest common multiple of 5 and 3 is 15.
- Your task is to write a program that computes the lowest common multiple of 2 numbers.

---

## Input Format
A single line containing 2 integers A and B separated by one space.

In 50% of the test cases, the number A and B will be less than 1000 (103). In the other 50% of the test cases, the numbers A and B may be bigger than 1000 but smaller than 100000000 (108). 

Note: For the larger test cases you’ll need to declare your variables as 64 bits integers. Use long long int in C/C++ and long in Java.

---

## Output Format
Print a single line containing an integer, the lowest common multiple of A and B.

---

## Sample Input

<pre>
3 5
</pre>

---

## Sample Output

<pre>
15
</pre>
