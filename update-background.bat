@echo off
CD /d %~dp0

REM download and copy latest goes and himawari images for use in windows background slideshow, this allows us to update the image dynamically.
REM usage:
REM 		update-background.bat <output path>

python himawari.py -o %1\himawari\himawari_01.png
copy %1\himawari\himawari_01.png %1\himawari\himawari_02.png

python rammb.py -s goes-16 -z 1 -d %1\goes-16\ -f goes-16_01.png
copy %1\goes-16\goes-16_01.png %1\goes-16\goes-16_02.png

python rammb.py -s goes-17 -z 1 -d %1\goes-17\ -f goes-17_01.png
copy %1\goes-17\goes-17_01.png %1\goes-17\goes-17_02.png
