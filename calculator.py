from pyscript import document, display

def grading_system(e):

    # STRING VARIABLES FOR NAME AND SECTION THROUG ID FROM CALCULATOR.HTML
    firstname = document.getElementById("firstname").value
    middlename =  document.getElementById("middlename").value
    lastname = document.getElementById("lastname").value
    level = document.getElementById("level").value
    section = document.getElementById("section").value

    # FLOAT VARIABLES FOR GRADE CALCULATION THROUGH ID FROM CALCUATOR.HTML
    num1 = float(document.getElementById("num1").value)
    num2 = float(document.getElementById("num2").value)
    num3 = float(document.getElementById("num3").value)
    num4 = float(document.getElementById("num4").value)
    num5 = float(document.getElementById("num5").value)
    num6 = float(document.getElementById("num6").value)
    num7 = float(document.getElementById("num7").value)
    num8 = float(document.getElementById("num8").value)
    num9 = float(document.getElementById("num9").value)
    num10 = float(document.getElementById("num10").value)
    num11 = float(document.getElementById("num11").value)

    # CALCULATES THE AVERAGE OF THE 11 SUBJECTS IN JUNIOR HIGH SCHOOL
    average = (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11)/11
    document.getElementById("average").innerText = "Your general weighted average is " + f"{average:.2f}"

    # DISPLAYS THE NAME AND SECTION OF THE STUDENT TO CALCUATOR.HTML
    document.getElementById("studentname").innerHTML = '{} {} {} {}'.format("Name:",  firstname, middlename, lastname) # DISPLAYS STUDENT NAME
    document.getElementById("studentsection").innerHTML = '{} {} {} {}'.format("Section:",  level, "-", section) # DISPLAYS STUDENT GRADE LEVEL AND SECTION 

    # LISTS AND TUPLES FOR SUBJECT VERIFICATION
    subject = [
        "Math:", 
        "Science:", 
        "English:",
        "Filipino:", 
        "Social Studies:", 
        "Values Education:", 
        "Information & Communications Technology:", 
        "Technology & Livelihood Education:", 
        "Music & Arts:", 
        "Physical Education & Health:", 
        "Leadership/Citzenship Advancement Training:"
    ] 
    grade = ("Error ⁉️", "Passed ✔️", "Failed ✖️") # THIS TUPLE CANNOT BE MODIFIED.

    # DISPLAY SUBJECT NAME AND GRADE VALUE WHEN IT IS FROM 0 to 100
    document.getElementById("sub1").innerHTML = '{} {}'.format(subject [0], num1)
    document.getElementById("sub2").innerHTML = '{} {}'.format(subject [1], num2)
    document.getElementById("sub3").innerHTML = '{} {}'.format(subject [2], num3)
    document.getElementById("sub4").innerHTML = '{} {}'.format(subject [3], num4)
    document.getElementById("sub5").innerHTML = '{} {}'.format(subject [4], num5)
    document.getElementById("sub6").innerHTML = '{} {}'.format(subject [5], num6)
    document.getElementById("sub7").innerHTML = '{} {}'.format(subject [6], num7)
    document.getElementById("sub8").innerHTML = '{} {}'.format(subject [7], num8)
    document.getElementById("sub9").innerHTML = '{} {}'.format(subject [8], num9)
    document.getElementById("sub10").innerHTML = '{} {}'.format(subject [9], num10)
    document.getElementById("sub11").innerHTML = '{} {}'.format(subject [10], num11)

    # DISPLAY ERROR WHEN GRADE VALUE IS BELOW 0 OR EXCEED 100
    if not (0 <= num1 <= 100 
            and 0 <= num2 <= 100 
            and 0 <= num3 <= 100 
            and 0 <= num4 <= 100 
            and 0 <= num5 <= 100 
            and 0 <= num6 <= 100 
            and 0 <= num7 <= 100 
            and 0 <= num8 <= 100 
            and 0 <= num9 <= 100 
            and 0 <= num10 <= 100
            and 0 <= num11 <= 100):
        
        document.getElementById("average").innerText = "Input is undefined. Please enter values from 0 to 100."
        document.getElementById("grade").innerText = (grade [0])
        return
    
    # CONDITIONAL STATEMENT FOR PASSING GRADE
    if average >= 75:
        document.getElementById("grade").innerText = (grade [1])
        return
    
    # CONDITIONAL STATEMENTS FOR FAILING GRADE
    if average < 75:
        document.getElementById("grade").innerText = (grade [2])
        return
    