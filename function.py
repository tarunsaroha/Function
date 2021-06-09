# def ask_question():
#     print("baar")
#     print("baar")
#     print("baar")
# ask_question()


# def ask_question():
#     i=1
#     while i<=100:
#         print("baar")
#         i=i+1
# ask_question()


# numbers = [3, 5, 7, 34, 2, 89, 2, 5] 
# def max():
#     b=numbers[0]
#     i=0
#     while i<len(numbers):
#         if numbers[i]>b:
#             b=numbers[i]
#         i=i+1
#     print(b)
# max()            



# numbers = [1, 2, 3, 4, 5] 
# def sum():
#     i=0
#     sum=0
#     while i<len(numbers):
#         sum=sum+numbers[i]
#         i=i+1
#     print(sum)
# sum()


# diconary
# i=0
# while i<10:
#     student=int(input("enter the number of student"))
#     kharcha=int(input("enter the student of kharcha"))
#     if student<50000:
#         print("budug ke ander hai")
#     else:
#         print("budget ke ander nahi hai")
#     i=i+1        




# a=[6, 8, 4, 3, 9, 56, 0, 34, 7, 15]   
# def sort():
#     print(sorted(a))
# sort()    





# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# def revers():
#     k=[]
#     i=1
#     while i<=len(reverse_list):
#         k.append(reverse_list[-i])
#         i=i+1
#     print(k)
# revers()        



 
# list1 = [8, 6, 4, 8, 4, 50, 2, 7]
# def min():
#     b=list1[0]
#     i=0
#     while i<len(list1):
#         if list1[i]<b:
#             b=list1[i]
#         i=i+1
#     print(b)
# min()            




# def sum():
#     print(12+13)
# sum()




# def welcome():
#     print("Welcome to function")
# welcome()





# def num():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number") 
# num()




# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print (max(numbers_list)) 




# a=[1,2,3,4,5,6]
# print(len(a))




# def say_hello(name):
#     print ("Hello ", name)
#     print ("Aap kaise ho?")
# say_hello("Aatif") 



 
# def add_numbers(number1, number2):
#     print ("Main do numbers ko add karunga.")
#     print (number1 + number2)
# add_numbers(120, 50)
# num_x = 134
# name = "Rinki"
# add_numbers(num_x, name)



 
# def say_hello_people(name_x, name_y, name_z, name_a):
#     print ("Namaste ", name_x) # hindi mein
#     print ("Alah hafiz ", name_y) # urdu mein
#     print ("Bonjour ", name_z) # french mein
#     print ("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev") 




 
# def icecream(*flavours):
#  for flavour in flavours:
#   print("i love"+flavour)

# icecream("chocolate", "butterscotch","vanilla","strawberry") 



 
# def attendance(name,status="absent"):
#     print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh") 




# def greet(*names):
#     for name in names:
#         print("Welcome",name)
# greet("Rinki", "Vishal", "Kartik", "Bijender")



# def info(name, age="10"):
#    print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18") 



# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)

# studentDetails("Nilam","loop",("Hello " , "name", "your" , "currentMilestone", "concept " , "is clear with the help of ", "mentorName"))
    


# def my_function():
#   print("Hello from a function") 
# my_function()




# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus") 
# my_function("apple")




# def my_function(fname, lname):
#   print(fname + " " + lname)
# my_function("Emil", "Refsnes")





# def my_function(*kids):
#   print("The youngest child is " + kids[2])
# my_function("Emil", "Tobias", "Linus") 





# def my_function(**kid):
#   print("His last name is " + kid["lname"])
# my_function(fname = "Tobias", lname = "Refsnes") 




# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")




# def my_function(country = "Norway"):
#   print("I am from " + country)
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil") 
# my_function("delhi")



# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum
#




# def add_numbers_print(number_x, number_y):
#     number_sum = number_x + number_y
#     print (number_sum)
# sum4 = add_numbers_print(4, 5)
# print (sum4)
# print (type(sum4)) 




# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print ("Hello from NavGurukul ;)")
#     return number_sum
#     number_sum = number_x + number_x
#     print ("Kya main yahan tak pahunchunga?")
#     return number_sum
# sum6 = add_numbers_more(100, 20)




# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"

#     print ("Kya main print ho payungi? :-(")

# mon_menu = menu("monday")
# print (mon_menu)
# tues_menu = menu("tuesday")
# print (tues_menu)
# fri_menu = menu("friday")
# print (fri_menu) 



# def f1():
#    s = "I Love Navgurukul"
#    def f2():
#        print(s)
#    f2()
# f1() 




# def first_function():
#     s = 'I love India'
#     def second_function():
#         print(s)     
#     second_function()
# first_function()




# def add(a,b):
#     c=a+b
#     print("add=",c)
# add(4,3)




 
# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print (max(numbers_list))


# def add_numbers(number1, number2):
#     print ("Main do numbers ko add karunga.")
#     print (number1 + number2)
# add_numbers(120, 50)
# num_x = 134
# name = "Rinki"
# add_numbers(num_x, name)



# def say_hello_people(name_x, name_y, name_z, name_a):
#     print ("Namaste ", name_x) # hindi mein
#     print ("Alah hafiz ", name_y) # urdu mein
#     print ("Bonjour ", name_z) # french mein
#     print ("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")





# def add():
#     a=2
#     b=4
#     c=a+b
#     print(c)
# add()



# def add(y):
#     a=2
#     c=a+y
#     print(c)
# add(23)



# def print_lines():
#     print("mera name rishab hai","mai navgurukul ka co-founder hu")
# print_lines()



# def add(num1,mun2):
#     num1 = 56
#     num2 = 12
#     num3=num1+num2
#     print(num1+num2)
# add(56,12)




# def employee(name,salary=20000):
#         print(name,"your salary is:-",salary)

# employee("kartik",30000)
# employee("deepak") 



 
# def primeorNot(num):     
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")

#     else:
#            print(num,"is not a prime number")
# primeorNot(406)





# def greet(*names):
#     for name in names:
#                print("Hello", name)
# greet("sonu", "kartik", "umesh", "bijender")






# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#     return sum

# print(sumofdigits(123))






# def  meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner"    :
#             return "veg-chapati"
#         else :
#             return "time not found"
# print(meal("sunday","lunch"))_multi
# print(meal("monday","dinner"))

#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "aloo 






# # def vate():
# #     num=int(input("enter the number"))
# #     if num>18:
# #         print("elible")
# #     else:
# #         print("elible not")
# # vate()    




# num=int(input("enter the num"))
# list=[1,2,3,4]
# i=0
# a=[]
# while i<=num:
#     if list==0:
#         a.append(list)
#     print(a)
#     i=i+1



# def n(name):
#     a=name.split()
#     i=len(a)-1
#     while i>=0:
#         print(a[i],end=" ")
#         i=i-1
#     return
# n("tarun saroha")






# a = 10
# if a * 2 == 20:
#    print ("a variable ko 2 se multiply kar ke 20 aata hai")
# else:
#    print ("Nah! a variable ko 2 se multiply kar ke 20 nahi aata.") 



# counter = 1
# while counter < 100:
#     print ("The counter is" + str(counter))
#     counter = counter + 1
#     print ('--------') 


