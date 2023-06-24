# Denoising Bitcoin's Price Graph using Linear Algebra (from Scratch)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
Spring 2021

This project aims to denoise Bitcoin's price graph by utilizing the principles of linear algebra and implementing the least-squares method. The goal is to remove the noise from the original price data and obtain a smoother representation of Bitcoin's price trends.

## Introduction
Bitcoin's price graph often contains a significant amount of noise, which can make it challenging to analyze trends and patterns accurately. This project addresses this issue by applying a denoising algorithm based on the principles of linear algebra. The algorithm utilizes the least-squares method to remove the noise and produce a cleaner representation of Bitcoin's price fluctuations.

## Dataset
The dataset used in this project consists of Bitcoin's prices recorded every 2 hours from the end of 2020 to the 20th of May 2021. The dataset provides a comprehensive view of Bitcoin's price fluctuations during this period, serving as the foundation for denoising the price graph.

## Methodology
The denoising process is based on the principles of linear algebra, specifically the least-squares method. By modeling the noisy price graph as a linear system, we can find the best-fit line that minimizes the sum of squared differences between the observed prices and the estimated values. This line serves as the denoised representation of the original price graph.

To implement the least-squares method, the following steps were taken:

1. Preprocessing
2. Matrix Formulation
3. Solving the System
4. Denoising

## Result

In the graphs below, the blue graph is the original Bitcoin price chart and the red graph is its denoised graph.

1. It is well de-noised (λ=100):
About the best approximation is when sqrt_lambda(landa radical) is equal to 10.

![sqrt_lambda=10](https://github.com/negarK2000/AppliedLinearAlgebra/blob/master/Denoising/1.png)

2. It is too denoised (λ>100):
The following diagram is for sqrt_lambda = 20.

!sqrt_lambda=20](https://github.com/negarK2000/AppliedLinearAlgebra/blob/master/Denoising/2.png)

We can see that the accuracy of the graph has decreased.

3. The diagram below is for sqrt_lambda = 100:

![sqrt_lambda=100](https://github.com/negarK2000/AppliedLinearAlgebra/blob/master/Denoising/3.png)

We can see that the graph has reduced its fluctuations so much that it has completely lost its original shape.

4. It is not well de-noised (λ<100):
The following diagram is for sqrt_lambda = 5.

![sqrt_lambda=5](https://github.com/negarK2000/AppliedLinearAlgebra/blob/master/Denoising/4.png)

We can see that the graph noise has increased.

The denoising process successfully removes the noise from Bitcoin's price graph, providing a clearer depiction of the underlying price trends. By minimizing the squared differences between the observed prices and the estimated values, the least-squares method effectively filters out the short-term fluctuations and emphasizes the long-term patterns.

5. The following diagram is for sqrt_lambda = 1:

![sqrt_lambda=1](https://github.com/negarK2000/AppliedLinearAlgebra/blob/master/Denoising/5.png)

We can see that the de-noised graph is almost identical to the original graph.

## Acknowledgments:

I would like to express my gratitude to the Teaching Assistants (TAs) of the Linear Algebra course who inspired and guided me in the development of this project.
