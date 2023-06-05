[Securing the Barn](https://www.acmicpc.net/problem/1759)

| Memory | Time |
| ----- | -------- |
|31256 KB|40 ms

---

## Task
Farmer John has installed a new security system on the barn and now must issue a valid password to the cows in the herd. A valid password consists of L (3 <= L <= 15) different lower-case characters (from the traditional latin character set 'a'...'z'), has at least one vowel ('a', 'e', 'i', 'o', or 'u'), at least two consonants (non-vowels), and has characters that appear in alphabetical order (i.e., 'abc' is valid; 'bac' is not).

Given a desired length L along with C lower-case characters, write a program to print all the valid passwords of length L that can be formed from those letters. The passwords must be printed in alphabetical order, one per line.

---

## Input Format
- Line 1: Two space-separated integers, L and C
- Line 2: C space-separated lower-case characters that are the set of characters from which to build the passwords

---

## Output Format
- Lines 1..?: Each output line contains a word of length L characters (and no spaces). The output lines must appear in alphabetical order.

---

## Sample Input 0
<pre>4 6
a t c i s w</pre>

---

## Sample Output 0
<pre>acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw</pre>