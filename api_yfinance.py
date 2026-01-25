import yfinance as yf
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


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
        # return historical_data
        # logger.info(f"Stock data for {symbol} retrieved successfully.")
        # return historical_data[['Open', 'High', 'Low', 'Close', 'Volume']]
    
    # try:
    #     stock = yf.Ticker(symbol)
    #     data = stock.history(period="1d")
    #     data = stock.history(start="2026-01-01", end="2026-01-23", interval="1d")
    #     data = stock.history(period="1mo")
    #     info = stock.info
        
    #     logger.info(f"Stock data for: {symbol} retrieved successfully")
    #     return {
    #         "symbol": symbol,
    #         "price": info.get("currentPrice"),
    #         "currency": info.get("currency"),
    #         "data": data.to_dict()
    #     }
    # except Exception as e:
    #     logger.error(f"Failed to fetch {symbol}: {e}")
    #     return {}


def main() -> None:
    data_cd_project_red = get_gpw_stock("CDR.WA")
    print(data_cd_project_red)


if __name__ == "__main__":
    main()