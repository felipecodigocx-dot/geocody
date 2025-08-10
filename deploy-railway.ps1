Write-Host "🚀 DEPLOY GEOCODIFICACAO WEB NO RAILWAY" -ForegroundColor Cyan
Write-Host "===========================================" -ForegroundColor Cyan

Write-Host "📁 Verificando arquivos..." -ForegroundColor Yellow

if (-not (Test-Path "app.py")) {
    Write-Host "❌ app.py nao encontrado" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path "requirements.txt")) {
    Write-Host "❌ requirements.txt nao encontrado" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path "templates/index.html")) {
    Write-Host "❌ templates/index.html nao encontrado" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Arquivos encontrados" -ForegroundColor Green

Write-Host "📦 Verificando Node.js..." -ForegroundColor Yellow
try {
    node --version
    Write-Host "✅ Node.js OK" -ForegroundColor Green
} catch {
    Write-Host "❌ Node.js nao encontrado. Instale: https://nodejs.org" -ForegroundColor Red
    exit 1
}

Write-Host "📦 Instalando Railway CLI..." -ForegroundColor Yellow
npm install -g @railway/cli

Write-Host "🔐 Fazendo login no Railway..." -ForegroundColor Yellow
railway login

Write-Host "🏗️ Inicializando projeto..." -ForegroundColor Yellow
railway init

Write-Host "🔧 Configurando variaveis..." -ForegroundColor Yellow
railway variables set FLASK_ENV=production

Write-Host "🚀 Fazendo deploy..." -ForegroundColor Yellow
railway up

Write-Host "✅ Deploy concluido!" -ForegroundColor Green
Write-Host "Dashboard: https://railway.app/dashboard" -ForegroundColor Cyan

railway status
