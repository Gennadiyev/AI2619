# AI2619 Written Assignment 4

> [name=Yikun Ji (520030910154) [Mail](mailto:da-kun@sjtu.edu.cn)]
###### tags: `assignment`

## Question 1

![](https://kunologist.pythonanywhere.com/static/fin.svg)

<div style="text-align:center"><b>Figure 1:</b> The output signal sketch</div>
<br>

> The above figure is in fact more precise than a sketch. It is a function:
> ![](https://notes.sjtu.edu.cn/uploads/upload_9609ebf0006ea16edf88392ae3e4f6fc.png)
> Most parameters are estimated from the original $x[n]$, though.

Define

$$x_1[n] = \begin{cases} x[n], &n\in[0,60) \\ 0, &\text{o.w.} \end{cases}, x_2[n]=\begin{cases} x[n], &n\in[60, 120) \\ 0, &\text{o.w.} \end{cases}, x_3[n] = \begin{cases} x[n], &n\in[120,180) \\ 0, &\text{o.w.} \end{cases}.$$

The magnitude is multiplied by $6$ for $x_1$, by $0$ in $x_2$, and by $4$ in $x_3$. We omit the 0-magnitude part for the rest sketching.

The group delay is $0$ for $x_1$ and $140$ for $x_3$.

The phase offset is $-50^\circ$ for $x_1$ and $-100^\circ$ for $x_3$.

Therefore we have the above figure.

## Question 2

### (a)

$$y[n]-\dfrac54y[n-1]-\dfrac32y[n-2]=x[n]-x[n-1].$$

### (b)

$$\begin{aligned}
H(z) &= \dfrac{1-z^{-1}}{1-\frac54z^{-1}-\frac32z^{-2}} \\
     &= \dfrac{1-z^{-1}}{\left(1-2z^{-1}\right)\left(1+\frac34 z^{-1}\right)}.
\end{aligned}$$

The Pole-Zero plot for the system:

![](https://kunologist.pythonanywhere.com/static/tsetse.svg)

<div style="text-align:center"><b>Figure 2:</b> Pole-zero plot for H</div>

From Euler's Theorem,

$$
\newcommand{j}{\mathrm{j}}
x[n]=\cos(\omega n) = \frac{1}{2} e^{\j \omega n}+\frac{1}{2} e^{-\j \omega n}.
$$

<!-- Select input $x_1[n]=\frac12e^{\j \frac{\pi}2 n}$ as depicted in Figure 2. From the lengths of the segments we see that the output amplitude should be:

$$
A=\frac{\frac{\sqrt{5}}{2}}{\frac{\sqrt{13}}{4} \cdot \frac{\sqrt{17}}{2}}=4 \sqrt{\frac{5}{221}},
$$

And the phase angle

$$\begin{aligned}
\phi &= -\arctan \frac{1}{2}-\left(-\arctan \frac{1}{4}+(-\pi)+\arctan \frac{2}{3}\right) \\
&=-\arctan \frac{1}{2}+\arctan \frac{1}{4}-\arctan \frac{2}{3}+\pi.
\end{aligned}$$
 -->
 
Thus $y[n]=\dfrac12 H\left(e^{\j \omega}\right)e^{\j\omega n}+\dfrac12H\left(e^{\j\omega}\right)e^{-j\omega n}$, which, from the Pole-zero plot,

$$\begin{cases}
\left| H\left(e^{\j\omega}\right) \right| = \dfrac{4\sqrt{10}}{25} \\
\varphi = \angle H\left(e^{\j\omega}\right)=-\dfrac\pi 4-\arctan\left(-\dfrac12\right)-\pi+\arctan\left(\dfrac43\right)
\end{cases}$$
 
Therefore $y[n]=\dfrac{4\sqrt{10}}{25}e^{\j\varphi} \cos(\omega n), A=\dfrac{4\sqrt{10}}{25} e^{\j\varphi}, \phi = 0.$
 
## Question 3

### (a)

$$\newcommand{gd}{\tau_{g}} \gd = \dfrac{b(a\cos\omega+b)}{a^2+2ab\cos\omega+b^2}.$$

### (b)

$$\gd = - \dfrac{c(\cos\omega+c)}{1+2c\cos\omega+c^2}.$$

### \(c\)

$$\gd=\dfrac{b(a\cos\omega+b)}{a^2+2ab\cos\omega+b^2}-\dfrac{c(\cos\omega+c)}{1+2c\cos\omega+c^2}.$$

### (d)

$$\gd=-\dfrac{c(\cos\omega+c)}{1+2c\cos\omega+c^2}-\dfrac{d}{1+3d\cos\omega+d^2}.$$

## Question 4

Fitst, we have:

$$\begin{aligned}
H_{ap}(z)&=k\cdot\dfrac{z^{-1}-\dfrac14}{1-\dfrac14 z^{-1}},  \\
H_\min(z)&=\dfrac{z^{-1}-\frac14}{\left(1-\frac12z^{-1}\right)\left(1-3z^{-1}\right)}\cdot \left(k\cdot\dfrac{z^{-1}-\frac14}{1-\frac14z^{-1}}\right)^{-1} \\
&= \dfrac{1}{k}\cdot \dfrac{1-\frac14 z^{-1}}{\left(1-\frac12z^{-1}\right)\left(1-3z^{-1}\right)}
\end{aligned}$$

We then draw the pole-zero plot of $H_{ap}$ and $H_{min}$, respectively.

![](https://kunologist.pythonanywhere.com/static/hap.svg)
<div style="text-align:center"><b>Figure 3:</b> Pole-zero plot for Hap</div>

The ROC is $|z|>\frac14$.

![](https://kunologist.pythonanywhere.com/static/hmin.svg)
<div style="text-align:center"><b>Figure 4:</b> Pole-zero plot for Hmin</div>

The ROC is $|z|>\frac12$.

Because only 1 zero point exists outside the unit circle, the decomposition is unique.

## Question 5

> For this problem, we will momentarily forget about the real-imaginary plot and focus on the coordinates as if on Descartes coordinates.

Let $Z(z,0)$, $P(p,0)$.

For $D(\cos\phi, \sin\phi)$, we have:

$$
\left(\alpha^{2}-1\right) \cos^2\phi+\left(\alpha^{2}-1\right) \sin^2\phi-2 \alpha^{2} z x+2 p x=p^{2}-\alpha^{2} z^{2}
$$

Additionally, the origin $(0,0)$ implies that:

$$-2\alpha^2 z +2p =0,$$

hence

$$p^2-\alpha^2z^2=\alpha^2-1\Rightarrow\begin{cases}
z= \frac 1 \alpha \\
p= \alpha
\end{cases},$$

therefore $|OZ|\cdot|OP|=1$


