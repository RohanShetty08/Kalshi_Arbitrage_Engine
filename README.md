HEAD
# Kalshi Mispricing and Arbitrage Engine

A Python research project that collects Kalshi market data,
detects structural pricing inconsistencies, and evaluates
opportunities under fees, liquidity, and execution delays.

## Initial scope

- One market family
- Read-only market data collection
- One verified structural arbitrage detector
- Recorded-data replay and paper trading

## Setup

Create an environment:
python3 -m venv .venv

Activate it:
source .venv/bin/activate

Install dependencies:
python -m pip install -r requirements.txt

## Run

python main.py

## Test

python -m pytest

# Kalshi_Arbitrage_Engine
 origin/main
