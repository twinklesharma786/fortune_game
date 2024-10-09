print("-------------Amazon Company----------")
print("Welcome to the Fortune Game!")

username = input("Enter the username: ")
empid = int(input("Enter the employee ID: "))
dept = input("Enter the department: ")
emailid = input("Enter the email ID: ")
post = input("Enter the post: ")

print(f"--------Username is: {username}----------")
print(f"----------Employee ID is: {empid}---------")
print(f"----------Department is: {dept}------------")
print(f"---------Email ID is: {emailid}---------")
print(f"---------Post is: {post}--------")

print("-----------------Fortune Game------------")
print("Enter a number between 1 and 7:")

if post == "DEO":
    num = int(input("Enter the number: "))
    if num == 1:
        print("You can go home after lunch.")
    elif num == 2:
        print("You have to register 10 databases on the website.")
    elif num == 3:
        print("Your work is complete before the lunch break.")
    elif num == 4:
        print("You can go on vacation.")
    elif num == 5:
        print("You have a lot of work to do. Before 3 PM, you have to complete 20 files.")
    elif num == 6:
        print("You have to update data of new employees and complete 40 files.")
    elif num == 7:
        print("Today is a holiday for you.")
    else:
        print("Invalid number.")

elif post == "INTERN":
    num = int(input("Enter any number: "))
    if num == 1:
        print("You have to conduct research, gather data, and analyze the data.")
    elif num == 2:
        print("You have to manage part of a project under the guidance of the supervisor.")
    elif num == 3:
        print("Your work is complete before the lunch break.")
    elif num == 4:
        print("You have to resolve client issues and handle service-related tasks today.")
    elif num == 5:
        print("You have to assist with social media, create content, and update the website.")
    elif num == 6:
        print("You have to update data for new projects.")
    elif num == 7:
        print("Today is a holiday for you.")
    else:
        print("Invalid number.")

elif post == "HR":
    num = int(input("Enter any number: "))
    if num == 1:
        print("You have to conduct interviews of 50 employees and finalize 20 for the job.")
    elif num == 2:
        print("You have to conduct employee surveys and feedback sessions.")
    elif num == 3:
        print("You have to identify training needs and organize desktop training programs.")
    elif num == 4:
        print("You have to organize workshops, seminars, and professional development opportunities.")
    elif num == 5:
        print("You have to conduct salary reviews and manage payroll.")
    elif num == 6:
        print("You have to handle employee documentation and reporting.")
    elif num == 7:
        print("Today is a holiday for you.")
    else:
        print("Invalid number.")

else:
    print("No specific tasks for this post.")
