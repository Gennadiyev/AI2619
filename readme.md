# Python Alternatives for AI2619 Course Assignments

![](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter) \| ![](https://img.shields.io/badge/Maintained%3F-yes-green.svg)

My submissions for programming assignments in SJTU AI2619 course. We should be using MATLAB, but I prefer to go open-source.

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

## Collaboration

The assignments are designed to be individual work. If you have any questions regarding my previous submissions (i.e. assignments that have already passed the deadline), please feel free to [submit an issue](https://github.com/Gennadiyev/AI2619/issues). Otherwise you're strongly advised to finish your own work before copying :+1:

Best of luck and have fun touring around here!

## Special Thanks

The **TAs** are nice people! They helped me a lot with the assignments, and allowed me to ignore the 2-page-limit on the PDF submissions. Salute to their hard work!

**Yuye Ling** is easily one of the most reliable and responsible teachers I've met in SJTU. He teaches intuitively, and pongs my ping in ~10 minutes (by e-mail), which is an incredible reflex :zap:! **LOTS** of thanks to him!
