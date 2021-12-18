==========
|README  |
==========

=== Each files =====
>_pycache_ - this is automatically produced when you execute the Main file.
 Ignore modifying it unless you know what you are doing.

>NumGen.py - Feel free to modifying the file. It basically produces a list of numbers for you to play around with.
 Executing the file might create a new file.

>quicksortWebAlgorithm - This algorithm was taken from CSDojo. Please check his youtube channel for more context
 On the algorithm. Note: We do not use this algorithm in our actual program.

>readFile.py - This file is an import file used to read the txt files of program. DO NOT REMOVE THIS IT IS AN IMPORTANT
 DEPENDENCY OF THIS PROGRAM.

>QuickSort.py - DO NOT REMOVE THIS FILE. This is the actual file used in the program for quicksorting.

>Main.py - This is the main Execution of the file. DO NOT REMOVE THIS FILE.

==================================================
>Onum - A file containing ordered numbered lists
	>Onum.txt (1,000,000+ items) will crash the program due to recursion limit |Note: You can change recursion limit, please be aware this may crash your computer potentially
	Copy this and insert it: Onum\Onum.txt

	>Onum2.txt (100,000 items) will crash the program due to recursion limit |Note: You can change recursion limit, please be aware this may crash your computer potentially
	Copy this and insert it: Onum\Onum2.txt

	>Onum3.txt (100 items) will not crash
	Copy this and insert it: Onum\Onum3.txt

	>Onum4.txt (10 items) will not crash
	Copy this and insert it: Onum\Onum4.txt

>Rnum - A file containing random number lists
	>Rnum.txt (460 items)
	Copy this and insert it: Rnum\Rnum.txt

	>Rnum.txt (10,000 items)
	Copy this and insert it: Rnum\Rnum2.txt

	>Rnum3.txt (100,000 items)
	Copy this and insert it: Rnum\Rnum3.txt

	>Rnum4.txt (1,000,000 items) <-------------------Will take the longest depending on hardware
	Copy this and insert it: Rnum\Rnum4.txt
	
==================================================

How QuickSorting works:

In an unordered list, quick sort  will pick a "Pivot point" this is usually the beginning or end or maybe somewhere in between. In our coding it is the beginning element. The pivot will act as a "grouping condition"

Any number less than the pivot will be on the left and anything more than the pivot is on the right. The way we swap values is using an incrementer denonted as i and decrementer j. i starts at the beginning and j starts at the end.

We increment and decrement i and j respectively, make element swaps when appropriate (Keyword: Elements of i and j, we do not swap positions of i and j!). Once i and j cross paths over the list, we swap the element of the pivot point with j.

Note: The pivot position where we made the swap is ABSOLUTE. This means when we swap j and pivot, pivot it is at the correct position. 

===== Partitioning and QuickSort method =======

>O_partitioning - It determines how to partition our list. Takes Parameter of a list[], starting position, and ending position.

>QuickSort - It uses O_partitioning recursively, it will exit recursion once certain parameters are met. This includes a list partitioned to a size of 1 or a size 2 list (we can make a simple comparison).

===============================================
Algorithmic Analysis and Big O notation

Best Case Scenario - O(n*log(n)) Linear Logarithm
Average Case Scenario - O(n*log(n)) Linear Logarithm
Worst Case Scenario - O(n^2) 2nd power/Quadratic <---------Happens if a list is already sorted, reverse order, most of the data are duplicates

Space complexity
Worst Case - O(n)

Final Note:
You can run the program using IDLE or other IDE software, or simply executing the Main.py
Also the program gives the time it takes for the completion at the end of the result.

>Contributors: Sidney K. Levine, Rezvee Rahman 


