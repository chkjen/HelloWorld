#first_number = float(input("Enter the first number: "))
#second_number = float(input("Enter the second number: "))
#result = first_number + second_number
#print("The sum is: " + str(result))

#course = "Python for Beginners"
#print("The index of the letter 'z' is: " + str((course.find("z"))))


#price = 25
#print(price > 10 and price < 30)

#temp = 35

#if temp > 30:
#   print("It's a really hot day today!")
#   print("Drink plenty of water")
#elif temp > 20:
#    print("It's a nice day today!")
#elif temp > 10:
#    print("It's a bit cold today.")
#else:
#    print("It's cold af outside.")
#print("Done")

#*****Weight conversion program excersize********
#Enter the weight
#ask if in (K)g or (L)b upper or lower
#it converts it to the opposite

#weight = float(input("Weight:"))
#x = input("Is that in (K)g or (L)bs? ")
#metric = x.upper()


#if metric == "L":
#    weight *= .45359237
#    print("Your weight is " + str(weight) +" Kg")
#elif metric == "K":
#    weight /= .45359237
#    print("Your weight is " + str(weight) +" Lbs")
#print("Done")


#i = 1
#while i <= 5:
#    print(i)
#    i += 1


#names = ["Chuck", "Bob", "Mosh", "Mary", "Sam"]
#names[2] = "Ricky"
#print (names[0:3])

#number = [1, 2, 3, 4, 5]

#for item in number:
#    print(item)

#for number in range(5):
#    print(number)

#numbers = (1, 2, 3)



#name = input("Enter your name: ")
#age = int(input("Enter your age: " ))
#weight = float(input("Enter your weight: "))
#convert = input("Is that in (K)g or (L)bs? ")

#converts the wight to lbs or leaves it as lbs depending on choice
#if convert.upper() == "K":
#   weight /= .453592
#   print ("Conversion completed on weight")
#else:
#    print ("No conversion needed on weight")

#reading info back via message
#print ("Hello %s. You are %s years old and weight %s Lbs." % (name, age, weight))

#appending the variable values to a list
#list_entry = []
#list_entry.append(str(name))
#list_entry.append(str(age))
#list_entry.append(str(weight))

#print(list_entry)

#numbers = [
#    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
#    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
#    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
#    743, 527
#]

#for number in numbers:
#    if number <= 237 and number % 2 == 0:
#        print(number)


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here

#car1 specs
car1 = Vehicle()
car1.name = "Fer"
car1.kind = "Convertible"
car1.color = "Red"
car1.value = 60000

#car2 specs
car2 = Vehicle()
car2.name = "Jump"
car2.kind = "Van"
car2.color = "Blue"
car2.value = 10000

# test code
print(car1.description())
print(car2.description())
