#import "@preview/numblex:0.1.1": numblex
#import "@preview/cetz:0.2.2"
#import "@preview/wrap-it:0.1.0": wrap-content
#import "@preview/fletcher:0.5.0": diagram, node, edge
#import cetz.draw: *

#let graph = x => cetz.canvas(x)
#set page(margin: 4em)
#set text(font: "STSong", size: 11pt)
#set par(leading: 0.6em, justify: true)
#set enum(numbering: numblex(numberings: ("1.", "a)")), full: true)

#show heading.where(level: 1): it => [
  #set align(center)
  #set text(size: 20pt, font: "Playfair Display")
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

#let answer = [#box(width: 1fr,repeat("_"))]

= Discrete Mathematics Quiz 4
== 2023-2024 春夏学期
=== shrike505

#linebreak()

+ Fill in the blanks. (40%, 5% each)
  + Write a proposition equivalent to $(p and not q)$ that uses only $p$, $q$, $not$, and the connective $or$.
  + Express the negations of the statement $exists x exists y P(x, y) and forall x forall y Q(x, y)$ so that all negation symbols immediately precede predicates.
  + If $G$ is a planar connected graph with 20 vertices, each of degree 3, then $G$ has #answer regions.
  + Given a rectangular coordinate system in three-dimensional space, how many points are there whose three coordinate values are all rational numbers? #answer
  + #let snode = (coord, name, location) => {
        circle(coord, name: name, radius: 0.06, fill: black)
        content(name, name, padding:.144, anchor: location)
        // Credit to Xecades
    }
    #let f1 = figure(graph({
        snode((0, 3), "a","south")
        snode((1.5, 3), "b","south")
        snode((3, 3), "c","south")
        snode((4.5, 3), "d","south")
        snode((0, 1.5), "e", "south-east")
        snode((1.5, 1.5), "f","south-east")
        snode((3, 1.5), "g","south-east")
        snode((4.5, 1.5), "h","south-east")
        snode((0, 0), "i","north")
        snode((1.5, 0), "j","north")
        snode((3, 0), "k","north")
        snode((4.5, 0), "l","north")
        let thinline = (name1,name2) => {
          line(name1, name2, stroke:(thickness: 0.7pt))
        }
        thinline("a", "b")
        thinline("b","c")
        thinline("c","d")
        thinline("a","e")
        thinline("b","f")
        thinline("c","g")
        thinline("d","h")
        thinline("e","f")
        thinline("f","g")
        thinline("g","h")
        thinline("e","i")
        thinline("f","j")
        thinline("g","k")
        thinline("h","l")
        thinline("i","j")
        thinline("j","k")
        thinline("k","l")
        thinline("i","l")
    }))
    #wrap-content(f1, align: bottom + right, columns: (50%, 50%),column-gutter:-0.5em)[A dominating set of vertices in a simple graph is a set of vertices suth that every other vertex is adjacent to at least one vertex of this set. A dominating set with the least number of vertices is called a minimum dominating set. Find the number of vertices of minimum dominating set for the given graph.]
    #v(2em)
  + Does the graph above have a Hamilton circuit? If it does, find such a circuit. If it does not, give an argument to show why no such circuit exists. #answer
  + What is the worst-case time complexity of Dijkstra#text(['],font: "Garamond")s algorithm for computing the shortest path between two points in a weighted graph with n vertices?
    #let bignode = (coord, name) => {
      circle(coord, name: name, radius: 0.3)
      content(name, name, padding:.1)
    }
    #let f2 = figure(diagram(
      let (a,b,c,d) = ((-2,0), (0.6,0), (-2,1.7), (0.6,1.7)),
      node(a, [A], stroke: 1pt),
      node(b, [B], stroke: 1pt),
      node(c, [C], stroke: 1pt),
      node(d, [D], stroke: 1pt),
      edge(b, a, bend: -10deg,"-|>"),
      edge(a, b, bend: -10deg,"-|>"),
      edge(a, c, "-|>"),
      edge(b, d, "-|>"),
      edge(d, a, "-|>"),
      edge(c, d, bend: -10deg,"-|>"),
      edge(d, c, bend: -10deg,"-|>"),
    ))
  + #wrap-content(f2, columns:(50%, 44%), align: right+bottom)[How many distinct paths of length are there in the given graph? (Note: Cycles are allowed.) #answer]
    #v(2em)
+ There are three consecutive positive integers that are divisible by 5, 7, and 11 respectively （依次能被 5, 7, 11 整除）. Find all the solutions. (6%)
+ (30%, 5% each) A standard deck of 52 cards consists of 4 suits, with each suit containing 13 cards corresponding to 13 values.
  + How many different poker hands of 5 cards that containing four cards of the same value? （xxxxy 牌型，问有多少种可能取法）#v(4em)
  + How many different poker hands of 5 cards that containing 2 pairs （两个对子，对子数字相同但花色可以不同）but not including 3 cards of the same value? （xxyyz 牌型，问有多少种可能取法） #v(4em)
  + How many playing cards do you need to take at random to ensure that there is a pair among them? #v(4em)
  + How many playing cards do you need to take at random to ensure that there is a straight（顺子，五张数字连续的牌）among them?（注：A-2-3-4-5 和 10-J-Q-K-A 都算顺子，花色可以不同） #v(4em)
  + Ignoring the differences in suits, how many different ways are there for taking out 3 cards? （把数字相同但花色不同的牌视为不可分辨） #v(4em)
  + Put these 52 cards into a grid with 4 rows and 13 columns, and prove that by selecting one card from each column, you can always get all the 13 values. （提示：可看作一个完全匹配问题） #v(8em)
+ Use generating functions to solve the recurrence relation $a_k= 5 a_(k-1) - 6 a_(k-2)$ with initial conditions $a_0 = 6$ and $a_1 = 30$. (12%) #v(8em)
+ There are n red points and n green points on the plane, any three of them are not collinear. Please use induction to prove: These $2 n$ points can be connected in pairs to form n non-intersecting line segments. Each line segment connects a red point and a green point. (12%)