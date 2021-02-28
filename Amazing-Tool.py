import os,sys,time
os.system("clear")
os.system("xdg-open https://youtube.com/c/SLPhoneTechnician")
os.system("toilet -f mono12 -F border Tool")
print('\033[1;31m'"______________________________________________")
print("                                                                                "
print('\033[1;32m'"Choose an option")
print("                              ")
print('\033[1;31m'"            1)Clock")
print('\033[1;31m'"            2)Tool Uninstaller")
print('\033[1;31m'"            3)SMS Sender")
print('\033[1;31m'"            4)Calculator")
print('\033[1;31m'"            5)Exit                    ")
print("______________________________________________")
print(" ")
print('\033[1;32m'"press Ctrl+Z for exit any tool")
marks=int(input('\033[1;31m'"Enter number>>"))
if (marks==1):
        os.system("tty-clock -t -s")
elif (marks==2):
        os.system("mc")
elif (marks==3):
        os.system("python file1")
elif (marks==4):
        os.system("python file2")
elif (marks==5):
        os.system("exit")
        print("Good Bye")
elif (marks>=6):
        print("wrong option")
        os.system("python amazing-tool.py")