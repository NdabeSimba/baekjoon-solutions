[Digit Generator](https://www.acmicpc.net/problem/2231)

| # | Memory   | Time  |
| - | -------- | ----- |
| 1 | 31256 KB | 40 ms |
| 2 | 31256 KB | 40 ms |

---

## Task
For a positive integer N, the digit-sum of N is defined as the sum of N itself and its digits. When M is the digitsum of N, we call N a generator of M.

For example, the digit-sum of 245 is 256 (= 245 + 2 + 4 + 5). Therefore, 245 is a generator of 256.

Not surprisingly, some numbers do not have any generators and some numbers have more than one generator. For example, the generators of 216 are 198 and 207.

You are to write a program to find the smallest generator of the given integer.

---

## Input Format
Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Each test case takes one line containing an integer N, 1 ≤ N ≤ 100,000.

---

## Output Format
Your program is to write to standard output. Print exactly one line for each test case. The line is to contain a generator of N for each test case. If N has multiple generators, print the smallest. If N does not have any generators, print 0.

---

## Sample Input 0
<pre>
216
</pre>
---

## Sample Output 0
<pre>
198
</pre>