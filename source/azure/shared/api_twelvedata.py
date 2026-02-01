import requests
import logging
import json
from urllib3.exceptions import InsecureRequestWarning

# logger will return the source module name
logger = logging.getLogger(__name__)
# display logging info level
logging.basicConfig(level=logging.INFO)
# Suppress certificate warnings
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# All responses return JSON format by default unless otherwise specified.
def stocks_list(stock_url: str, api_key: str) -> str:
    api = "/stocks"
    url = stock_url + api
    headers = {
        "Authorization": f"apikey {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "country": "pl",
        "type": "Common Stock",
        "exchange": "GPW",
        "symbol": "DNP" # CDR, DNP
        }
    response = requests.get(
        url=url,
        headers=headers,
        params=payload
    )
    if response.status_code == 200:
        logger.info("Stocks list successfully retrieved.")
        # return response.json()
        return json.dumps(response.json(), indent=4)
    else:
        logger.info(f"Failed to retrieved the stocks list: {response.status_code}")
        logger.info(response.text)


def stock_quote(stock_url: str, api_key: str, symbol: str) -> str:
    api = f"/quote?symbol={symbol}"
    url = stock_url + api
    headers = {
        "Authorization": f"apikey {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=url,
        headers=headers,
        verify=False
    )
    if response.json()["code"] == 200:
    # if response.status_code == 200:
        logger.info(f"Stock {symbol} data successfully retrieved.")
        return json.dumps(response.json(), indent=4)
    else:
        logger.info(f"Failed to retrieved {symbol} stock data: {response.json()["code"]}")
        logger.info(response.json()["message"])


# TODO:
# API calls error - how to solve 200, 400 issue?

def main() -> None:
    stocks_api_url = "https://api.twelvedata.com"
    api_key = "demo"
    data_apple = stock_quote(stocks_api_url, api_key, "AAPL")
    print(data_apple)


if __name__ == "__main__":
    main()