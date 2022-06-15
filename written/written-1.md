# AI2619 Written Assignment 1

> [name=Yikun Ji (520030910154) [Mail](mailto:da-kun@sjtu.edu.cn)]
###### tags: `assignment`

## Question 1

### (a)

Since $\displaystyle{\langle f,\, g \rangle = \int_{-\infty}^{\infty} f(t) g(t) \mathbb d t}$, $\|f\|^2 = \langle f,\, f \rangle$, we have

$\begin{aligned} ||x - y||^2 &= \langle x - y ,\, x - y \rangle  \\ &=  \langle x,\,x\rangle + \langle y,\,y \rangle - 2 \langle x,\, y \rangle \\ &= \int_{-\infty}^{\infty} x^2(t) \mathbb d t + \int_0^T c^2 \mathbb d t - 2\int_0^T cx(t) \mathbb d t \\&= Tc^2 - 2c \int_0^T x(t) \mathbb d t + \int_{-\infty}^{\infty} x^2(t) \mathbb d t \end{aligned}$

Let $f(c) = Tc^2 - 2c \int_0^T x(t) \mathbb d t + \int_{-\infty}^{\infty} x^2(t) \mathbb d t$, so $f(c)$ is a quadratic function. This is a convex optimization problem where:

$$\min_{c}\|x-y\|^2 = \min_c \left(\int_0^T -2cx(t)\,\mathrm{d}t+c^2T\right)$$

Solve for $f'(c) = 0$ and we have $c = \dfrac{\int_0^T x(t) \mathbb d t}{T}$, which is the optimal $c$.

### (b)

For $V$ can be presented as the span of a single function $e(t)$, where $e(t) = \begin{cases}\begin{aligned} & 1 \quad t \in [0,\,T) \\ & 0 \quad \text{o.w.} \end{aligned}\end{cases}$

Suppose $y(t) = \begin{cases}\begin{aligned} & c \quad t \in [0,\,T) \\ & 0 \quad \text{o.w.} \end{aligned}\end{cases}$.

$$\langle x(t), e(t) \rangle = \int_0^Tx(t)\cdot c \,\mathrm{d}t$$

As $\|e(t)\| = c^2T$, we have:

$$y(t) = \begin{cases}
\dfrac{\int_0^T x(t) \mathbb d t}{T}, &t \in [0,\,T) \\
0, &\text{o.w.}\end{cases}$$

### \(c\)

Both methods yield $c = \dfrac{\int_0^T x(t) \mathbb d t}{T}$ for $t \in [0, T)$. I prefer the second method as it is neater.

## Question 2

### (a)

(Trivial by graphical proof, and also trivial by taking the derivative on both sides)

$$f=f(-1)\cdot\varphi_{-1}+f(0)\cdot\varphi_{0}+f(1)\cdot\varphi_{1}$$

### (b)

Orthogonal functions are two functions with an inner product of zero.[^1] Therefore we take the inner product of different pairs of functions:

[^1]: [Reference](https://www.calculushowto.com/orthogonal-functions/#:~:text=Orthogonal%20functions%20are%20two%20functions%20with%20an%20inner,formula%20is%20zero%2C%20then%20the%20functions%20are%20orthogonal.)

$$
\langle \varphi_{-1}, \varphi_0 \rangle = \int_{-1}^1 \varphi_{-1}(t)\cdot \varphi_{0} (t)\ \mathrm{d}t = \frac16
$$

Repeat for three pairs, and it is trivial that $\langle \varphi_{-1}, \varphi_1 \rangle = 0$, thus $\varphi_{-1}, \varphi_1$ are orthogonal.

### \(c\)

Apply [Kindergarten formula] $\boldsymbol{x} =\langle \boldsymbol{x}, \boldsymbol{e}_1\rangle \boldsymbol{e}_1 +\langle \boldsymbol{x}, \boldsymbol{e}_2 \rangle \boldsymbol{e}_2$

Then:

$$
\begin{aligned}
P_{V_1}(\varphi_0)&=\langle \varphi_0, \varphi_{-1} \rangle \varphi_{-1} + \langle \varphi_{0}, \varphi_{1} \rangle \varphi_1 \\
&= \frac16 \cdot \varphi_{-1}(t)+\frac16 \cdot \varphi_1(t)
\end{aligned}
$$

Along with $\hat{\varphi_{0}}=\varphi_0 - P_{V_1}(\varphi_0)$, the resulting graph is as follows:

![](https://sjtusy.pythonanywhere.com/static/geogebra-export.svg)

In fact, $\hat{\varphi_0}$ is a rescaled, translated curve from $\varphi_0$, which means the family $\{\varphi_-1, \hat{\varphi_0}, \varphi_1\}$ are still able to assemble all functions $f \in V$.

### (d)

Suppose $f(t)=a\varphi_{-1}(t)+b\varphi_{0}(t)+c\varphi_{1}(t),\, a,b,c\in\mathbb{R}$.

$$
f(t) = \begin{cases}
a(-t)+b(1+t),&-1<t<0 \\
b(1-t)+ct,&0\leqslant t<1
\end{cases}
$$

The best approximation of $g(t)$ is an $f(t)$ s.t.:

$$\min_{f \in V} \| f(t) - g(t) \| ^2 \text{ i.e. } \min_{f\in V}\langle f-g, f-g \rangle$$

$$
\begin{aligned}
\langle f-g, f-g \rangle &= \frac{a^2}{3}+\frac{a b}{3}-a+\frac{2 b^2}{3}+\frac{b c}{3}-\frac{17 b}{9}+\frac{c^2}{3}-\frac{4 c}{9}+\frac{5}{3}
\end{aligned}
$$

Then we compute:

$$\arg \min\left(\frac{a^2}{3}+\frac{a b}{3}-a+\frac{2 b^2}{3}+\frac{b c}{3}-\frac{17 b}{9}+\frac{c^2}{3}-\frac{4 c}{9}+\frac{5}{3}\right)$$

As $a, b, c$ are all independent, we can give $\{a,b,c\} = \left\{\frac{11}{12},\frac{7}{6},\frac{1}{12}\right\}$. Here is the plot.

![](https://sjtusy.pythonanywhere.com/static/last.svg)

