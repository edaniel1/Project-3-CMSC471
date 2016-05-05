This ReadMe explains how to run the program edaniel1Proj3.1.py

DISCLAIMER: The program does not have perfect accuracy (sadly)

1) All training data should be in a subdirectory of "../TESTING", 
		which is relative to where the program is.
2) "../TESTING" should only include 5 folders (01, 02, 03, 04, 05).
3) The 5 folders should include the following testing data:
		Folder "01": Testing data for the Smile label
		Folder "02": Testing data for the Hat label
		Folder "03": Testing data for the Hash label
		Folder "04": Testing data for the Heart label
		Folder "05": Testing data for the Dollar label
4) All user input for the program is through command line arguments. To set up the SVM,
		run the program with the command line argument "Setup". Be aware of capitalization,
		and do not include the double quotes. The program will print "Setup Complete" when finished.
5) The program can now be run. Give the program the file path of an image which the program
		should identify as one of the labels (as a command line argument).
6) If the training data set did NOT change, then return to step 5. If the training set changed,
		return to step 4.
