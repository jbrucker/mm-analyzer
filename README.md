## View and Analyze Fixed Income Fund Returns

The NAV (price) of fixed income and money market funds fluctuate daily.
For the best yield, it would be good to buy at the end of a downturn in daily yield
and possibly sell or switch-out when the daily yield is above the trend for some days.

Macro factors can affect the daily returns in the short term. Most notable are an
unexpected change in interest rates or a change in *expectation* of a rate cut or hike
by the central bank.

This repo contains some Python and Jupyter code to get data for Thai M.M. or F.I. funds
and view return trends in a Jupyter Notebook.

Planned work is to create an app to test strategies for buy/sell/switch to see if
a more profitable strategy than "buy and hold" can be found.

## Run MM-Analyzer Notebook on Colab

You may need to be logged in to Google for this to work.

1. Click the "Open in Colab" button below. This will open Google Colab and load [mm_trends.ipynb](./mm_trends.ipynb)

2. On Colab, from the **Runtime** menu click **Run all** to execute the entire notebook.  Then you can scroll down to view plots and stats.

3. **Or** run individual cells by clicking the Right Arrow at the top of each cell.
   - You must run cells sequentially (at least the first time) since each cell depends on results from previous cell(s).

! [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jbrucker/mm-analyzer/blob/master/mm_trends.ipynb)

[<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" width="150"/>](https://colab.research.google.com/github/jbrucker/mm-analyzer/blob/master/mm_trends.ipynb)