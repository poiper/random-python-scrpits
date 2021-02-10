# Author : @poiper 
# patch version : 0.0.1
import sys, time, pyautogui
def sumthing():
  flag = 0
  while flag < 1:
   x = input("[?] would you like the typer to begin y/n : ")
   if x == 'y':
    y = input("[?] are you sure ? y/n : ")
    if y == 'y':
        animation = ['[!] starting in : 5 ','[!] starting in : 4 ','[!] starting in : 3 ','[!] starting in : 2 ','[!] starting in : 1 ','[!] starting now     ']
        for i in range(len(animation)):
          time.sleep(1)
          sys.stdout.write("\r" + animation[i % len(animation)])
          sys.stdout.flush()
        print("\n")
        time.sleep(1)
        f = open('example.txt','r')
        for word in f:
          pyautogui.typewrite(word)
          pyautogui.press('enter')
        flag = flag + 1
    if y == 'n':
       z = input("[?] would you like the program to exit y/n ? : ")
       if z == "y":
         input("[!] the program will now exit press enter to continue . . .")
         exit()
       if z == "n":
         pass   
   if x == 'n':
      p = input("[?] would you like the program to exit y/n ? : ")
      if p == "y":
         input("[!] the program will now exit press enter to continue . . .")
         exit()
      if p == "n":
         pass
sumthing()
print("[!] done !!")