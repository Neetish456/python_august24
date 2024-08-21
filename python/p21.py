#porblem statement : Write a program to draw a hollow square.
side = int(input("Enter the side of the square : "))

for i in range(1,side+1):
    for j in range(1,side+1):
          if (j==1 or j==side or i == 1 or i == side):
                print("        *       ",end=" ")
          else:
                print("                ",end=" ")
    print(" ")

