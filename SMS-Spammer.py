#!/usr/bin/python
import sys, os

# Restart ####################
def restart_program():
     python = sys.executable
     os.execl(python, python, * sys.argv)
     curdir = os.getcwd()
##############################
""" Coded By Allistar by Star Sec."""
os.system("clear")
print " "
print "\033[1;32;40m   ___   __  __   ___     ___                                             "
print "\033[1;32;40m  / __| |  \/  | / __|   / __|  _ __   __ _   _ __    _ __    ___   _ _   "
print "\033[1;32;40m  \__ \ | |\/| | \__ \   \__ \ | '_ \ / _` | | '  \  | '  \  / -_) | '_|. "
print "\033[1;32;40m  |___/ |_|  |_| |___/   |___/ | .__/ \__,_| |_|_|_| |_|_|_| \___| |_|    "
print "\033[1;32;40m                               |_|                                        "
print "\033[1;32;40m------------------------------------------------------------------------- "
print "  ===|[ SMS Spamer ]|===         "
print "  [01] Setup New Session         "
print "  [02] Spam From Contact         "
print "  [03] Update                    "
print "  [00] Exit                      "
print "                                 " 

Spammer = raw_input(" Choose:  ")
while True:
     if (Spammer == '01' or Spammer == '1'):
            print "Input Number:"
            print "SMS Rate: 1s - 10min"
            Delay = raw_input(" Delay: ")
            Number = raw_input(" Number: ")
            Message = raw_input(" Message: ")
            os.system("watch -n %s termux-sms-send -n %s %s " % (Delay, Number, Message))
            break
       
     elif (Spammer == '02' or Spammer == '2'):
            print "(Add Contact y or n?)"
            Choice = raw_input(">")
            if (Choice == 'Y' or Choice == 'y'):
                 Name1 = Empty
                 Name2 = Empty
                 Name3 = Empty
                 print "Contact 1: " + Name1
                 print "Contact 2: " + Name2
                 print "Contact 3: " + Name3 
                 Num = raw_input("Contact Number: ")
                 Name + Num = raw_input("Name: ")
                 Number + Num = raw_input("Number: ")
                 os.system("clear")
                 print (""Name%s " (Num)")
                 Option = raw_input("Is this correct, Y or N?\N")
                 if (Option == 'Y' or Option == 'y'):
                      print "Done"
                      os.system("clear")
                      sys.exit
                    
                 elif (Option == 'N' Option == 'n'):
                      print "Sorry Please Try again"
                      sys.exit 
                    
            elif (Choice == 'N' or Choice == 'n'):
                 print "exiting"
                 break

     elif (Spammer == '03' or Spammer == '3'):
            os.system("git clone https://github.com/STAR-Sec/SMS-Spammer")
            break
     
     elif (Spammer == '00' or Spammer == '0'):
            print "\n[!] Exit the Program..."
            sys.exit()
            break

     else:
            print "\n[!] ERROR : Wrong Input"
            os.system("sleep 1")
       
