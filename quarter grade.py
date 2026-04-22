my_tentative_quarters = ["q1", "q2", "q3", "q4"]

for quarter in my_tentative_quarters:
    sa1 = float(input("Enter your SA1 score: "))
    sa2 = float(input("Enter your SA2 score: "))
    final_sa = float(((sa1 + sa2)/2)*.7)

    fa1 = float(input("Enter your FA1 score: "))
    fa2 = float(input("Enter your FA2 score: "))
    final_fa = float(((fa1 + fa2)/2)*.3)
    quarter = float(final_sa + final_fa )
    print("Your final grade for this quarter is: ", quarter)

final_q2= float((q1 + (q2 * 2))/3)
final_q3= float((q1 + q2 + q3)/3)
final_q4 = float((q2 + q3 + q4)/3)


def grade_status(final_average):
    if final_average >= 96 and final_average <= 100:
        return  "1.00"
        return "EXCELLENT!"
    elif final_average >= 90 and final_average <= 95.99:
        return "1.25"
        return "VERY GOOD!"
    elif final_average >= 84 and final_average <= 89.99:
        return "1.50"
        return "VERY GOOD!"
    elif final_average >= 78 and final_average <= 83.99:
        return "1.75"
        return "GOOD!"
    elif final_average >= 72 and final_average <= 77.99:
        return "2.00"
        return "GOOD!"
    elif final_average >= 66 and final_average <= 71.99:
        return "2.25"  
        return "SATISFACTORY!"
    elif final_average >= 60 and final_average <= 65.99:
        return "2.50"
        return "SATISFACTORY!"
    elif final_average >= 55 and final_average <= 59.99:
        return "2.75"
        return "FAIR!"
    elif final_average >= 50 and final_average <= 54.99:
        return "3.00" 
        return "FAIR!"
    elif final_average >= 40 and final_average <= 49.99:
        return "4.00"
        return "FAILED ON CONDITION!"
    else:
        return "5.00"
        return "FAILED!"    