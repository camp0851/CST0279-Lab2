#calculateAreaOfCircle
def calculateAreaOfCircle(radius):
    from math import pi;
    area = pi * radius ** 2;
    return area;

#calculateMpg
def calculateMpg(miles, gallon):
    milesPerGallon = miles / gallon;
    return milesPerGallon;

#calculateFahrenheitToCelsius
def calculateFahrenheitToCelsuis(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9;
    return celsius;

#calculateDistanceBetweenPoints
def calculateDistanceBetweenPoints(x, y, x1, y1):
    pointOne = x + y;
    pointTwo = x1 + y1;
    distance = pointOne - pointTwo;
    return distance;