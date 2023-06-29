| #    | Name                                           | Difficulty |
| ---- | ---------------------------------------------- | ---------- |
| 1159 | [TRENER](https://www.acmicpc.net/problem/1159) | Bronze II  |

---

| #   | Memory   | Time  |
| --- | -------- | ----- |
| 1   | 31256 KB | 40 ms |

---

## Task

Mirko has been moving up in the world of basketball, starting as a mere spectator, mastering snack salesmanship, finally reach the coveted position of the national team coach. He is now facing a difficult task: selecting the five primary players for the upcoming match against Tajikistan.

Since Mirko is incredibly lazy, he doesn't bother remembering players' names, let alone their actual skills. That's why he has settled on selecting five players who share the same first letter of their surnames, so that he can remember them more easily. If there are no five players sharing the first letter of their surnames, Mirko will simply forfeit the game!

In order to obtain insight into possibilities for his team, Mirko wants to know all the different letters that his primary team's surnames may begin with.

---

## Input Format

The first line of input contains the positive integer N (1 ≤ N ≤ 150), the number of players that Mirko has available.

Each of the following N lines contains one word (at most 30 characters long, consisting only of lowercase English letters), a surname of one of the players.

---

## Output Format

If there are no five players that Mirko can select matching his criteria, output a single line containing the word “PREDAJA” (without quotes). Otherwise, output all possible first letters of representation player surnames, sorted lexicographically, in a single line with no spaces.

---

## Sample Input

<pre>
18
babic
keksic
boric
bukic
sarmic
balic
kruzic
hrenovkic
beslic
boksic
krafnic
pecivic
klavirkovic
kukumaric
sunkic
kolacic
kovacic
prijestolonasljednikovi
</pre>

---

## Sample Output

<pre>
bk
</pre>
