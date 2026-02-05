import logging
import json
import os
import azure.functions as func
from shared.api_twelvedata import stock_quote

# logger will return the source module name
logger = logging.getLogger(__name__)
# display logging info level
logging.basicConfig(level=logging.INFO)


app = func.FunctionApp()

# route: api/stocks?stock=CompanySymbol
# route: api/stocks?user=Username
# https://functionAppName.azurewebsites.net/api/stocks?stock=CompanySymbol
# https://functionAppName.azurewebsites.net/api/stocks?user=YourName
@app.function_name(name="HttpTrigger-stocks")
@app.route(route="stocks", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logger.info("AZ-FUNC app-stock-exchange.")
    stocks_api_url = "https://api.twelvedata.com"
    api_key = os.environ["TWELVEDATA_API_KEY"]
    stock = req.params.get("stock")
    user = req.params.get("user")

    if user:
        return f"Ciao {user}, come stai?"
    if stock:
        # data = json.loads(stock_quote(stocks_api_url, api_key, "MSFT"))
        # return f"Company name: {data["name"]}, Price: {data["close"]} {data["currency"]}"
        data = stock_quote(stocks_api_url, api_key, stock)
        # return data["fifty_two_week"]["high_change"]
        return data
    else:
        return "Ciao!"


# route parameter is changed: api/{functionname} to api/message
@app.function_name(name="HttpTrigger-api")
@app.route(route="message", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logger.info("AZ-FUNC TEST API message.")

    # return "Hello, from the stocks API!"
    return json.dumps({"text": "Hello, from the stocks API!"})


# route parameter is changed: api/{functionname} to api/os
@app.function_name(name="HttpTrigger-api-os")
@app.route(route="os", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logger.info("AZ-FUNC OS type.")
    os_type = os.name
    az_env = os.environ["AZURE_FUNCTIONS_ENVIRONMENT"]

    # os.name = "nt" for Windows, "posix" for Linux
    return json.dumps({"OS type": os_type, "Environment": az_env})
