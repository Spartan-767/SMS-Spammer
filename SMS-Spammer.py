#!/usr/bin/python
import sys, os
# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################
""" Developed by spartan """
os.system("clear")
print " "
print "   ___   __  __   ___     ___       "
print "  / __| |  \/  | / __|   / __|  _ __   __ _   _ __    _ __    ___   _ _ "
print "  \__ \ | |\/| | \__ \   \__ \ | '_ \ / _` | | '  \  | '  \  / -_) | '_|"
print "  |___/ |_|  |_| |___/   |___/ | .__/ \__,_| |_|_|_| |_|_|_| \___| |_|  "
print "                               |_|                                      "
print "------------------------------------------------------------------------- "
print "  ===|[ SMS Spammer ]|==="
print "  [01] Setup New Session        "
print "  [02] Repeat Last Spam          "
print "  [03] Update           "
print "  [00] Exit"
print
Spammer = raw_input(" Choose:  ")

if (Spammer == '01' or Spammer == '1'):
       print " "
       print " SMS Rate:(1s - 10min)             "
       Delay = raw_input(" Delay: ")
       Number = raw_input(" Number: ")
       Message = raw_input(" Message: ")
       os.system("watch -n %s termux-sms-send -n %s %s " % (Delay, Number, Message))
       sys.exit()

elif (Spammer == '02' or Spammer == '2'):
       print "Coming Soon"

elif (Spammer == '03' or Spammer == '3'):
       os.system("git clone")

elif (Spammer == '00' or Spammer == '0'):
       print "\n[!] Exit the Program..."
       sys.exit()

else:
       print "\n[!] ERROR : Wrong Input"
       time.sleep(1)
       restart_program()
