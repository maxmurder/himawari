@echo off
REM download and copy latest himawari image to a background folder for use in slideshow

C:\python39\python.exe C:\Users\Urist\Development\himawari\himawari.py -o C:\Users\Urist\Pictures\bg\himawari\himawari_01.png
copy C:\Users\Urist\Pictures\bg\himawari\himawari_01.png C:\Users\Urist\Pictures\bg\himawari\himawari_02.png

C:\python39\python.exe C:\Users\Urist\Development\himawari\rammb.py -s goes-16 -z 1 -d C:\Users\Urist\Pictures\bg\goes-16\ -f goes-16_01.png
copy C:\Users\Urist\Pictures\bg\goes-16\goes-16_01.png C:\Users\Urist\Pictures\bg\goes-16\goes-16_02.png

C:\python39\python.exe C:\Users\Urist\Development\himawari\rammb.py -s goes-17 -z 1 -d C:\Users\Urist\Pictures\bg\goes-17\ -f goes-17_01.png
copy C:\Users\Urist\Pictures\bg\goes-17\goes-17_01.png C:\Users\Urist\Pictures\bg\goes-17\goes-17_02.png
