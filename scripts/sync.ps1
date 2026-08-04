param(
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$src = Join-Path $repoRoot 'packages'
$target = Join-Path $env:APPDATA 'Sublime Text\Packages'

if (-not (Test-Path -LiteralPath $src)) {
    Write-Error "Source folder not found: $src"
}

$extensions = @('.sublime-settings', '.sublime-keymap', '.sublime-syntax', '.sublime-color-scheme')

$dry = if ($DryRun) { ' [DRY RUN]' } else { '' }
Write-Host "Syncing packages to: $target$dry"

foreach ($pkgDir in Get-ChildItem -LiteralPath $src -Directory) {
    $pkgTarget = Join-Path $target $pkgDir.Name
    $files = Get-ChildItem -LiteralPath $pkgDir.FullName -File | Where-Object { $_.Extension -in $extensions }

    if ($files.Count -eq 0) {
        continue
    }

    if (-not (Test-Path -LiteralPath $pkgTarget)) {
        New-Item -ItemType Directory -Path $pkgTarget -Force | Out-Null
    }

    Write-Host "  [$($pkgDir.Name)] $($files.Count) file(s)"
    foreach ($file in $files) {
        $dest = Join-Path $pkgTarget $file.Name
        Write-Host "    $($file.Name)"
        if (-not $DryRun) {
            Copy-Item -LiteralPath $file.FullName -Destination $dest -Force
        }
    }
}

if ($DryRun) {
    Write-Host "Dry run complete. Re-run without -DryRun to copy."
}
