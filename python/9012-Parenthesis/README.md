[Parenthesis](https://www.acmicpc.net/problem/9012)

| Memory   | Time  |
| -------- | ----- |
| 31256 KB | 52 ms |

---

## Task
Parenthesis String (PS) consists of two parenthesis symbols ‘(’ and ‘)’ only. In parenthesis strings, some strings are called a valid PS (shortly, VPS). Let us give the formal definition of VPS. A single “( )” is a member of VPS, called the base VPS. Let x and y be a member of VPS. Then “(x)”, a VPS which encloses a VPS x with a single pair of parenthesis, is also a member of VPS. And xy, the concatenation of two VPS x and y, is a member of VPS. For example, “(())()” and ((()))” are all VPS, but “(()(”, “(())()))” and “(()” are not VPS. You are given a set of PS. You should decide if the input string is VPS or not. 

---

## Input Format
Your program is to read from standard input. The input consists of T test cases. The number of test cases T is given in the first line of the input. Then PS’s are given in the following T lines one by one. The length of each PS is between 2 and 50, inclusively.

---

## Output Format
Your program is to write to standard output. Print the result in each line. If the input string is a VPS, then print “YES”. Otherwise print “NO”. 

---

## Sample Input 0
<pre>
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
</pre>

---

## Sample Output 0
<pre>
NO
NO
YES
NO
YES
NO
</pre>