# XAUUSD Trading Bot - Version 1
# Strategy: BOS -> Pullback -> Confirmation

def analyse_market(candles):
    if len(candles) < 5:
        return "WAIT"

    # Most recent candles
    previous = candles[-3]
    current = candles[-1]

    # Simple structure check
    if current["close"] > previous["high"]:
        return "BULLISH BOS"

    if current["close"] < previous["low"]:
        return "BEARISH BOS"

    return "WAIT"


# Test data
candles = [
    {"high": 2650, "low": 2640, "close": 2645},
    {"high": 2655, "low": 2643, "close": 2650},
    {"high": 2665, "low": 2648, "close": 2660},
    {"high": 2675, "low": 2655, "close": 2670},
    {"high": 2680, "low": 2660, "close": 2678},
]

signal = analyse_market(candles)

print("XAUUSD BOT SIGNAL:", signal)
