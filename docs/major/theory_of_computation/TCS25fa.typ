#show heading.where(level: 1): it => [
  #set align(center)
  #set text(size: 18pt, font: "FZXiaoBiaoSong-B05S")
  #it.body
]

#set enum(numbering: "1.a)")
#let poly = math.cal("P")
#let np = math.cal("NP")
#let bpp = math.cal("BPP")

= Introduction to Theoretical Computer Science

#align(center)[
  #text(size: 13pt,font: "STZhongsong",[2025-2026 秋冬期末])
]

#align(center)[
  #text(size: 13pt,font: "STZhongsong",[图灵回忆卷])
]

1. Write T if the statement is true, and F if it is false.

  + [] If $A$ is computable, then $A^*$ is computable.
  + [] $exists$ a boolean function $F: {0,1}^m -> {0,1}^n$, such that there exists a circuit with at least $Omega(m 2^n)$ gates that computes $F$.
  + [] Gate set {OR, NOT} is universal, in the sense that any boolean function can be computed by a circuit using only these 2 kinds of gates.
  + [] To simulate multiple TMs with $k$ states in total using one TM, the resulting TM needs $Omega(k)$ states.
  + [] To convert an NFA with $k$ states to a DFA, the resulting DFA has $Theta(2^k)$ states.
  + [] Let a DFA with $k$ states recognize a regular language $L$. $L$ contains an infinite number of strings if and only if $L$ contains a string of length at least $k$.
  + [] There exists a randomized algorithm that computes some problem with error rate at most $1/3$ if and only if there exists a randomized algorithm that computes the same problem with error rate at most $1/2026$.
  + [] Probablistic Turing Machine is more powerful than normal Turing Machine, in the sense that it can compute some functions that normal Turing Machine cannot compute.
  + [] If $f,g in poly$ and they are not constant functions, then $f <=_p g$.
  + [] If $f <=_p g$ and $g in bpp$, then $f in bpp$.

2. (Regular Language and Automaton) Judge whether the following languages are regular. Prove your answer.
  1. $L_1 = { w x in {0,1}^* | x "as a binary number", x mod 3 = 2}$.
  2. $L_2 = { w 0 x in {0,1}^* | x "has strictly more 1s than" w}$.
3. (Context-Free Language and Pushdown Automaton) Show that the language $L = { w 101 x in {0,1}^* | w^R "is a subsequence of" x}$ is a context-free language. (Note: *Subsequence* is not the same as *Substring*. For example, "abc" is a subsequence of "axbxc", but not a substring of it.)
4. (Automaton) Let $A$ be a context-free language and $B$ be a regular language. Prove that $A \\ B = { w in {0,1}^* | w in A and w in.not B}$ is a context-free language. (Hint: You may conceptually run a PDA and a DFA in parallel.)
5. (Reduction and Uncomputability) $f: {0,1}^* -> {0,1}$ is a function which takes 2 Turing Machines $M_1$ and $M_2$ as input, and $f(M_1, M_2) = 1$ if there exist at least 2026 strings on which $M_1$ and $M_2$ both halt. Prove that $f$ is uncomputable by reducing HALT to it. (Hint: You may let one of $M_1$ and $M_2$ halt on every input.)
6. （存疑）(Time Complexity Classes) WSAT problem, based on SAT problem, is defined as follows: Given a boolean formula $phi$ in CNF form and every instance is OR of one to three literals (*Note: In WSAT literals are only allowed to be variables themselves and their negations are not allowed*), and an integer $k$, decide whether there exists a satisfying assignment to $phi$ such that *exactly* $k$ variables are assigned to 1. 
  1. Prove that WSAT $in np$.
  2. Prove that VC $<=_p$ WSAT, where VC is the Vertex Cover problem. 