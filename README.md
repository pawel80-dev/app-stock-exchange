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

### Set environment variables via VSC terminal.integrated.env.windows:
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

<br>

> [!NOTE]
>**.env** File: Best for project-specific secrets shared with other developers (usually requires dotenv package in code).  
>**terminal.integrated.env.windows**: Best for local development environment machine-specific paths or variables.  