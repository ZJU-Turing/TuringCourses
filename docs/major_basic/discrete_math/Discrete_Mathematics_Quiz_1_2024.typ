#import "@preview/numblex:0.1.1": numblex
#import "@preview/tablex:0.0.8": tablex
#set text(font: "STSong", size: 10pt)

#set enum(numbering: numblex(numberings: ("1.", "a)")), full: true)

#show heading.where(level: 1): it => [
  #set align(center)
  #set text(size: 20pt, font: "FZXiaoBiaoSong-B05S")
  #it.body
]

#show heading.where(level: 2): it => [
  #set align(center)
  #set text(size: 13pt, font: "FZXiaoBiaoSong-B05S")
  #it.body
]

#show heading.where(level: 3): it => [
  #set align(center)
  #set text(size: 15pt, font: "Princess Sofia")
  #it.body
]

= Discrete Mathematics Quiz 1
== 2023-2024 春夏学期
=== shrike505

#linebreak()
+ Determine whether the following statements are true or false. (30%)
  + The following two propositions are logically equivalent:#align(center)[$p arrow (q arrow r), (p arrow q) arrow r$]
  + If $A$, $B$, $C$ are sets, then $A plus.circle (B plus C) = (A plus.circle B) plus.circle C$.
  + $8 + 3 = 9$ $$iff$$ $8 - 3 = 7$.
  + The set of positive real numbers less than 1 with decimal representations consisting only of 6s and 8s is uncountable.
  + The set of real numbers that are solutions of quadratic equations $a x^2 + b x + c = 0$, where $a$, $b$, $c$ are integers, is countable.
  + The time complexity of a linear search to find the smallest number in a list of $n$ numbers is #sym.Theta ($n log n$).

+ Suppose the variable $x$ represents students, $y$ represents courses, $T(x, y)$ means $\"x$ is taking $y.\"$. Translate the statement into symbols. (10%)
  + There is a course that is being taken by all students.
  + No student is taking all courses.

+ Suppose $g: A arrow B$ and $f: B arrow C$ where $A = {1, 2, 3, 4}, B = {a, b, c}, C = {2, 7, 10}$, and $f$ and $g$ are defined by $g = {(1, b), (2, a), (3, a), (4, b)}$ and $f= {(a, 10),(b, 7),(c, 2)}$. Find $f compose g$. (5%)

+ Write a proposition equivalent to $(p and not q)$ using only $p$, $q$, and the connective #sym.bar.v . (7%) #linebreak() ($\" bar.v \"$ represents NAND. The proposition $p bar.v g$ is true when either $p$ or $q$, or both, are false; and it is false when both $p$ and $q$ are true)

+
  + Express the proposition formula $p plus.circle (q plus.circle r)$ in full disjunctive normal form. (7%)
  + Express the proposition formula $p plus.circle (q plus.circle r)$ in full conjunctive normal form. (7%)

+ Put the functions below in order so that each function is big-O of the next function on the list. (7%)\ #tablex(
  columns: 3,
  rows: 3,
  align: center + horizon,
  auto-lines: false,
  [$f_1 (n) = (1.01)^n$],[$f_2 (n) = 10 n excl$],[$f_3 (n) = (log n)^3$],[$f_4 (n) = 2^n$],[$f_5 (n) = log log n$],[$f_6 (n) = 999 n^2 (log n)^3$],[$f_7 (n) = frac(n^4 + 1, n^3 + 3)$],[$f_8 (n) = n^3 + n (log n)^2$],[$f_9 (n) = 9^999$]
)

+ Set $A = {ceil(x) + ceil(2x) +ceil(3x) bar.v x in R}$, set $B = x bar.v x$ is a positive integer less than $2024}$, find the value of ${A sect B}$ (10%)

+ Prove that if $x^3$ is irrational, then $x$ is irrational. (10%)

+ Use induction to prove that: if $x > 0, y > 0$, then $frac(x^n + y^n, 2) gt.eq (frac(x + y, 2))^n$ for all positive integers $n$.