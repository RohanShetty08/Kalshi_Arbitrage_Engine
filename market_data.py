import httpx


BASE_URL = "https://external-api.kalshi.com/trade-api/v2"


def fetch_markets():
    """Fetch one page of open NYC temperature markets."""
    response = httpx.get(
        f"{BASE_URL}/markets",
        params={
            "series_ticker": "KXHIGHNY",
            "status": "open",
            "limit": 100,
        },
        timeout=15.0,
    )

    response.raise_for_status()
    return response.json()


def main():
    try:
        data = fetch_markets()
    except httpx.HTTPStatusError as error:
        print(f"Kalshi returned HTTP {error.response.status_code}.")
        return
    except httpx.RequestError as error:
        print(f"Could not connect to Kalshi: {error}")
        return

    markets = data["markets"]

    print(f"Received {len(markets)} open NYC temperature markets.\n")

    if not markets:
        print("No open markets in this series right now.")
        return

    for market in markets[:10]:
        print(f"Ticker: {market['ticker']}")
        print(f"Title: {market['title']}")
        print(f"YES description: {market.get('yes_sub_title', '')}")
        print(f"Event: {market['event_ticker']}")
        print(f"Closes: {market.get('close_time', 'Not provided')}")
        print()

    if data.get("cursor"):
        print("More markets are available on another page.")


if __name__ == "__main__":
    main()