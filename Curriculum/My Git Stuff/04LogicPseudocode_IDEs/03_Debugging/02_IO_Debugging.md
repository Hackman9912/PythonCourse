|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---

## Print() Debugging

---

**Objectives**

This topic provides the student with knowledge and skills on:

*  **print() debugging concepts**

* **How to print() debug**
  * **Pre Checks**
  * **Five steps of debugging print()**

---

In this topic we're going to review the method for **print() Debugging**. 

**Note:** print() is often overlooked by modern debugging tools, but is still a proven and indispensable method of debugging.** 

**To debug using print()**

* Print variables, outputs, etc. to see if the data meets your expecations. 

**Recall `step 4: analyze snapshot`: Using print(), we can test all of the things we think to be true** 

**Example:** A value should be 5, a return should be at this pointer, this condition should be true, As code is found that does not meet our expectations, we can begin to formulate **why** and **how**. 

---

**How to print() Debug**

* Initially we have a few things we need to identify prior to stepping through the debugging process. These Pre-checks will help us to analyze what happened to our program.  We start off by asking a few questions:

**Pre-Checks**

**What is the program's purpose?**

* It's a simple calculator with add, subtract, multiply and division. The program continues to run until user tells it to stop. 

**What did we expect to happen?**

* We expected that a user would select what kind of operation they wanted to do. 
  * If they selected something wrong, the prompt would appear again asking for selection. 
  * If they selected correctly, it would then route the user to the correct function.  The function would ask for two numbers to perform some sort of math at that point.  The value would then be returned and printed. Lastly, the program would ask if the user wants to continue. (Loop the program)**

**What really happened?**

  * ???

**What should of happened?**

  * Same as what we expected to happen

---
**5 Steps to debugging**

* Now that we have answered a few preliminary questions, Let's begin debugging by walking through our `print_demo, We can do this by going through step by step. 

---

**Step One:** Can we reproduce this issue? 

This step is the same as reviewed during our introduction.

* What are some ways you can reproduce a bug?
* Why is this important?

---

**Step Two: Describe the Bug**

Again follow the guide from the introduction topic.

* Is it reproduceable?
* How can you make it happen again?
* What happened?
* What should of happened?
* Is it correct sometimes?
* When did it happen?
* What can support this?
* How critical is it?

---

**Step Three: Snapshot**

For print(), taking a snapshot is fairly simple. Unlike other methods, we aren't going to take a legit snapshot. Instead, we narrow down the area of where the issue occurred and debug that portion. 

**Let's take a look at the example:**

* Where does the code first break in this program? 
* What should we print out? 
* Let's capture that data and move on.

---

**Step Four: Analyze Snapshot**

Let's take a look at the data we did gather though:

* Did the values meet our expectations? ex:
  * We have a while loop, was it's exit condition met?
  * Were the switch case conditions met?
  * Did the if statement meet our expectations?

If a condition isn't being met as expected; did we set that condition up correctly? If so, why isn't the condition being met? How can we make it behave as expected?

---

**Step Five: Step 5: Fix the Bug**

Once the bug has been identified, it is time to fix it. 

* What is the fix?
* Now that the bug is identified, fix it, and recheck.

---

|[Next Topic](/03_Debugging/04.3_VSCode_Debugging.md)|
|---|
