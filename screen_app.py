import pandas as pd
from finvizfinance.screener.overview import Overview

def screenoverview(signal):
    stocks_overview = Overview()
    filters_dict = {
        'Exchange':'Any', 
        'Sector':'Any',
        'Market Cap.': 'Any',
        'Analyst Recom.': 'Hold or better' ,
        'P/E':'Profitable (>0)',
        'Forward P/E': 'Profitable (>0)',
        'PEG':'Under 2',
        'P/S': 'Under 2',
        'P/B':'Under 2',
        'Return on Equity': 'Positive (>0%)',
        'Return on Investment':'Positive (>0%)',
        'Gross Margin':'Positive (>0%)',
        'Net Profit Margin':'Positive (>0%)',
        'Current Ratio': 'Over 1',
        'Quick Ratio': 'Over 1'
        }
    stocks_overview.set_filter(signal=signal,filters_dict=filters_dict)
    df = pd.DataFrame(stocks_overview.screener_view())
    print(df)

screenoverview(input("Signals include: Top Gainers, Top Losers, New High, New Low, Most Volatile, Most Active," +
    " Unusual Volume, Overbought, Oversold, Downgrades, Upgrades, Earnings Before, Earnings After, Recent Insider Buying," +
    " Recent Insider Selling, Major News, Horizonal S/R, TL Resistance, TL Support, Wedge Up, Wedge Down, Triangle Ascending" +
    " Triangle Descending, Wedge, Channel Up, Channel Down, Channel, Double Top, Double Bottom, Multiple Top," +
    " Multiple Bottom, Head & Shoulders, Head & Shoulders Inverse. Enter your signal: "))
