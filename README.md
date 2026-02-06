# app-stock-exchange

> [!NOTE]
> For most of my projects, the leading branch is the **dev** one. That means that *_dev.yaml file is the most frequently used workflow/pipeline.  

Simple app for retrive the stock exchange data.  

Tools:
- Azure Function (not implemented: Azure Container Registry)
- Azure Static Web App
- Single Page App (SPA) ?

Issues:
- Failed to containerized Azure Function (no Selenium): --kind functionapp
- Failed to use yfinance API in Azure Function, Google protobuf version mismatch: remove module cache for google._upb but failed with 'google', Language Worker Process exited

<br>

> [!NOTE]
>To distinguish between local and remote environment, use a system variable, for example AZURE_ENVIRONMENT:  
>```az functionapp config appsettings set -g ${{ ... }} -n ${{ ... }} --settings AZURE_ENVIRONMENT="${{ secrets.AZURE_ENVIRONMENT }}"```  
>then in the code, ```os.getenv("AZURE_ENVIRONMENT", "local")```  

<br>

> [!NOTE]
>Import environment variables:  
>- Powershell/Bash script  
>- **.env** File: Best for project-specific secrets shared with other developers (usually requires dotenv package in code)  
>- **terminal.integrated.env.windows (terminal.integrated.env.linux)**: Best for local development environment machine-specific paths or variables  


### Set environment variables via Powershell code (Windows 11):
Temporary in a current Powershell session:  
```$env:VARIABLE_NAME = "Value"```

Permanently in privilege mode:  
```[Environment]::SetEnvironmentVariable('MyVariable', 'Some value', 'Machine')```

Broadcast change to Windows:  
```$env:MyVariable = [System.Environment]::GetEnvironmentVariable('MyVariable', 'Machine')```

Remove system variable:  
```Remove-Item Env:MyVariable```

Display system variables via Powershell:  
```Get-ChildItem Env:```

### Set environment variables via VSC terminal.integrated.env.windows (or terminal.integrated.env.linux):
File -> Preferences -> Settings  
Find @id:terminal.integrated.env.windows  
Select which config you would like to change - User’s or Worspace (recommended)  
For the setting Terminal › Integrated › Env: Windows, click the **Edit in settings.json** link  
Define your environment variables here:  
```
{
    "terminal.integrated.env.windows": {
        "MY_VARIABLE1": "",
        "MY_VARIABLE2": ""
    }
}
```
