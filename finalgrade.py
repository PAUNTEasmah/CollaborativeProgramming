def grade_status(final_average):
        if final_average >= 96: return "1.00", "Excellent!"
        elif final_average >= 90: return "1.25", "Very Good!"
        elif final_average >= 84: return "1.50", "Very Good!"
        elif final_average >= 78: return "1.75", "Good!"
        elif final_average >= 72: return "2.00", "Good!"
        elif final_average >= 66: return "2.25", "Satisfactory!"
        elif final_average >= 60: return "2.50", "Satisfactory!"
        elif final_average >= 55: return "2.75", "Fair!"
        elif final_average >= 50: return "3.00", "Fair!"
        elif final_average >= 40: return "4.00", "Failed on Condition!"
        else: return "5.00", "Failed!"

previous_final = 0

tentative_list = [1, 2, 3, 4]
for q in [1, 2, 3, 4]:
    print(f"--- Quarter {q} ---")
    sa = (float(input("Enter your SA1 score: "))) + (float(input("Enter your SA2 score: ")))
    fa = (float(input("Enter your FA1 score: "))) + (float(input("Enter your FA2 score: ")))
    tentative = ((sa/2) * 0.7) + ((fa/2) * 0.3)
    if q == 1:
        current_final = tentative
    else: 
        current_final = (previous_final + 2 * tentative)/ 3

        previous_final = current_final

        numeric_grade, remarks = grade_status(current_final)
        print(f"Equivalent: {numeric_grade}")
        print(f"Status: {remarks}")


    print(f"QUARTER FINAL GRADE: {current_final:.2f}")

   



