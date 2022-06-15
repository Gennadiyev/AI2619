# AI2619 Written Assignment 3

> [name=Yikun Ji (520030910154) [Mail](mailto:da-kun@sjtu.edu.cn)]
###### tags: `assignment`


## Question 1

> $$
\begin{array}{ll}
x[n]=\cos \left(\frac{\pi n}{2}\right), & n=0,1,2,3 \\
h[n]=2^{n}, & n=0,1,2,3
\end{array}
$$

### (a)

$x[n]$ starts with $[0,2,0,2]$. Apply $X[k]=\sum_{n=0}^{N-1}W_N^{kn}\cdot x[n]$ where $N=4$, and we can have:

$$X[0:3] = [0,2,0,2].$$

($X[0:3]$ denotes the sub-array of X, indexed from 0 to 3, i.e. $[X[0], X[1], X[2], X[3]]$.)

### (b)

Similarly as in (a):

$$H[0:3] = [15, -3+\mathrm{j}6, -5, -3-\mathrm{j}6].$$

### \(c\)

$y[n] = \sum_{k=0}^{N-1}x[k]h[((n-k))_N]]$. Perform circular convolution as $h[((n))_4]$ starts with $[1, 8, 4, 2]$:

$\begin{cases}
y[0] = \sum_{k=0}^3 x[k]h[((0-k))_4] = -3 \\
y[1] = \sum_{k=0}^3 x[k]h[((1-k))_4] = -6 \\
y[2] = \sum_{k=0}^3 x[k]h[((2-k))_4] = 3 \\
y[3] = \sum_{k=0}^3 x[k]h[((3-k))_4] = 6 \\
\end{cases}$

Therefore:

$$y[0:3] = [-3, -6, 3, 6].$$

### (d)

From $Y[k] = X[k]\cdot H[k]$ we have:

$$
Y[0:3] = [0,\, -6+\mathrm{j}12,\, 0,\, -6-\mathrm{j}12].
$$

Meanwhile, as $\mathcal{F}^{-1}\left\{X[k]\right\} = \dfrac{1}{N} \mathcal{F} \{X^*[k]\}^*$,

$$y[n] = \dfrac{1}{N}\sum_{k=0}^{N-1} Y[k] W_N^{-nk}.$$

Therefore:

$$y[0:3] = [-3, -6, 3, 6].$$

We see that our result **matches** with the direct computation of the circular convolution.

## Question 2

### (a)

> $$
\sum_{n=-\frac{N}{2}}^{\frac{N}{2}} W_{N+1}^{-n(m-k)}=(N+1) \sum_{r=-\infty}^{\infty} \delta[m-k-r(N+1)]
$$

Since $N$ is even, let $N=2k, k \in \mathbb{Z}^+$.

For simplicity's sake, denote $\mathcal{Y}[m-k]=\sum_{n=-\frac{N}{2}}^{\frac{N}{2}} W_{N+1}^{-n(m-k)}$.

**CASE 1:** $m-k=r(N+1), r\in\mathbb{Z}$, then $W_{N+1}^{-n(m-k)} = 1$, thus:

$$\mathcal{Y}[m-k] = \sum_{N=-\frac{N}{2}}^{\frac{N}{2}}1 = N+1.$$

**CASE 2:** $m-k \neq r(N+1), r\in\mathbb{Z}$, then $W_{N+1}^{-n(m-k)}=W_{N+1}^{-nr_0}$, where $r_0=m-k-r(N+1)$, thus:

$$\sum_{n=-\frac{N}{2}}^{\frac{N}{2}}W_{N+1}^{-nr_0}=0 \Rightarrow \mathcal{Y}[m-k]=0.$$

Finally we have:

$$\mathcal{Y}[m-k] = \begin{cases}
N+1 & m-k=r(N+1), r\in\mathbb{Z} \\
0 &\text{o.w.}
\end{cases}.$$

Which means:

$$
\sum_{n=-\frac{N}{2}}^{\frac{N}{2}} W_{N+1}^{-n(m-k)}=(N+1) \sum_{r=-\infty}^{\infty} \delta[m-k-r(N+1)].
$$

Q.E.D

### (b)

**CASE 1:** When $N$ is even:

$$\begin{aligned}
\sum_{k=-N/2}^{N/2}F_kW_{N+1}^{nk} &= \sum_{k=-N/2}^{N/2}\dfrac{1}{N+1}\left(\sum_{m=-N/2}^{N/2} f_m W_{N+1}^{-mk}\right) W_{N+1}^{nk} \\
&=\dfrac{1}{N+1}\sum_{m=-N/2}^{N/2}f_m\sum_{k=-N/2}^{N/2}W_{N+1}^{-(m-n)k}.
\end{aligned}$$

By orthogonality property, plug
$$
\sum_{n=-\frac{N}{2}}^{\frac{N}{2}} W_{N+1}^{-n(m-k)}=(N+1) \sum_{r=-\infty}^{\infty} \delta[m-k-r(N+1)].
$$
into the above equality, and thus

