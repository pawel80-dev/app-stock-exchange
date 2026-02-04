# app-stock-exchange

> [!NOTE]
> For most of my projects, the leading branch is the **dev** one. That means that *_dev.yaml file is the most frequently used workflow/pipeline.  

Simple app for retrive the stock exchange data.  

Issues:
- Failed to containerized Azure Function (no Selenium): --kind functionapp
- Failed to use yfinance API in Azure Function, Google protobuf version mismatch: remove module cache for google._upb but failed with 'google', Language Worker Process exited

Tools:
- Azure Function (not implemented: Azure Container Registry)
- Azure Static Web App
- Single Page App (SPA) ?


Set environment variable via Powershell code (Windows 11):  
Temporary in a current Powershell session:  
$env:VARIABLE_NAME = "Value"  

# Permanently in privilege mode
[Environment]::SetEnvironmentVariable('MyVariable', 'Some value', 'Machine')  
# Broadcast change to Windows  
$env:MyVariable = [System.Environment]::GetEnvironmentVariable('MyVariable', 'Machine')  

Remove system variable:
'''
Remove-Item Env:MyVariable
'''

Display system variables via Powershell:  
'''
Get-ChildItem Env:
'''

> [!NOTE]
>.env File: Best for project-specific secrets shared with other developers (usually requires dotenv package in code).
>terminal.integrated.env.windows: Best for local development environment machine-specific paths or variables. 