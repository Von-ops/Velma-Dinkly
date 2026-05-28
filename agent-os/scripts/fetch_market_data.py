#!/usr/bin/env python3
"""
Fetch live market data for Von's watchlist using yfinance.
Writes JSON to web/data/market_data.json for the dashboard.
Usage: python3 fetch_market_data.py [--watchlist-file path/to/tickers.json]
"""

import json
import sys
import os
from datetime import datetime, timezone

WATCHLIST = ["AAPL", "NVDA", "MSFT", "AMZN", "GOOGL", "TSLA", "META", "EYPT"]
SECTORS = {
    "AAPL": "Consumer Tech", "NVDA": "Semiconductors", "MSFT": "Software",
    "AMZN": "E-Commerce", "GOOGL": "Internet", "TSLA": "EV/Auto",
    "META": "Social Media", "EYPT": "Biotech"
}

def fetch_data(tickers=None):
    import yfinance as yf
    tickers = tickers or WATCHLIST
    t = yf.Tickers(" ".join(tickers))
    results = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    for sym in tickers:
        try:
            info = t.tickers[sym].fast_info
            price = info.last_price
            prev = info.previous_close
            if not price or not prev:
                raise ValueError("No price data")
            chg = price - prev
            pct = (chg / prev) * 100
            day_high = getattr(info, "day_high", 0) or 0
            day_low = getattr(info, "day_low", 0) or 0
            volume = getattr(info, "last_volume", 0) or 0
            mkt_cap = getattr(info, "market_cap", 0) or 0

            results.append({
                "ticker": sym,
                "price": round(price, 2),
                "change": round(chg, 2),
                "pct_change": round(pct, 2),
                "day_high": round(day_high, 2),
                "day_low": round(day_low, 2),
                "volume": volume,
                "market_cap": mkt_cap,
                "sector": SECTORS.get(sym, ""),
                "updated": now
            })
        except Exception as e:
            results.append({
                "ticker": sym, "price": 0, "change": 0, "pct_change": 0,
                "day_high": 0, "day_low": 0, "volume": 0, "market_cap": 0,
                "sector": SECTORS.get(sym, ""), "error": str(e), "updated": now
            })

    return results

def write_output(data, path=None):
    if not path:
        path = os.path.join(os.path.expanduser("~/von-empire-os/web/data"), "market_data.json")

    output = {
        "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "source": "yfinance",
        "market_status": "fetching...",
        "tickers": data
    }

    with open(path, "w") as f:
        json.dump(output, f, indent=2)

    return path

if __name__ == "__main__":
    data = fetch_data()
    path = write_output(data)
    print(f"Market data written to {path}")
    for t in data:
        sign = "+" if t["change"] >= 0 else ""
        price_str = f"${t['price']:.2f}" if t["price"] else "N/A"
        chg_str = f"{sign}{t['pct_change']:.2f}%" if t["price"] else "ERROR"
        print(f"  {t['ticker']:6s}: {price_str:>10s} ({chg_str:>8s}) [{t['sector']}]")
    print(f"\nTotal: {len(data)} tickers fetched")
