param(
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$src = Join-Path $repoRoot 'user'
$target = Join-Path $env:APPDATA 'Sublime Text\Packages\User'

if (-not (Test-Path -LiteralPath $src)) {
    Write-Error "Source folder not found: $src"
}

$extensions = @('.sublime-settings', '.sublime-keymap', '.sublime-syntax', '.sublime-color-scheme')
$files = Get-ChildItem -LiteralPath $src -File | Where-Object { $_.Extension -in $extensions }

if (-not (Test-Path -LiteralPath $target)) {
    New-Item -ItemType Directory -Path $target -Force | Out-Null
}

$dry = if ($DryRun) { ' [DRY RUN]' } else { '' }
Write-Host "Syncing $($files.Count) file(s) to: $target$dry"

foreach ($file in $files) {
    $dest = Join-Path $target $file.Name
    Write-Host "  $($file.Name)"
    if (-not $DryRun) {
        Copy-Item -LiteralPath $file.FullName -Destination $dest -Force
    }
}

if ($DryRun) {
    Write-Host "Dry run complete. Re-run without -DryRun to copy."
}
