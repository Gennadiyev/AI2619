# Python Alternatives for AI2619 Course Assignments

![](https://img.shields.io/badge/Made%20with-Jupyter-orange)  ![](https://img.shields.io/badge/Maintained%3F-no-green.svg)

*Professor: [Yuye Ling](http://www.yuyeling.com/)*

My submissions for programming assignments in SJTU AI2619 course. We should be using MATLAB, but I prefer to use a more open-source toolchain. ~~Look MATLAB, we can do everything without you.~~

Feel free to fork and submit your own solutions. Some of the implementations are quite useful in many ways!

## Programming Assignment 1

:link: [Link](https://github.com/Gennadiyev/AI2619/tree/main/programming-1)

This assignment is mainly about denoising and unblurring a manually processed image using [Wiener Filter](https://en.wikipedia.org/wiki/Wiener_filter). It guides us through the mist of convolution and deconvolution for 2D signals.

## Programming Assignment 2

:link: [Link](https://github.com/Gennadiyev/AI2619/tree/main/programming-2)

This assignment is mainly about sampling and performing Fourier Transform on a [rectangular window function](https://ww2.mathworks.cn/help/signal/ref/rectwin.html). It involves Discrete-time Fourier Transform and its inverse.

## Programming Assignment 3

:link: [Link](https://github.com/Gennadiyev/AI2619/tree/main/programming-3)

This assignment requires us to perform DFT to a random signals, but in 4 different ways:
- [`numpy`'s implementation](https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html)
- `for` loop implementation
- Matrix multiplication
- CUDA-accelerated implementation using [`cupy`](https://docs.cupy.dev/en/stable/user_guide/fft.html)

## Programming Assignment 4

:link: [Link](https://github.com/Gennadiyev/AI2619/tree/main/programming-4)

This assignment is all about audio processing. We start from Short-time Fourier Transform, finishing off by creating an equalizer! The [equalizer]() is designed to be used for future purposes, and can be used as a simple module.

> My favorite assignment till now. :smiley_cat:

## Programming Assignment 5

:link: [Link](https://github.com/Gennadiyev/AI2619/tree/main/programming-5)

Image processing task covering histogram matching with various distributions.

## Written Assignments

> I think I should not have exposed all written assignments to public because it may encourage copywork. However, I am personally proud of what I've learned and used thoughout the thoughtfully designed assignments. Some of the solutions are not perfect, and maybe disappointing if you are a math-maniac that digs into the math as much as you can. But most assignment answers here are quite intuitive (at least I think so). So feel free to learn more about this subject of DIP, but **DO NOT copy it** for your own work.

The written assignments are originally hosted on [CodiMD](https://notes.sjtu.edu.cn), which is more featureful than GitHub markdown. The following links are CodiMD links to my solutions. In case the service is down, the markdown sources are also enclosed in the repository [here](https://github.com/Gennadiyev/AI2619/tree/main/written).

- [Assignment 1](https://notes.sjtu.edu.cn/s/3oUIaB2Lh)
- [Assignment 2](https://notes.sjtu.edu.cn/s/an4QDdn5L)
- [Assignment 3](https://notes.sjtu.edu.cn/s/fH0mf_bfR)
- [Assignment 4](https://notes.sjtu.edu.cn/s/3oUIaB2Lh)
- [Assignment 5](https://notes.sjtu.edu.cn/s/aGHrQw1_V)

## Collaboration

~~The assignments are designed to be individual work. If you have any questions regarding my previous submissions (i.e. assignments that have already passed the deadline), please feel free to [submit an issue](https://github.com/Gennadiyev/AI2619/issues). Otherwise you're strongly advised to finish your own work before copying :+1:~~

Let me guess. You're AI2619 student, right?

*If your teacher is also Yuye Ling, he is one of the best teachers you may meet at SJTU, so please listen to his lectures carefully. The course is bound to give you lots of knowledge for later use. Trust me.*

The assignments are now open for [issues](https://github.com/Gennadiyev/AI2619/issues) as well as [pull requests](https://github.com/Gennadiyev/AI2619/pulls).

Best of luck and have fun touring around here!

## Special Thanks

The **TAs** are nice people! They helped me a lot with the assignments, and allowed me to ignore the 2-page-limit on the PDF submissions. Salute to their hard work!

[**Yuye Ling**](http://www.yuyeling.com/) is easily one of the most reliable and responsible teachers I've met in SJTU. He teaches intuitively, and pongs my ping in ~10 minutes (by e-mail), which is an incredible reflex :zap:! **LOTS** of thanks to him!

## License

All the **code** here is licensed under the [MIT License](LICENSE).
