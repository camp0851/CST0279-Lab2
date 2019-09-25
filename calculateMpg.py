#Import Library
import camp0851Library;

#Get Input
input1 = int(input('What is the amount you\'ve driven in miles? '));
input2 = int(input('How much gas have you used up in gallons? '));

#Print to Screen
print('Your MPG is ' + str(camp0851Library.calculateMpg(input1, input2)));