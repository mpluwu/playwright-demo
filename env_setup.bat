@echo off
echo ==========================================
echo  Environment Setup - Playwright + opencart 
echo ==========================================

echo [1/7] Installing test data, env vars, date/time handling...
call npm install dotenv @faker-js/faker luxon  ::loads settings from .env file into ur code, generates realistic fake data, handles dates
if errorlevel 1 goto :error

echo [2/7] Installing API / data validation...
call npm install ajv csv-parse xlsx #validate json data and read csv/excel test-data files
if errorlevel 1 goto :error

echo [3/7] Installing accessibility testing (WCAG)...
call npm install @axe-core/playwright #adds accessibility check to tests
if errorlevel 1 goto :error

echo [4/7] Installing Allure reporting...
call npm install allure-playwright #produces the allure report 
if errorlevel 1 goto :error

echo [5/7] Installing Node.js TypeScript type definitions...
call npm install -D @types/node #gives typescript awareness of node.js built in feature
if errorlevel 1 goto :error

echo [6/7] Installing Playwright browser binaries...
call npx playwright install #downloads the actual browsers playwright will control
if errorlevel 1 goto :error

echo [7/7] Installing MySQL DB validation / DML...
call npm install mysql2 #lets ur tests connect to a mysql database
if errorlevel 1 goto :error

echo.
echo ==========================================
echo  Environment setup completed successfully!
echo ==========================================
pause
exit /b 0

:error
echo.
echo ERROR: Setup failed. See output above.
pause
exit /b 1
