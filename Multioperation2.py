class Multioperation():
    def subfields():
        num1 = int(input("Enter number 1 for List Area of AI subfields"))
        if num1 == 1:
           print("Sub-Fields in AI area:\n Machine learning \n Neural networks \n Vision \n Robotics \n Speach processing \n Natural language processing")

    def oddeven():
        num1 = int(input("Enter a number"))
        if num1%2 ==0:
           print(f"{ num1 } is even number")
        else:
           print(f"{num1 } is odd number")
        
    def eligible():
      gender = input("Your Gender:")
      age = int(input("Your age"))
      if gender == 'male' and age>= 20:
          print("Eligiable")
      elif gender == 'male' and age <= 19:
          print("Not Eligiable")
      else:
          print("female")
          
    def percentage():
      sub1 = int(input("Subject1 = "))
      sub2 = int(input("Subject2 = "))
      sub3 = int(input("Subject3 = "))
      sub4 = int(input("Subject4 = "))
      sub5 = int(input("Subject5 = "))
      Tot = sub1 + sub2 + sub3 + sub4 +sub5
      per = ( sub1 + sub2 + sub3 +sub4 + sub5 )/5
      print(f"Total = { Tot }")
      print(f"percentage = { per }")
            
    def triangle():
         Hig = int(input("Height = "))
         bre = int(input("breadth = "))
         area = Hig * bre / 2
         print(f"Area formula: ( height * breadth )/2")
         print(f"Area of triangle:{ area }")
         Height1 = int(input("Height1 = "))
         Height2 = int(input("Height2 = "))
         Breadth = int(input("Breadth = "))
         perimeter = Height1 + Height2 + Breadth
         print(f"Perimeter formula: Height1+Height2+Breadth")
         print(f"Perimeter of Triangle:{ perimeter }")
         