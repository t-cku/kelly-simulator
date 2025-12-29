Kelly Criterion Risk Simulator

Project Overview
A quantitative simulation engine built using Python to analyse the performance of the Kelly Criterion strategy. The project compares different betting sizing strategies (Full Kelly, Half Kelly, and Over-Bet) to demonstrate the relationship between geometric growth and risk of ruin.

Key Features
- Custom Simulation Engine: Built a reusable Simulator class in Python
- Monte Carlo Analysis: Simulates hundreds and thousands of equity curves to determine average outcomes, rather than just one simulation
- Risk Visualisation: Visualises the volatility drag of overbetting vs the stability of full/fractional Kelly

Results
- Full Kelly: Maximises theoretical growth but experiences significant drawdowns
- Half Kelly: Offers the best risk-adjusted returns; highest Sharpe-Ratio
- Over-betting: While it is capable of short-term outperformance, it guarantees ruin in the long term


Installation

1. Clone the repository
git clone https://github.com/t-cku/kelly-simulator
2. Install dependencies
pip install -r requirements.txt
3. Run the Sim
python main.py
