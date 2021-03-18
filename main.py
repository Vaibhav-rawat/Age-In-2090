'''Taking age or year from the user and tell them when they will turn 100 years old . 
And also providing them the functionality to check on particular year how old they will 
be.
Author - Vaibhav Rawat
Purpose - Python Problem Solving'''
try:
    age=int(input('Enter your age or year of birth\n'))
    agee=age
except ValueError:
    print('Sorry You have entered string ')
except:
    print('Unexpected error')
else:
    if age>2021:
        print('You are not born yet')
    elif age>1800 and age<=2021:
        print(f'You will turn 100 in {agee+100}')
    else:
        agee=(2021-age)
        print(f'You will turn 100 in {agee+100} years')
    print("\nDo you want to know your age in particular year?")
    while True:
        ans=input('Y or y for Yes \nN or n for No\n')
        if ans=='Y' or ans=='y':
            year=int(input('Enter the year\n'))
            if year<agee:
                print('You are entering year less than your actual DOB\n')
            else:
                print(f'You will be {year-agee} years old in the year {year}')
            break
        elif ans=='N' or ans=='n':
            print('Have a good day ')
            break
        else:
            print('Wrong input choose again\n')
