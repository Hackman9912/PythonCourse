# Algorithms Big O Notation

<a href="https://github.com/CyberTrainingUSAF/04-IDE-s-and-Algorithms-Pt.-1/blob/master/00-Table-of-Contents.md" rel="Return to TOC"> Return to TOC </a>


### For this lesson, we are going to discuss the Big O notation. Additionally, we will be going over pseudo-code and techniques used to help learn how to logically write code.


## Objectives

**During this topic the student will have a fundemental understanding on IDE setup and use to include the following.**
* **Big O Notation concepts**
* **Logarithms**
* **O(Log N)**

---

## Big O Notation

The Big O notation is used in Computer Science to describe the performance or complexity of an algorithm.
Big O specifically describes the worst-case scenario, and can be used to describe the execution time required or the space used (e.g. in memory or on disk) by an algorithm.

---

## Introduction

One of the best methods for understanding Big O thoroughly is through code examples.  So, to help you to understand it best; we have provided some common orders of growth along with descriptions and examples when possible.

---

## O(1)

O(1) describes an algorithm that will always execute in the same time (or space) regardless of the size of the input data set.

![](/assets/big_O_01.png)

---

## O(N)

O(N) describes an algorithm whose performance will grow linearly and in direct proportion to the size of the input data set.  The example below also demonstrates how Big O favours the workst-case performance scenarios; a matching string could be found during any iteration of the ***for loop*** and the function would return early, but Big O notation will always assume the upper limit where the algorithm will perform the maximum number of iterations.

![](/assets/big_O_02.png)

---

## O(N2)

O(N2) represents an algorithm whose performance is directly proportional to the square of the size of the input data set. The growth curve of an O(2N) function is exponential - starting off very shallow, then rising meteorically.  An example of an O(2N) function is the recursive calcualtion of Fibinacci numbers:

![](/assets/big_O_03.png)

---

## O(2N)

O(2N) denotes an algorithm whose growth doubles with each additon to the input data set. The growth curve of an O(2N) function is exponential - starting off very shallow, then rising meteorically. An example of an O(2N) function is the recursive calculation of Fibonacci numbers:

![](/assets/big_O_04.png)

---

## Logarithms

Logarithms are slighlty trickier to explain, so we will use a common example:
* **Binary Search** is a technique used to search sorted data sets. essentially the median, and compares it against a target value.
If the values match, it will return success.  
  * If the target value is higher than the value of the probe element, it will take the upper half of the data set and perform the same operation against it.
  * If the target value is lower than the value of the probe element, it will perform the operation against the lower half.  It will continue to halve the dataset with each iteration until the value has been found or until it can no longer split the data set.
  
* **Iterative halving** of data sets described in the binary search example produces a growth curve that peaks at the beginning and slowly flattens out as the size of the data sets increase e.g. an input data set containing 10 items takes one second to complete, a data set containing 100 items takes two seconds, and a data set containing 1000 items will take three seconds.

* **Doubling the size** of input data set has little effect on its growth as after a single iteration of the algorithms the data set will be halved and therefore on a par with an input data set half the size.  This makes algorithms like binary search extremely efficient when dealing with large data sets.

---

<a href="https://github.com/CyberTrainingUSAF/04-IDE-s-and-Algorithms-Pt.-1/blob/master/02_Agorithms_pt1/02_Algorithms_Practice.md" rel="Continue to Next Topic"> Continue to Next Topic </a>

