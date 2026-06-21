@echo off

REM Check if Python is installed
python --version > nul 2>&1
if %errorlevel% equ 0 (
    echo Python is installed
) else (
    echo Python is not installed
)

REM Check if pymongo library is installed
python -c "import pymongo" > nul 2>&1
if %errorlevel% equ 0 (
    echo pymongo library is installed
) else (
    echo pymongo library is not installed
)

REM Check if OpenAI library is installed
python -c "import openai" > nul 2>&1
if %errorlevel% equ 0 (
    echo OpenAI library is installed
) else (
    echo OpenAI library is not installed
)

REM Check if MongoDB is installed and running
sc query MongoDB > nul 2>&1
if %errorlevel% equ 0 (
    echo MongoDB service is installed and running
) else (
    echo MongoDB service is not installed or not running
)

pause
