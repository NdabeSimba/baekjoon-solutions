| #     | Name                                                              | Difficulty |
| ----- | ----------------------------------------------------------------- | ---------- |
| 11366 | [Tons of Orcs, no Fibbin’](https://www.acmicpc.net/problem/11366) | Silver IV  |

---

| #   | Memory   | Time  |
| --- | -------- | ----- |
| 1   | 31256 KB | 44 ms |

---

## Task
The armies of Mordor are fearsome in both stature and numbers. How did they raise such a host in so short a time? It turns out, orcs breed very quickly. For any given year, their population equals the sum of the populations from the previous two years. For example, if there are 14 orcs in year 7 and 20 orcs in year 8, then we can calculate a total population of 34 orcs in year 9, and a total population of 54 orcs in year 10. Given the populations in two previous years, calculate the population at the nth following year.

---

## Input Format
Each test case is on its own line, each of the form a b c; Here a and b are non-negative integers denoting the number of orcs in the previous two years, and c is the number of years in the future to calculate the population in. The end of input is marked by a line of the form ”0 0 0”, which should produce no output. No values will exceed the value that can be stored in an int variable.

---

## Output Format
For each test case, output one integer on its own line describing the number of orcs in the specified year. No values will exceed the value that can be stored in an int variable.

---

## Sample Input

<pre>
10 10 1
0 39 4
14 20 1
0 0 0
</pre>

---

## Sample Output

<pre>
20
195
34
</pre>
