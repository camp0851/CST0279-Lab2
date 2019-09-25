#Import Library
import camp0851Library;

#Get Inputs
input1 = int(input('Enter the first coordinate X -> '));
input2 = int(input('Enter the first coordinate Y -> '));
input3 = int(input('Enter the second coordinate X -> '));
input4 = int(input('Enter the second coordinate Y -> '));

#Print to Screen
print('The distance between coordinates ({},{}) and ({},{}) is {}'.format(input1, input2, input3, input4, camp0851Library.calculateDistanceBetweenPoints(input1, input2, input3, input4)));