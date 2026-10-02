Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Suits You Sir Build" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/4] Cleaning old files..." -ForegroundColor Yellow

Remove-Item "build" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "dist" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "SuitsYouSir.spec" -Force -ErrorAction SilentlyContinue

Write-Host "       Done!" -ForegroundColor Green
Write-Host ""

Write-Host "[2/4] Building executable..." -ForegroundColor Yellow

python3 -m PyInstaller `
    --onefile `
    --windowed `
    --name "SuitsYouSir" `
    --add-data "Sounds;Sounds" `
    --icon Icon.ico `
    main.py

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "BUILD FAILED!" -ForegroundColor Red
    Write-Host ""
    Read-Host "Press Enter to close"
    exit 1
}

Write-Host "       Done!" -ForegroundColor Green
Write-Host ""

Write-Host "[3/4] Moving executable..." -ForegroundColor Yellow

Move-Item "dist\SuitsYouSir.exe" ".\SuitsYouSir.exe" -Force

Write-Host "       Done!" -ForegroundColor Green
Write-Host ""

Write-Host "[4/4] Cleaning build files..." -ForegroundColor Yellow

Remove-Item "build" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "dist" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "SuitsYouSir.spec" -Force -ErrorAction SilentlyContinue

Write-Host "       Done!" -ForegroundColor Green
Write-Host ""

Write-Host "========================================" -ForegroundColor Green
Write-Host " BUILD SUCCESSFUL!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

Write-Host "Output:" -ForegroundColor Cyan
Write-Host "  .\SuitsYouSir.exe" -ForegroundColor White
Write-Host "  .\SuitsYouSir.zip" -ForegroundColor White
Write-Host ""

Read-Host "Press Enter to close"