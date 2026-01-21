# Question 5 (1 Point): Circle Area Comparison with Validation
#------------------------------------------------------------------------
"""
Write a function that takes the radii of two circles and performs the following:
• Validates that both radii are positive integers.
• Computes the area of each circle.
• Returns the percentage of the larger circle’s area that can be covered by the smaller circle.
If invalid input is provided, return a meaningful message instead of performing the calcula-
tion.
"""
import math

def circleAreaCoverage(radiusOfCircle1,radiusOfCircle2):
    if radiusOfCircle1 < 0 and radiusOfCircle2 <0:
        if radiusOfCircle1 < 0:
            return 'the first radious you are analysing is not positive'
        elif radiusOfCircle2 < 0:      
            return 'the second radious you are analysing is not positive'
        else:       
            return 'the raddii you are analysing are not positive'
    else:
        area_circle_1 = radiusOfCircle1 ** 2 * math.pi
        area_circle_2 = radiusOfCircle2 ** 2 * math.pi
        if area_circle_1 > area_circle_2:
            percentage_circle2 = (area_circle_2 / area_circle_1) * 100
            return f'The percentage of circle 2 area that can be covered by circle 1 is {percentage_circle2} %'
        else:
            percentage_circle1 = (area_circle_1 / area_circle_2) * 100
            return f'The percentage of circle 1 area that can be covered by circle 2 is {percentage_circle1} %'
        
print(circleAreaCoverage(3,5))