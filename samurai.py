#di sini saya menggunakan python karena saya gak bisa shell
import os


os.system('clear')




print("  |°°°°°°|")
print("  |  |°°°°")
print("  |  |___")
print(" _|   _  |")
print("|_°______|")

print("Author: Xme 4")
print("for education cybersecurty")
print("\n1.Tebas index")
print("2.Nitip file")
print("0.exit")

apa=input("\n\nPilih: ")

if(apa == "1"):
  os.system('sh ti.sh')  
elif(apa == "2"):
  os.system('sh lihan.sh')
elif(apa == "0"):
  print("Keluar")
  
else:
  print("ngetik apa sih")
