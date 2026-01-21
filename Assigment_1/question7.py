# Question 7 (1 Point): Time Conversion Function
#------------------------------------------------------------------------
"""
Write a function that converts a given number of seconds since midnight into:
• Hours
• Minutes
• Seconds
• AM or PM
The function should return a formatted string. If the input is invalid, return an appropriate
message.
"""
def convert_seconds_to_time(total_seconds):
   
    seconds_in_a_day = 86400
    if total_seconds < 0 or total_seconds >= seconds_in_a_day:
        return "Enter a number of seconds between 0 and 86399."
    
    if type(total_seconds) != int and type(total_seconds) != float:
        return "Enter a numeric value for seconds."
    
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    seconds_until_noon = 43200

    if total_seconds < seconds_until_noon:
        period = "AM"
    else:
        period = "PM"
    
    if period == "PM" and hours > 12:
        hours -= 12
    elif period == "AM" and hours == 0:
        hours = 12
    # 5 17 47 AM
    hours_string = f"{hours} {minutes} {seconds} {period}"
    return hours_string

print(convert_seconds_to_time(50_000))  