$$\begin{aligned}
\sum_{k=-N/2}^{N/2}F_kW_{N+1}^{nk} &= \dfrac{1}{N+1}\sum_{m=-N/2}^{N/2}f_m\sum_{r=-\infty}^{\infty}(N+1)\delta[m-n-r(N+1)] \\
&= \sum_{m=-N/2}^{N/2}f_m\delta[m-n] = f_n.
\end{aligned}$$

**CASE 2:** When $N$ is odd:

The procedure is similar to case 1, except we replace $N/2$ with $\left\lfloor \frac{N}{2}\right\rfloor$ (or equivalently, $\frac{N-1}{2}$):

$$\sum_{k=-(N-1)/2}^{(N-1)/2}F_kW_{N+1}^{nk} = f_n.$$

Therefore, we have the DTFT:

$$f_n=\begin{cases}
\displaystyle \sum_{k=-\frac{N}{2}}^{\frac{N}{2}}F_kW_{N+1}^{nk} & N \text{ is even} \\
\\
\displaystyle \sum_{k=-\frac{N-1}{2}}^{\frac{N-1}{2}}F_kW_{N}^{nk} & N \text{ is odd}
\end{cases}.$$

### \(c\)

When $N$ is even, $n=-\frac{N}{2}:\frac{N}{2}.$

$$-\dfrac{A}{2} < -\dfrac{N}{2(N+1)}A \leqslant x_n \leqslant \dfrac{N}{2(N+1)}A < \dfrac{A}{2}.$$

Therefore the sample range does not include $-\frac{A}{2}$ or $\frac{A}{2}$ when $N$ is even.

This remains true for odd $N$.

Therefore, when $N \to \infty$, we have:

$$\left|x_{\pm N/2}\pm\frac{A}{2}\right| \leqslant \dfrac{1}{2(N+1)}A.$$

Thus for constant, finite value $A$,

$$\lim_{n\to\infty}x_{(\pm N/2)} = 0.$$

## Question 3

From $\overline{F_k} = \sum_{n=-3}^{4} \overline{f_n} W_{8}^{kn}$ we have:

| $i$  |            $\overline{F_{i}}$ |
| ---- | -----------------------------:|
| $-3$ |  $-1+\mathrm{j}(2\sqrt{2}-2)$ |
| $-2$ |                           $1$ |
| $-1$ |  $-1+\mathrm{j}(2\sqrt{2}+2)$ |
| $0$  |                           $1$ |
| $1$  | $-1+\mathrm{j}(-2\sqrt{2}-2)$ |
| $2$  |                           $1$ |
| $3$  | $-1+\mathrm{j}(-2\sqrt{2}+2)$ | 
| $4$  |                           $1$ |

Obviously, $\overline{F_{[-3:4]}}$ is neither odd nor imaginary.

The reason is that **such a sampling generates a asymmetric result**.

The input sequence should be defined (extended) as:

$$\overline{f_n}=\{-1, -1, -1, -1, 0, 1, 1, 1, 1\}$$

> *or $\overline{f_n}=\{-1, -1, -1, 0, 1, 1, 1\}$ to shorten the signal. Here we take the longer one.*

This sequence will produce a valid odd and imaginary DFT output:

| $i$  |         $\overline{F_{i}}$ |
| ---- | --------------------------:|
| $-4$ |                        $0$ |
| $-3$ |  $\mathrm{j}(2\sqrt{2}-2)$ |
| $-2$ |                        $0$ |
| $-1$ |  $\mathrm{j}(2\sqrt{2}+2)$ |
| $0$  |                        $0$ |
| $1$  | $\mathrm{j}(-2\sqrt{2}-2)$ |
| $2$  |                        $0$ |
| $3$  | $\mathrm{j}(-2\sqrt{2}+2)$ |
| $4$  |                        $0$ |



## Question 4

### (a)

![](https://notes.sjtu.edu.cn/uploads/upload_87d2671cc47f2e4098cc9e990d3fd818.png)

From the above graph we can easily figure out that the maximum non-zero value count is $59$. Note that value starts from $0$.

### (b)

Let $y[n]=x[n]*h[n]$, then:

$$y[n]=\begin{cases}
x[n] (50) y[n] = 10 & 9 \le n \le 49 \\
5 & 0 \le n \le 4
\end{cases}.$$

(In the above equation, $(50)$ should be ![](https://notes.sjtu.edu.cn/uploads/upload_c9803e4315f0217b4ea1e934e1e68481.png =30x30), but it does not render properly in math formula.)

When $0\le n \le 4$,

$$\begin{aligned}
x[n] (50) y[n] &= \sum_{m-\infty}^\infty x[m] h[n-m] + \sum_{m=-\infty}^{\infty} x[m]h[50+n-m] \\
&= x[n] * h[n] + x[50+n] * h[50+n] = 10,
\end{aligned}$$

therefore,

$$y[n] = 5, (50\le n \le 54).$$

For $n \in [5,8]\cup [55,59]$, $y[n]$ is undetermined.

Therefore, we have:

$$y[n] = x[n]*h[n] = \begin{aligned}\begin{cases} 5 &0\leqslant n \leqslant 4 \\ 10 &9\leqslant n\leqslant 49\\ 5 &50\leqslant n\leqslant 54\end{cases}\end{aligned}.$$

