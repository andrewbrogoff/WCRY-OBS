This is just something that I wanted to try so that I could learn how malware authors think.

Python and Powershell have to be installed in order for this to work - Powershell is included in windows by default.

Sources for installing Powershell and Python:
https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2
and at: https://www.python.org/downloads/

Run 'FinalLauncher.ps1' if you want to test the code. (windows only)
Otherwise run 'LinuxFinalLauncher.ps1' to test. (Mac and Linux)
Deobfuscated Versions of the launchers are available and should be identifiable.


Special thanks to the developers at https://github.com/danielbohannon/Invoke-Obfuscation,  https://github.com/billythegoat356/Kramer, and https://github.com/PyObfx/PyObfx for creating their tools for obfuscation.


The path that the code is executed is as follows (In base64 to prevent spoilers accidentally): RmluYWxMYXVuY2hlci5wczEgZG93bmxvYWRzIE9zaGF3b3R0LnB5IGFuZCBleGVjdXRlcyBpdC4gRnJvbSB0aGVyZSBPc2hhd290dC5weSB0YWtlcyBoZXhhZGVjaW1hbHMgZm9yIHBheWxvYWQuemlwIGFuZCBjb252ZXJ0ZXMgdGhhdCB0byBhIGZpbGUgYW5kIGV4dHJhY3RzIGl0IGludG8gTWFsd2FyZS5weS4gQWZ0ZXIgdGhhdCBPc2hhd290dC5weSBleGVjdXRlcyBNYWx3YXJlLnB5LiBUaGVuIE1hbHdhcmUucHkgcnVucyBhbiBlYXN0ZXIgZWdnIHRoYXQgZG9lcyBub3RoaW5nIGFuZCBhbHNvIGRlY29kZXMgZnJvbSBiYXNlNjQgYW5kIHRoZW4gQUVTIHRvIFdhbm5hY3J5IFByYW5rLnB5IGFuZCBleGVjdXRlcyBpdC4=