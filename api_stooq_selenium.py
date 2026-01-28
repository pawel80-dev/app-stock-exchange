import yfinance as yf
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


# How to create a Selenium web scraper in Azure Functions
# https://towardsdatascience.com/how-to-create-a-selenium-web-scraper-in-azure-functions-f156fd074503
# https://learn.microsoft.com/en-us/answers/questions/4375201/how-can-i-run-selenium-script-in-functions-app
# https://learn.microsoft.com/en-us/answers/questions/1354174/cannot-find-chrome-binary-in-azure-function-app-(w
def get_gpw_stock(symbol: str) -> dict:
    try:
        stock = yf.Ticker(symbol)
        # historical_data = stock.history(start="2026-01-01", end="2026-01-23", interval="1d")
        # historical_data = stock.history(period="1mo")
        # return historical_data
        return {
            "symbol": symbol,
            "price": stock.info.get("currentPrice"),
            "currency": stock.info.get("currency")
            }

    except Exception as e:
        logger.info(f"Generic error when fetching the data for {symbol}: {e}")
        return None


def main() -> None:
    data_cd_project_red = get_gpw_stock("SCW.NC")
    # data_cd_project_red = get_gpw_stock("CDR.WA")
    print(data_cd_project_red)


if __name__ == "__main__":
    main()