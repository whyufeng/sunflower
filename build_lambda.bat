@echo off
echo =========================================
echo AWS Lambda Deployment Packager
echo =========================================

set DEPLOY_DIR=lambda_dist
set ZIP_NAME=sunflower_daily_notify.zip

echo [1/4] Cleaning up old builds...
if exist %DEPLOY_DIR% rmdir /s /q %DEPLOY_DIR%
if exist %ZIP_NAME% del /q %ZIP_NAME%

echo [2/4] Creating temporary directory...
mkdir %DEPLOY_DIR%

echo [3/4] Installing dependencies from requirements.txt for Linux...
:: Force pip to download Linux compatible binaries instead of Windows ones
pip install --platform manylinux2014_x86_64 --target %DEPLOY_DIR% --implementation cp --python-version 3.12 --only-binary=:all: --upgrade -r requirements.txt

echo [4/4] Copying project files...
:: Copy the main script
copy scripts\daily_notify.py %DEPLOY_DIR%\

:: Copy the services directory
xcopy services %DEPLOY_DIR%\services /E /I /H /Y /Q

echo.
echo =========================================
echo Packaging to %ZIP_NAME%...
echo =========================================
:: Use PowerShell to zip the contents of the deployment directory
powershell.exe -nologo -noprofile -command "& { Compress-Archive -Path '%DEPLOY_DIR%\*' -DestinationPath '%ZIP_NAME%' -Force }"

echo.
echo Cleaning up temporary files...
rmdir /s /q %DEPLOY_DIR%

echo =========================================
echo ✅ SUCCESS! 
echo Your deployment package is ready: %ZIP_NAME%
echo.
echo Next steps:
echo 1. Go to AWS Lambda Console
echo 2. Upload the '%ZIP_NAME%' file
echo 3. Make sure your Handler is set to: daily_notify.lambda_handler
echo =========================================
pause
