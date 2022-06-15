# AI2619 Written Assignment 5

> [name=Yikun Ji (520030910154) [Mail](mailto:da-kun@sjtu.edu.cn)]

###### tags: `assignment`

## Question 1

*The solution is not unique.*

$$z_1(r)= \begin{cases}\sqrt{r-\frac{1}{2} r^{2}} & 0 \leq r \leq \frac{2-\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} r + 1 - \frac{\sqrt{2}}{2} & \text{o.w.}\end{cases} \ldots(1)$$

This transform function can be found by cumulative distribution function (CDF) matching. The procedure is described as follows:

By definition of Probability Density Function (PDF) and CDF,

$$\begin{aligned}
\newcommand{cdf}[1]{\operatorname{CDF}\left[#1\right]}
\cdf{f_r(r)} &= 2r-r^2 \\
\cdf{f_z(r)} &= \begin{cases}
                   2z^2 & z \le 0.5 \\
                   -2z^2+4z-1 & \text{o.w.}
                \end{cases}
\end{aligned}$$

If $\cdf{f_r} \le 0.5$, i.e. $r \le \frac{2-\sqrt{2}}{2}$, we solve

$$
2r-r^2=2z^2
$$ 

for $z$ and thus $z=\sqrt{r-\frac{1}{2}r^2}$.

If $\cdf{f_r} > 0.5$, i.e. $r > \frac{2-\sqrt{2}}{2}$, we solve

$$
2r-r^2=-2z^2+4z-1
$$

for $z$ and thus $z=\frac{\sqrt{2}}{2} r + 1 - \frac{\sqrt{2}}{2}$.

Therefore we have $z_1$ as written in **Eq.1**.

---

There are quite a lot of other possible transforms from $r$ to $z$. To mention the most straightforward one,

$$z_2 = \sigma \times r \times 0.5 + 0.5$$

where $\sigma$ is a random value selected from $\{-1. 1\}$.

The (non-strict) correctness of both $z_1$ and $z_2$ can be proved by sampling. The Python code is attached in [Appendix A](#Appendix-A).

![](https://notes.sjtu.edu.cn/uploads/upload_3e6f6950e9d507fe74d6b70e630e60bf.png)

:arrow_up: Samples from $f_r$

![](https://notes.sjtu.edu.cn/uploads/upload_06ca90c0cc249d2cc739ee396b6f8eaa.png)

:arrow_up: Samples from $f_r$ and transformed $r$

<div style="page-break-after: always"></div>

## Question 2

### 2 (a)

Denote $g(x,y) = f(x, y) * w(x,y)$.

Let's say we have a $2 \times 3$ kernel and a $9\times 9$ image. For display purpose the padding is omitted.

![](https://notes.sjtu.edu.cn/uploads/upload_354928032693acb33656e5449e4bdb56.png)

The output image will be also $9 \times 9$. Now if we zoom in to one pixel $f(0,0)$:

![](https://notes.sjtu.edu.cn/uploads/upload_a6574f59963794265b066ef2086c681b.png)

We can observe that each coefficient in $W$ (the kernel) is multiplied with $f(0,0)$.

**The same thing happens to every single pixel of the padded image.** Because the image is padded with $0$, the boundary pixels may not multiplied by every coefficient in $W$, but has sum $0$, which we can safely omit.

Therefore we can conclude that when $\sum W = 0$, the output will have a sum of $0$ as well.

### 2 (b)

We see that the above conclusion is independent on the arrangement of coefficients within the kernel $W$.

**If the 2D mask (kernel) used to compute convolution is flipped vertically and horizontally, we are performing correlation,** given proper zero-padding.

Thus, the resulting image will still have a sum $0$.

<div style="page-break-after: always"></div>

## Question 3

$$
\newcommand{iinf}{\int_{-\infty}^{+\infty}}
\newcommand{d}{\mathrm{d}}
\newcommand{j}{\mathrm{j}}
\newcommand{e}{\mathrm{e}}
\begin{aligned}
f(x,y) * h(x,y) &= \iinf\iinf f(s,t) h(x-s,y-t) \d x \d y \\
&=\iinf \iinf \iinf \iinf f(x,y)h(x-s,y-t) \d s \d t \\
&\qquad\cdot\e^{-\j2\pi(ux+vy)}\d x \d y \\
&=\iinf\iinf f(s,t)\e^{-\j 2 \pi(us+vt)}\d s \d t \\
&= \iinf\iinf f(x,y) \e^{-\j 2 \pi (ux+vy)} \d s \d y \\
&\qquad\cdot \iinf \iinf h(x,y)\e^{-\j2\pi(ux+vy)}\d x \d y
\end{aligned}
$$

Notice that

$$\begin{aligned}
&\underbrace{\iinf\iinf f(x,y) \e^{-\j 2 \pi (ux+vy)} \d s \d y}_{F(u,v)}
\cdot \underbrace{\iinf \iinf h(x,y)\e^{-\j2\pi(ux+vy)}\d x \d y}_{H(u,v)} \\
= &F(u,v)\cdot H(u,v).
\end{aligned}$$

Therefore **Eq.3** is proved.

---

$$
\newcommand{ift}{\mathscr{F^{-1}}}
\newcommand{ft}{\mathscr{F^}}
\begin{aligned}
  &\ift \left(F*H\right) \\
  =&\ift \left( \iinf\iinf F(s,t)H(u-s,v-t)\d s \d t \right) \\
  = &\iinf \iinf (\cdot) \e^{\j2\pi (ux+vy)} \d u \d v \\
  = &\iinf \iinf \left[
    \iinf \iinf H(u-s, v-t) \e^{\j 2 \pi ((u-s)x+(v-t)y)} \d (u-s) \d (v-t)
  \right] \\
    & \qquad \qquad \qquad F(s,t) \e^{\j2\pi(sx+ty)} \d s \d t \\
  = &h(x,y) \iinf \iinf F(s,t) \e^{\j 2\pi(sx+ty)} \d s \d t \\
  = &h(x,y)\cdot f(x,y).
\end{aligned}
$$

Therefore **Eq.4** is proved.

<div style="page-break-after: always"></div>

## Question 4

### 4 (a)

<table>
	<tr>		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: #3f3f3f; color: white; width: 30px; height: 30px;'>0.25</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
	</tr>
	<tr>		<td style='background-color: #3f3f3f; color: white; width: 30px; height: 30px;'>0.25</td>
		<td style='background-color: #3f3f3f; color: white; width: 30px; height: 30px;'>0.25</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
	</tr>
	<tr>		<td style='background-color: #3f3f3f; color: white; width: 30px; height: 30px;'>0.25</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
	</tr>
	<tr>		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: #3f3f3f; color: white; width: 30px; height: 30px;'>0.25</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
	</tr>
	<tr>		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: #bfbfbf; color: black; width: 30px; height: 30px;'>0.75</td>
		<td style='background-color: #bfbfbf; color: black; width: 30px; height: 30px;'>0.75</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: #3f3f3f; color: white; width: 30px; height: 30px;'>0.25</td>
		<td style='background-color: #3f3f3f; color: white; width: 30px; height: 30px;'>0.25</td>
	</tr>
	<tr>		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: #3f3f3f; color: white; width: 30px; height: 30px;'>0.25</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
	</tr>
	<tr>		<td style='background-color: #3f3f3f; color: white; width: 30px; height: 30px;'>0.25</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
	</tr>
	<tr>		<td style='background-color: #3f3f3f; color: white; width: 30px; height: 30px;'>0.25</td>
		<td style='background-color: #3f3f3f; color: white; width: 30px; height: 30px;'>0.25</td>
		<td style='background-color: #7f7f7f; color: white; width: 30px; height: 30px;'>0.5</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
	</tr>
	<tr>		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: #3f3f3f; color: white; width: 30px; height: 30px;'>0.25</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
		<td style='background-color: black; color: white; width: 30px; height: 30px;'>0.0</td>
	</tr>
</table>

:heart: See [Appendix B](#Appendix-B) for Python code.

### 4 (b)

From

$$h(x,y)=\dfrac{1}{4}\Large\left(\normalsize h(x-1, y) + h(x+1, y) + h(x, y-1) + h(x, y+1)\Large\right)$$

Then we have a kernel:

$$
h = \begin{pmatrix}
0 & \dfrac{1}{4} & 0 \\
\dfrac{1}{4} & 0 & \dfrac{1}{4} \\
0 & \dfrac{1}{4} & 0
\end{pmatrix}
$$

$$
\begin{aligned}
H(u, v) &=\sum_{x} \sum_{y} h(x, y) \e^{-\j 2 \pi(u x+v y)}\\
&=\frac{1}{4} \cdot\left(\e^{-\j 2 \pi(-v)}+\e^{-\j 2 \pi(-u)}+\e^{-\j 2 \pi(u)}+\e^{-\j 2 \pi(v)}\right) \\
&=\frac{1}{4}\left[\left(\e^{-\j 2 \pi u}+\e^{\j 2 \pi u}\right)+\left(\e^{-\j  2 \pi v}+\e^{\j 2 \pi v}\right)\right]\\
&=\frac{1}{4}[2 \cos (2 \pi u)+2 \cos (2 \pi v)] \\
&=\frac{1}{2} \cos (2 \pi u)+\frac{1}{2} \cos (2 \pi v)
\left(\frac{2\pi}{9} < u < \frac{2\pi}{9}, \frac{2\pi}{7} < v < \frac{2\pi}{7}\right)
\end{aligned} $$

### 4 \(c\)

As the function $H(u,v)$ is only valued under a certain range of frequencies ($|u|< \frac{2\pi}{9},  |v| < \frac{2\pi}{7}$), therefore it is trivial that $H$ is a low-pass filter.

<div style="page-break-after: always"></div>

## Appendix

### Appendix A

```python
import numpy as np
from tqdm import tqdm
import multiprocessing

class Distribution():

    def __init__(self, pdf, range):
        assert callable(pdf)
        assert isinstance(range, tuple)
        self.pdf = pdf
        self.range = range
    
    def __call__(self, c=5000):
        # Draw c samples within the range
        samples = np.random.uniform(self.range[0], self.range[1], c)
        # Get the probability of each sample
        # list(map(func, arr_or_val))
        probs = list(map(self.pdf, samples))
        # Normalize the probabilities
        probs /= sum(probs)
        # Sample from the distribution
        return np.random.choice(samples, p=probs)

    def transform_call(self, c=5000):
        r = self.__call__(c)
        z = np.sqrt(r - r ** 2 / 2) if 0 < r <= 0.2928 else np.sqrt(2) / 2 * r + 1 - np.sqrt(2) / 2 if 0.2928 < r <= 1 else 0
        return z


def firstPDF(x):
    if 0 < x < 1:
        return 2 - 2 * x
    else:
        return 0

def secondPDF(x):
    if 0 < x < 0.5:
        return 4 * x
    elif 0.5 <= x < 1:
        return 2 - 4 * (x - 0.5)
    else:
        return 0

firstDistribution = Distribution(firstPDF, (0, 1))
secondDistribution = Distribution(secondPDF, (0, 1))

sample_count = 50000

if __name__ == '__main__':
    # Create a pool of processes
    processes = multiprocessing.cpu_count()
    # raise NotImplementedError("Do you know you have {} cores?".format(processes))
    p = multiprocessing.Pool(processes=processes)
    # Split the workload
    results = []
    for i in range(sample_count):
        results.append(p.apply_async(firstDistribution))
    # Get the results
    # samples = [r.get() for r in results] with tqdm
    samples = [r.get() for r in tqdm(results)]
    # Close the pool
    p.close()
    # Wait for the processes to finish
    p.join()
    # Plot the distribution
    import matplotlib.pyplot as plt
    plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
    plt.rc('text', usetex=True)
    plt.figure(dpi=400)
    plt.hist(samples, bins=100)
    plt.savefig('distribution.png')
    print("Finished sampling from first distribution")
    # Second distribution
    del p, results, samples
    p = multiprocessing.Pool(processes=processes)
    results = []
    for i in range(sample_count):
        results.append(p.apply_async(firstDistribution.transform_call))
    samples = [r.get() for r in tqdm(results)]
    p.close()
    p.join()
    plt.hist(samples, bins=100)
    # use serif, use tex
    plt.legend(['20000 samples from $r$', '20000 samples from transformed $r$'])
    plt.savefig('distribution2.png')
    print("Finished sampling from second distribution")
```

### Appendix B

```python
from copy import deepcopy

mat_str = '''10000
11000
01100
00111
01100
11000
10000'''

# Generate matrix from string
mat = []
for line in mat_str.split('\n'):
    mat.append([int(x) for x in line])

def aveconv(mat):
    # For each element, take the average of the 4 neighbors, excluding the element itself
    matcopy = deepcopy(mat)
    for i in range(1, len(mat) - 1):
        for j in range(1, len(mat[0]) - 1):
            matcopy[i][j] = (mat[i-1][j] + mat[i+1][j] + mat[i][j-1] + mat[i][j+1]) / 4 
    return matcopy

def pad(mat, pad_w, pad_h):
    # Pad the mat with 0
    for i in range(pad_h):
        mat.insert(0, [0] * len(mat[0]))
    for i in range(pad_h):
        mat.append([0] * len(mat[0]))
    for i in range(len(mat)):
        mat[i] = [0] * pad_w + mat[i] + [0] * pad_w
    return mat

# Write aveconv to html table
def write_to_html(mat, path):
    ...

import matplotlib.pyplot as plt
plt.imshow(mat, cmap='gray')
plt.axis('off')
plt.savefig('original.png')
write_to_html(mat, 'original.html')
mat = pad(mat, 2, 2)
plt.imshow(mat, cmap='gray')
plt.savefig('padded.png')
write_to_html(mat, 'padded.html')
mat = aveconv(mat)
plt.imshow(mat, cmap='gray')
plt.savefig('aveconv.png')
write_to_html(mat, 'aveconv.html')
write_to_html([
    row[1:-1] for row in mat[1:-1]
], 'aveconv_no_pad.html')
```

> Some modifications have been made after the 06/01 lecture by Hang Su.
