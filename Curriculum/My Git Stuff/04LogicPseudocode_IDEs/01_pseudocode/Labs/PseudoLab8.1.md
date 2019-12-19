# Choose Two additional Programming Projects along with the (Mandatory) one. (Three Total) 

##  Payroll Program with Input Validation


Design a payroll program that prompts the user to enter an employee’s hourly pay rate and the number of hours worked. Validate the user’s input so that only pay rates in the range of $7.50 through $18.25 and hours in the range of 0 through 40 are accepted. The program should display the employee’s gross pay.

## Theater Seating Revenue with Input Validation

A dramatic theater has three seating sections, and it charges the following prices for tickets in each section: section A seats cost $20 each, section B seats cost $15 each, and section C seats cost $10 each. The theater has 300 seats in section A, 500 seats in section B, and 200 seats in section C. Design a program that asks for the number of tickets sold in each section and then displays the amount of income generated from ticket sales. The program should validate the numbers that are entered for each section.

```
Module main()

	Declare 
	Integer seatCountA, totalA, seatCountB, totalB, seatCountC, totalC, totalAll
	Constant integer COSTA = 20
	Constant integer COSTB = 15
	Constant integer COSTC = 10
	Constant integer SEATA = 300
	Constant integer SEATB = 500
	Constant integer SEATC = 200

	seatCountA()
	seatCountB()
	seatCountC()
	totalCount()

Module End

Module seatCountA()
	Display "Please input the number of tickets sold in section A"
	Input seatCountA
	If seatCountA > SEATA OR seatCountA < 0  Then
		Display "Input the correct number of seats sold for section A."
		Input seatCountA
	End If

	Set totalA = seatCountA * COSTA
	Display "Here is the profit from section A", totalA

	Return
End Module

Module seatCountB()
	Display "Please input the number of tickets sold in section B"
	Input seatCountB
	If seatCountB > SEATB OR seatCountB < 0 Then
		Display "Input the correct number of seats sold for section B."
		Input seatCountB
	End If

	Set totalA = seatCountA * COSTB
	Display "Here is the profit from section B", totalB

	Return
End Module

Module seatCountC()
	Display "Please input the number of tickets sold in section A"
	Input seatCountA
	If seatCountC > SEATC OR seatCountC < 0  Then
		Display "Input the correct number of seats sold for section A."
		Input seatCountA
	End If

	Set totalC = seatCountC * COSTC
	Display "Here is the profit from section C", totalC

	Return
End Module

Module totalCount()

	Set totalAll = totalA + totalB + totalC

	Display "Here is the total amount of money made from ticket sales:", totalAll

	Return

End Module
```
## Fat Gram Calculator

Design a program that asks for the number of fat grams and calories in a food item. Validate the input as follows:

Make sure the number of fat grams and calories is not less than 0.

According to nutritional formulas, the number of calories cannot exceed "fat grams X 9 "

Make sure that the number of calories entered is not greater than "fat grams X 9"

Once correct data has been entered, the program should calculate and display the percentage of calories that come from fat. Use the following formula:

