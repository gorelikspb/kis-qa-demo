# Скрипт проверки перед push на GitHub
# Проверяет что внутренние документы не попадут в репозиторий

Write-Host "🔍 Проверка перед push на GitHub..." -ForegroundColor Cyan
Write-Host ""

$errors = @()
$warnings = @()

# Проверка 1: Нет ссылок на локальные пути
Write-Host "1. Проверка ссылок на локальные пути..." -ForegroundColor Yellow
$localPathPatterns = @(
    "D:\\dev",
    "cv_common",
    "\\.\\./common",
    "\\.\\.\\\\common"
)

$filesToCheck = Get-ChildItem -Path . -Include *.md,*.py,*.txt -Recurse | Where-Object { 
    $_.FullName -notmatch "venv|__pycache__|\.git"
}

foreach ($file in $filesToCheck) {
    $content = Get-Content $file.FullName -Raw -ErrorAction SilentlyContinue
    if ($content) {
        foreach ($pattern in $localPathPatterns) {
            if ($content -match $pattern) {
                $warnings += "⚠️  Найдена ссылка на локальный путь в $($file.Name): $pattern"
            }
        }
    }
}

# Проверка 2: .gitignore настроен правильно
Write-Host "2. Проверка .gitignore..." -ForegroundColor Yellow
if (Test-Path ".gitignore") {
    $gitignoreContent = Get-Content ".gitignore" -Raw
    if ($gitignoreContent -notmatch "venv|__pycache__") {
        $warnings += "⚠️  .gitignore может быть неполным"
    }
} else {
    $errors += "❌ .gitignore отсутствует!"
}

# Проверка 3: Что будет добавлено в git
Write-Host "3. Проверка файлов для коммита..." -ForegroundColor Yellow
$gitStatus = git status --porcelain 2>$null
if ($LASTEXITCODE -eq 0) {
    $stagedFiles = git diff --cached --name-only 2>$null
    if ($stagedFiles) {
        Write-Host "   Файлы готовые к коммиту:" -ForegroundColor Green
        foreach ($file in $stagedFiles) {
            Write-Host "   ✅ $file" -ForegroundColor Gray
        }
    }
    
    # Проверка на внутренние документы
    $internalDocs = $stagedFiles | Where-Object { 
        $_ -match "cv_common|\.\./common|DEPLOYMENT_PLAN|EMPLOYER_GUIDE"
    }
    if ($internalDocs) {
        $errors += "❌ Обнаружены внутренние документы в staged: $($internalDocs -join ', ')"
    }
} else {
    $warnings += "⚠️  Git репозиторий не инициализирован или не в git папке"
}

# Проверка 4: README.md содержит необходимую информацию
Write-Host "4. Проверка README.md..." -ForegroundColor Yellow
if (Test-Path "README.md") {
    $readmeContent = Get-Content "README.md" -Raw
    if ($readmeContent -notmatch "Live Demo") {
        $warnings += "⚠️  README.md может не содержать ссылку на Live Demo"
    }
} else {
    $errors += "❌ README.md отсутствует!"
}

# Вывод результатов
Write-Host ""
Write-Host "═══════════════════════════════════════" -ForegroundColor Cyan
Write-Host "Результаты проверки:" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

if ($errors.Count -eq 0 -and $warnings.Count -eq 0) {
    Write-Host "✅ Все проверки пройдены! Можно делать push." -ForegroundColor Green
    exit 0
}

if ($errors.Count -gt 0) {
    Write-Host "❌ Ошибки (нужно исправить перед push):" -ForegroundColor Red
    foreach ($error in $errors) {
        Write-Host "   $error" -ForegroundColor Red
    }
    Write-Host ""
}

if ($warnings.Count -gt 0) {
    Write-Host "⚠️  Предупреждения (рекомендуется проверить):" -ForegroundColor Yellow
    foreach ($warning in $warnings) {
        Write-Host "   $warning" -ForegroundColor Yellow
    }
    Write-Host ""
}

if ($errors.Count -gt 0) {
    Write-Host "❌ Нельзя делать push до исправления ошибок!" -ForegroundColor Red
    exit 1
} else {
    Write-Host "⚠️  Есть предупреждения, но можно продолжать." -ForegroundColor Yellow
    exit 0
}

