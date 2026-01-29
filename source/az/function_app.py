import logging
# import os
import azure.functions as func

# logger will return the source module name
logger = logging.getLogger(__name__)
# display logging info level
logging.basicConfig(level=logging.INFO)


app = func.FunctionApp()

# route parameter is changed: api/{functionname} to api/stocks
# https://functionAppName.azurewebsites.net/api/stocks?user=YourName
@app.function_name(name="HttpTrigger-stocks-api")
@app.route(route="stocks", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logger.info("AZ-FUNC app-stock-exchange.")
    user = req.params.get("user")

    return f"Hello, {user}!"


# route parameter is changed: api/{functionname} to api/message
@app.function_name(name="HttpTrigger-api")
@app.route(route="message", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logger.info("AZ-FUNC TEST API message.")

    return "Hello, from the stocks API!"