![image](https://user-images.githubusercontent.com/47218880/67504468-0ba93a80-f64f-11e9-85d0-f080ac66a64a.png)

Some nutritionists classify a food as “low fat” if less than 30 percent of its calories come from fat. If the results of this formula are less than 0.3, the program should display a message indicating the food is low in fat.
```
Module main()

	Declare integer fatGrams, fat9
	Declare real calories, fatCalories

	Display "Please put in the number of fat grams and calories in your food"
	Display "Input fat grams now"
	Input fatGrams

	While fatGrams < 0 
		Display "Enter a valid number of fat grams"
		Input fatGrams
	End While

	Set fat9 = fatGrams * 9

	Display "Please put in the number of calories in your food"
	Input calories

	While calories < 0 OR calories < fat9
		Display "Enter a valid number of calories:
		Input calories
	End While

	Set fatCalories = fat9 / calories

	Display "Your food is", fatCalories * 100, "percent fat"

	If fatCalories < 0.3 then
		Display "Your food is low in fat!"
	Else
		Display "Your food is fatty, fatty."
	End If

End Module

```


## Speeding Violation Calculator

Design a program that calculates and displays the number of miles per hour over the speed limit that a speeding driver was doing. The program should ask for the speed limit and the driver’s speed. Validate the input as follows:

The speed limit should be at least 20, but not greater than 70.

The driver’s speed should be at least the value entered for the speed limit ­(otherwise the driver was not speeding).
Once correct data has been entered, the program should calculate and display the number of miles per hour over the speed limit that the driver was doing.

```
Module main()

	Declare integer speedLimit, spdrSpd, diff

	Display "Enter the speed limit"
	Input speedLimit

	While speedLimit < 20 OR speedLimit >70

    	Display "Please enter a valid speed limit between 20 and 70"
    	Input answer

	End While

	Display "Enter the speed of the speeder"
	Input spdrSpd

	While spdrSpd <= speedLimit

		Display "The speed limit was", speedLimit, "Please enter a speeding speed"
		Input spdrSpd

	End While

	Set diff = spdrSpd - speedLimit
	Display "Your speeder was doing", diff, "over the speed limit."

End Module
```

# Rock, Paper, Scissors Modification (MANDATORY)

In a previous Programming Exercise option you were asked to design a program that plays the Rock, Paper, Scissors game. In the program, the user enters one of the three strings—"rock", "paper", or "scissors"—at the keyboard. Add input validation (with a case-insensitive comparison) to make sure the user enters one of those strings only.
(If you didnt design one, here is a version of that game program to work with) 

### Program "Rock,Paper,Scissors"

```
// main module
Module main()
// Local variables
Declare Integer computer, player

// Get computer number
Set computer = Rand(1, 3)

// Get player number
Call getNumber(player)

// Show winner
Call showWinner(computer, player)

End Module

// The getNumber module gets an integer
Module getNumber(Integer Ref inputAnswer)
		Display “Enter rock, paper, scissors:  “
		Input inputAnswer

		While toLower(inputAnswer) != "rock" AND toLower(inputAnswer) != "paper" AND toLower(inputAnswer) != "scissors"
   			Display "Please answer 'rock', 'paper', or 'scissors'."
   			Input inputAnswer
		End While

		If toLower(inputAnswer) == rock Then
			Set inputAnswer = 1
		Else
			If toLower(inputAnswer) == paper Then
				Set inputAnswer = 2
			End If
		Else
			If toLower(inputAnswer) == scissors Then
				Set inputAnswer = 3
			End If
		
		End If
End Module

// The showWinner module shows if number is a prime
Module showWinner(Integer computer, player)
Declare Integer which

Display “Computer chose “, whichChoice(computer)
If computer == player Then
	Display “Player made same choice.  Play again.”
Else
Set which = whoWon(computer, player)
If which == 1 Then
		Display “Computer wins.”
Else
If which == 2 Then
			Display “Player wins.”
		Else
			Display “No winner.”
		End If
End If
End If

End Module

// The whichChoice function displays choice 
Function String whichChoice (Integer number)

If number == 1 Then
	Return “rock”
Else
If number == 2 Then
		Return “paper”
	Else
		Return “scissors
	End If

End Function

// The whoWon function selects winner 
Function Integer whoWon(computer, player)
// 1 = rock, 2 = paper, 3 = scissors
// rock smashes scissors
// scissors cuts paper
// paper wraps rock

	// both choose same no winner
If computer == player then
		Return 0
	End If

	// test computer chose rock
	If computer == 1 then
		If player == 2 then
			Return 2  // paper wraps rock
		End If
Else
		If player == 3 then
			Return 1  // rock smashes scissors
		End If
End If

	// test computer chose paper
	If computer == 2 then
		If player == 1 then
			Return 1  // paper wraps rock
		End If
Else
		If player == 3 then
			Return 2  // scissors cuts paper
		End If
End If

	// test computer chose scissors
	If computer == 3 then
		If player == 1 then
			Return 2  // rock smashes scissors 
		End If
Else
		If player == 2 then
			Return 1  // scissors cuts paper
		End If
End If

	Return 0

End Function
```
