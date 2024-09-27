#import "@preview/numblex:0.1.1": numblex
#import "@preview/diagraph:0.2.1": raw-render
#import "@preview/cetz:0.2.2"

#set text(font: "Times New Roman", size: 11pt)
#set par(leading: 1.1em, justify: true)
#set enum(numbering: numblex(numberings: ("1.", "(a)")), full: true, spacing: 2em)
#set figure(supplement: "Fig.", gap: 15pt, caption: "")
#set figure.caption(separator: "")

#let und(w: 5em) = box(width: w, line(length: 100%, stroke: .5pt))
#let header-fn-sized = size => it => [
    #set align(center)
    #set text(size: size, font: "FZXiaoBiaoSong-B05S")
    #it.body
]
#let graph = x => figure(cetz.canvas(x))
#let node = (coord, name) => {
    import cetz.draw: *
    circle(coord, name: name, radius: .3)
    content(name, name)
}
#let raw_edge = (u, v, w, marked: false) => {
    import cetz.draw: *
    set-style(content: (frame: "rect", stroke: none, fill: white, padding: .05))
    if marked { set-style(mark: (end: "straight")) }
    let name = "edge_" + u + "_" + v
    line(u, v, name: name)
    content(name + ".mid", [#w])
}
#let edge = raw_edge.with(marked: false)
#let dedge = raw_edge.with(marked: true)
#let redge = cetz.draw.line

#show heading.where(level: 1): header-fn-sized(20pt)
#show heading.where(level: 2): header-fn-sized(13pt)
#show heading.where(level: 3): header-fn-sized(13pt)

#show regex("(\d+%)"): set text(style: "italic")

= Discrete Mathematics Quiz 3

== 2023-2024 春夏学期

=== Xecades

#v(2em)

+ $R={(a,a), (a,b), (b,d), (a,d)}$ is a relation on ${a, b, c, d}$. Find the smallest relation containing the relation $R$ that is:
  + (6%) partial order relation.
  + (6%) symmetric and transitive.

+ Given the undirected graph $G$ as shown in @fig1.
  + (6%) Use Kruskal's algorithm to find the minimun spanning tree of graph $G$. What is the order in which the edges are added to the minimum spanning tree?
    #graph({
        node((0, 0), "c")
        node((3, 0), "d")
        node((0, 3), "a")
        node((3, 3), "b")
        node((1.5, 1.5), "e")
        node((4.5, 1.5), "f")
        edge("a", "b", 20)
        edge("a", "c", 12)
        edge("a", "e", 9)
        edge("b", "e", 11)
        edge("b", "d", 6)
        edge("b", "f", 5)
        edge("c", "e", 10)
        edge("c", "d", 18)
        edge("d", "e", 14)
        edge("d", "f", 7)
    })<fig1>
  + (6%) Using alphabetical ordering, find a spanning tree for this graph by depth-first search.

+ (6%) The frequencies of six characters are $0.09$, $0.05$, $0.2$, $0.25$, $0.3$ and $0.11$, respectively. If Huffman coding is used for optimal encoding, the average number of bits required to encode a character is #und().

+ (6%) How many leaves does a full $7$-ary tree with $2024$ vertices have?

+ (6%) Determine all positive integers $r$ and $s$ for which the complete bipartite graph $K_(r,s)$ is a tree.

+ (6%) Suppose $abs(A)=4$. Find the number of different equivalence relations on $A$.

+ Answer these questions for the poset $({2, 3, 5, 6, 12, 20, 27, 36, 60}, |)$.
  + (4%) Draw the Hasse diagram.
  + (2%) Find the maximal elements.
  + (2%) Is there a least element?
  + (2%) Find all upper bound of ${2, 3}$.

+ (10%) In the network below (@fig2), find a maximum flow from $A$ to $J$, calculate its flow value, and prove that it is the maximum flow.
    #graph({
        node((0, 1.5), "G")
        node((0, 3), "D")
        node((0, 4.5), "B")
        node((4, 1.5), "H")
        node((8, 1.5), "I")
        node((8, 0), "J")
        node((6, 3), "F")
        node((6, 4.5), "C")
        node((3, 6), "A")
        dedge("B", "D", 10)
        dedge("D", "G", 2)
        dedge("D", "H", 9)
        dedge("G", "H", 7)
        dedge("H", "I", 2)
        dedge("G", "J", 9)
        dedge("H", "J", 9)
        dedge("I", "J", 4)
        dedge("F", "H", 3)
        dedge("F", "I", 3)
        dedge("B", "F", 2)
        dedge("A", "B", 13)
        dedge("A", "C", 7)
        dedge("B", "C", 7)
        dedge("C", "F", 9)
    })<fig2>

+ (8%) Determine if the given pair of graphs (@fig3) is isomorphic. Give the reason.
    #figure(grid(
        columns: 2,
        column-gutter: 2em,
        cetz.canvas({
            node((0, 0), "7")
            node((0, 1), "5")
            node((0, 2), "3")
            node((0, 3), "1")
            node((2, 0), "8")
            node((2, 1), "6")
            node((2, 2), "4")
            node((2, 3), "2")
            redge("1", "2")
            redge("1", "4")
            redge("1", "6")
            redge("3", "2")
            redge("3", "4")
            redge("3", "8")
            redge("5", "2")
            redge("5", "6")
            redge("5", "8")
            redge("7", "4")
            redge("7", "6")
            redge("7", "8")
        }),
        cetz.canvas({
            node((0, 0), "g")
            node((3, 0), "h")
            node((0, 3), "a")
            node((3, 3), "b")
            node((1, 1), "e")
            node((2, 1), "f")
            node((1, 2), "c")
            node((2, 2), "d")
            redge("a", "b")
            redge("b", "h")
            redge("h", "g")
            redge("g", "a")
            redge("c", "d")
            redge("d", "f")
            redge("f", "e")
            redge("e", "c")
            redge("a", "c")
            redge("b", "d")
            redge("h", "f")
            redge("g", "e")
        })
    ))<fig3>

+ $Q_n$ is the graph with $2^n$ vertices representing bit strings of length $n$. An edge exists between two vertices that differ in exactly one bit position.
  + (3%) Find the number of edges of $Q_5$.
  + (3%) Find the chromatic number of $Q_5$. Give the reason.
  + (6%) Determing is $Q_5$ has Hamilton circuit / path. Give the reason.

+ (12%) $8$ students take a test with $8$ true / false questions. It is known that no two students make exactly the same choice. Prove that we can remove one of the $8$ questions, and still no two students make exactly the same choice.
