|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---
### Performance Lab 3 options**

Assume that you have created a mechanical robot that can perform the following tasks: 
* Stand up
* Sit down
* Turn left 90 degrees
* Turn right 90 degrees
* Take a step 

*Additionally, the robot can determine the answer to one test condition:   Am I touching something? 

* Place two chairs 20 feet apart, directly facing each Other. Draw a structured flowchart or write pseudocode describing the logic that would allow the robot to start from a sitting position in one chair, cross the room, and end up sitting in the other chair. Have a fellow student act as the robot and Carry out your instructions

* Draw a structured flowchart or write pseudocode describing the logic that would allow the robot to start from a sitting position in one chair, stand up and circle the chair, cross the room, circle the other chair, return to the first chair, and sit. Have a fellow student act as the robot and carry out your instructions
  
---

* Assume that you want to look up logic. You might open the dictionary to a random page and see juice. You know this word comes alphabetically before logic, so you flip forward and see lamb. That is still not far enough, so you flip forward and see monkey. You have gone too far, so you flip back, and so on. Draw a structured flowchart or write pseudocode that describes the process of looking up a word in a dictionary. Pick a word at random and have a fellow student attempt to carry out your instructions. 

* Draw a structured flowchart or write structured pseudocode describing how to decide what college to attend. Include at least two decisions and two loops.

---

**Find the Problem**

* The intended purpose of the following module is to set the temp parameter to the value 32.0 if it is not already equal to 32.0. This will not work as the programmer expects.  *Find the problem*

```
Module resetTemperatuze (Real Ref temp)
    If NOT temp == 32.0 Then
       set temp = 32.0 
    End If 
End Module 

```

---

* The intended purpose of the following module is to determine whether the value parameter is within a specified range. The module will not work. *Find the problem*

```

Module checkRange (Integer value, Integer lower, Integer upper)
    If value < lower AND value > upper Then 
       Display "The value is outside the range."
    Else
       Display "The value is with the range."
    End If 
End Module 

```

---

End of Performance Lab 3

---

|[Next Topic](/01_pseudocode/04_Decisions.md)|
|---|
