#import "@preview/numbly:0.1.0": *
#set enum(full: true, numbering: numbly("{1:一、}", "({2})",))
#set text(size: 14pt, font: "Source Han Serif SC")
#let title(body, lev:1) = {
  show heading.where(level: lev): it => [
    #set align(center)
    
    #if lev == 1 {
      text(size: 22pt, font: "Source Han Serif SC")[#it.body]
    } else if lev == 2 {
      text(size: 18pt, font: "FZXiaoBiaoSong-B05S")[#it.body]
    }
  ]
  heading(body, level: lev)
}

#title(lev: 1)[概率论（H）2023-2024 秋冬小测]

#align(center)[#text(size: 15pt,font: "Ink Free",[shrike505])]

#title(lev: 2)[第一次小测：2024年10月11日]

+ 
    + 假设事件 $A, B, C$ 互不相容，且 $P(A) = P(B) = 0.2, P(C) = 0.4$. 求 $P(A dash.en(C) union B)$.
    + 假设事件 $A, B$ 相互独立，且 $P(A) = 0.6, P(B) = 0.3$. 求 $A$ 与 $B$ 至少有一个发生的条件下 $A$ 发生的概率.
    + 对随机事件 $A, B$，若 $P(A bar B) = 0.2, P(dash.en(A) bar dash.en(B)) = 0.3, P(B) = 0.4$，求 $P(B bar A)$.
+ 在线段 $A B$ 中随机取三点 $C, D, E$, 求三线段 $A C, A D, A E$ 可构成三角形的概率.
+ 投票选举甲乙两人，已知甲共得 $m$ 张，乙共得 $n$ 张，$m gt.eq n + 2$. 求在第一张票后的计票过程中，甲得票数始终至少领先乙得票数 $2$ 张的概率.

#title(lev: 2)[第二次小测：2024年11月22日]

+ 设随机变量 $xi_1, xi_2, dots, xi_n$ 相互独立，且同分布. $P(xi_1 = i) = frac(2, 3^i), i = 1, 2, dots, n$. 令 $eta = min_(1 lt.eq k lt.eq n) xi_k$
    + 求 $P(eta gt.eq i)$.
    + 求 $eta$ 的分布列.
+ 设 $X, Y$ 为非负整数值随机变量，$X + Y tilde P(lambda)$（泊松分布），并在给定 $X + Y = n$ 的条件下，$X tilde B(n, p)$. 求 $X, Y$ 的分布.
+ 设随机变量 $X_1, X_2, X_3$ 相互独立，都服从参数为 1 的指数分布，
  
  记 $Y_1 = frac(X_1, X_1 + X_2), Y_2 = frac(X_1 + X_2, X_1 + X_2 + X_3), Y_3 = X_1 + X_2 + X_3$.
    
    + 求 $(Y_1, Y_2, Y_3)$ 的联合密度函数.
    + 证明 $Y_1, Y_2, Y_3$ 相互独立.