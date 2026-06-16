# Modern Portfolio Theory (MPT) Optimization Engine

An asset allocation engine built in Python that uses Markowitz Modern Portfolio Theory to maximize risk-adjusted returns and minimize portfolio variance across large-cap equity assets.

## Core Features
- **Automated Data Pipeline:** Fetches historical market closing prices via Yahoo Finance API (`yfinance`).
- **Statistical Risk Modeling:** Computes annualized expected returns and a historical covariance matrix to track asset cross-correlations.
- **Monte Carlo Simulation:** Simulates 10,000 random asset allocation strategies to map out the Efficient Frontier.
- **Mathematical Optimization:** Utilizes SciPy's `SLSQP` (Sequential Least Squares Programming) optimizer under strict boundary conditions (no short selling, weights sum to 100%) to isolate the Maximum Sharpe Ratio and Minimum Volatility allocations.
- **Data Visualization:** Generates customized scatter plots mapping risk vs. return with highlighted tactical allocation targets.

## Technologies Used
- Python 3
- Pandas & NumPy (Data Wrangling & Matrix Math)
- SciPy (Mathematical Optimization)
- Matplotlib (Quantitative Visualization)
