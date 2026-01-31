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
        # return historical_data[['Open', 'High', 'Low', 'Close', 'Volume']]
        return {
            "symbol": symbol,
            "company_name": stock.info.get("longName"),
            "price": stock.info.get("currentPrice"),
            "currency": stock.info.get("currency"),
            # "recommendations": stock.get_recommendations()
            }

    except Exception as e:
        logger.info(f"Generic error when fetching the data for {symbol}: {e}")
        return None


def main() -> None:
    stocks = ["CDR.WA", "PKO.WA", "KGH.WA"]
    for symbol in stocks:
        data = get_gpw_stock(symbol)
        print(data)


if __name__ == "__main__":
    main()