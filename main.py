# Variables! Input your ISO image to download, HDD space (in gigabytes) and Memory (in Megabytes). Default image is Haiku (may be outdated). This script allows us to not waste our storage space by downloading ISO when we run! Read README.md for more info.

ISO_URL = "http://mirror.rit.edu/haiku/r1beta4/haiku-r1beta4-x86_64-anyboot.iso"
HDD_SPACE = 20
SHOW_CREDITS = 1
MEMORY = 256
SHOWLOG = 0
AUTOSTART = 0
FULLSCREEN = 0

# Main code begins
if AUTOSTART == 0:
  print("Press ENTER to start.")
  input()

import os

print("Checking for image files...")
if os.path.isfile("./image.iso") == True:
  os.remove("./image.iso")
  print("Deleted image.iso")

if os.path.isfile("./disk1.img") == True:
  os.remove("./disk1.img")
  print("Deleted disk1.img")

if os.path.isfile("./disk1.img") == False:
  print("None found.")

if os.path.isfile("./image.iso") == False:
  print("None found.")

print("############################################")
print("#                                          #")
print("#      AutoVM - automatic VM creator       #")
print("#                                          #")
print("############################################")

if SHOW_CREDITS == 1:
  print("Script make by @randomusbs11")


print("########################")
print("Downloading ISO image...")
print("########################")
os.system("wget -O image.iso " + ISO_URL)

print("###############")
print("Creating HDD...")
print("###############")
os.system("qemu-img create -f qcow2 disk1.img " + str(HDD_SPACE) + "G")
if SHOWLOG == 1:
  print(str(HDD_SPACE))

print("Processes completed, starting VM...")

if FULLSCREEN == 1: 
  os.system("qemu-system-x86_64 -cdrom ./image.iso -m " + str(MEMORY) + " -hda disk1.img -full-screen")
else:
  os.system("qemu-system-x86_64 -cdrom ./image.iso -m " + str(MEMORY) + " -hda disk1.img")

if SHOWLOG == 1:
  print(str(MEMORY))
