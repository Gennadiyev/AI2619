# AI2619 Written Assignment 2

> [name=Yikun Ji (520030910154) [Mail](mailto:da-kun@sjtu.edu.cn)]
###### tags: `assignment`

## Question 1

### (a)

$\begin{aligned}
\tilde{X}_3[k] &= \sum_{0}^{3N-1}\tilde{x}[n]W_{3N}^{kn}=\sum_{n=0}^{N-1}\tilde{x}[n]W_{3N}^{kn}+\sum_{n=N}^{2N-1}\tilde{x}[n]W_{3N}^{kn}+\sum_{n=2N}^{3N-1}\tilde{x}[n]W_{3N}^{kn} \\
&= \sum_{n=0}^{N-1}\tilde{x}[n]W_{3N}^{kn} \left(1+W_{3N}^{kn}+W_{3N}^{2kn}\right) \\
&=\dfrac{1}{N}\left(1+W_{3N}^{kn}+W_{3N}^{2kn}\right)\sum_{n=0}^{N-1}W_{3N}^{kn}\sum_{k=0}^{N-1}\tilde{X}[k]W_N^{kn}
\end{aligned}$

- **CASE 1** When $3\mid m$ (i.e. $\left\lfloor{\dfrac{m}{3}}\right\rfloor=\dfrac{m}{3}$), based on:

  $$\sum_{n=0}^{N-1}W_{N}^{(m-l)n}=\begin{cases}0 & m\neq l \\ N & m = l\end{cases}$$

  We have $\tilde{X}_3[k] = \dfrac{3}{N}\cdot N \tilde{X}\left[\dfrac{k}{3}\right]=3\tilde{X}\left[\dfrac{k}{3}\right]$

- **CASE 2** When $3 \not\mid m$, it's trivial that $1+W_3^k+W_3^{2k}=0$, therefore $\tilde{X}_3[k] = 0$.

Therefore:

$$\tilde{X}_3[k] = \begin{cases}
0 & 3 \not \mid m \\
3\tilde{X}\left[\dfrac{k}{3}\right] & 3 \mid m \\
\end{cases}$$

### (b)

> I love the problem design

Firstly:

$\tilde{X}[0]=\tilde{x}[0] \cdot W_{2}^{0} + \tilde{x}[1] \cdot W_{2}^{0} = 1 + 2 = 3$

$\tilde{X}[1]=\tilde{x}[0] \cdot W_{2}^{0} + \tilde{x}[1] \cdot W_{2}^{1} = 1 - 2 = -1$

It is trivial that $\tilde{X}[k]$ is **periodic** with period $2$. Therefore:

$$\tilde{X}[k] = \begin{cases}
3 & 2 \mid k \\
-1 & \text{o. w.}
\end{cases}$$

Next:

$\tilde{X}_3[0] = \sum_{n=0}^5 {\tilde{x}[n] W_6^0} = 1+2+1+2+1+2 = 9$

$\tilde{X}_3[1] = \sum_{n=0}^5 {\tilde{x}[n] W_6^n} = e^0 + e^{-\frac{2}{6}\pi} + e^{-\frac{4}{6}\pi} + 2 \left(e^{-\frac{1}{6}\pi} + e^{-\frac{3}{6}\pi} + e^{-\frac{5}{6}\pi}\right) = 0$

$\tilde{X}_3[2] = \sum_{n=0}^5 {\tilde{x}[n] W_6^{2n}} = 3\left(e^{0}+e^{\frac{\pi}{3}}+e^{-\frac{2\pi}{3}}\right) = 0$

Similarly, the first $6$ terms of $\tilde{X}_3$ are:

| Term | $\tilde{X}_3[k]$ |
| - | - |
| 0 | $9$ |
| 1 | $0$ |
| 2 | $0$ |
| 3 | $-3$ |
| 4 | $0$ |
| 5 | $0$ |

Meanwhile, it is trivial that $\tilde{X}_3$ is **periodic** with period $6$.

Therefore:

$$\tilde{X}_3[k] = \begin{cases}
9 & k=6\nu \\
0 & k=6\nu+1 \\
0 & k=6\nu+2 \\
-3 & k=6\nu+3 \\
0 & k=6\nu+4 \\
0 & k=6\nu+5 \\
\end{cases}, \nu \in \mathbb{N}^*$$

Results verified!

## Question 2

### (a)

$X\left(e^{\mathrm{j}\omega}\right)=\sum_{n=-\infty}^{+\infty}x[n]e^{-\mathrm{j}\omega n}=\sum_{n=0}^{+\infty}\alpha^n e^{-\mathrm{j}\omega n}=\dfrac{1}{1-\alpha e^{-\mathrm{j}\omega}}$

> Last semester we take the above equation as granted, and used it a *lot* because it is everywhere in the test.

### (b)

$\begin{aligned}
\tilde{X}[k]&=\sum_{n=0}^{N-1}\tilde{x}[n]W_N^{kn} \\
&= \sum_{n=0}^{N-1}\sum_{r=0}^{+\infty}x[n+rN]W_N^{kn} \\
&= \sum_{n=0}^{N-1}\sum_{r=0}^{+\infty}\alpha^{n+rN}W_{N}^{kn} \\
&= \sum_{n=0}^{N-1}W_{N}^{kn}\cdot \dfrac{\alpha^n}{1-\alpha^N} \\
&= \dfrac{1}{1-\alpha^N}\cdot\dfrac{1-\alpha^N e^{-\mathrm{j}2 \pi}}{1-\alpha e^{-\mathrm{j} \frac{2k\pi}{N}}} \\
&= \dfrac{1}{1-\alpha e^{-\mathrm{j} \frac{2k\pi}{N}}}
\end{aligned}$

### \(c\)

$\tilde{X}[k]$ is the **sampling** of $X\left(e^{\mathrm{j}\omega}\right)$ with sampling interval $\Delta\omega=\dfrac{2\pi}{N}$
