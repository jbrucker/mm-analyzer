"""
Download historical NAV data for Bualuang funds.

URL is of the form
https://www.bblam.co.th/en/products/mutual-funds/historical-daily-navs?p_code=BFIXED
&date_from=01&month_from=01&year_from=2024&date_to=14&month_to=09&year_to=2025

This returns an HTML page with a lot of Javascript.
It has two interesting arrays:
let fundArray = JSON.parse('[
      {"code": "B-TREASURY","date":"2025-09-12","name":"Bualuang Treasury"},
      ...
      ]');
// selected fund
let p_code = 'BFIXED';  
// History performance for selected fund
let performArray = JSON.parse('[
      {"pf_date":"2025-09-12","p_code":"BFIXED",
       "pf_buy":"13.49010","pf_sell":"13.49020", "pf_price":"13.49010",
       "pf_units":"3710530955.42","pf_value":"50055618063.92",
       "pf_day":"6","pf_date_show":"2025-09-12"},
       ...
       ]');
"""
# flake8: noqa E501 Line Too Long
from datetime import datetime, date
import json
import re
import urllib.request, urllib.error


BASE_URL = "https://www.bblam.co.th/en/products/mutual-funds/historical-daily-navs"

def blam_download(fund_code: str, start_date: str | date, end_date: str | date):
    """Download data for a specified BLAM mutual fund.

    :param fund_code: Fund code as on BLAM web site, e.g. "BFIXED"
    :param start_date: starting date in the form "dd-mm-yyyy" or a date object
    :param end_date: ending date in the form "dd-mm-yyyy" or a date object
    :returns: ?
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, "%d-%m-%Y").date()
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, "%d-%m-%Y").date()
    url = (f"{BASE_URL}?p_code={fund_code}"
           f"&date_from={start_date.day}&month_from={start_date.month}&year_from={start_date.year}"
           f"&date_to={end_date.day}&month_to={end_date.month}&year_to={end_date.year}"
          )
    print(url)
    # Get the page
    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode("utf-8")
        response.close()
        # save response to a file
        with open("response.txt", "w", encoding="utf-8") as output_file:
            output_file.write(content)
    except urllib.error.HTTPError as ex:
        print(f"HTTP Error Code: {ex.code} {ex.reason}")
        return ""
    except urllib.error.URLError as ex:
        print(f"URL Error: {ex.reaseon}")
        return ""
    # Extract performance data using a regex
    pattern = r"let performArray = JSON.parse('[^)]*')"
    pattern = r"let performArray\s*=\s*JSON\.parse\('\[(.+).*\]'\)"
    match = re.search(pattern, content)
    if match:
        data = match.group(1)
        return data
    else:
        print(f"Pattern {pattern} not found")
        return ""


def save_as_csv(data: str, filename: str):
    """Save historical NAV data to a CSV file.
    
    The data from BLAM is in a JSON array.
    """
    # Is is an array?
    if not data.startswith('['):
        data = "[" + data + "]"
    nav_list = json.loads(data)
    # Each data point is a dict. Useful keys are 'pf_date' and 'pr_price'
    with open(filename, "w", encoding='utf-8') as outfile:
        outfile.write("DATE,NAV\n")
        for count, item in enumerate(nav_list, start=1):
            outfile.write(f"{item['pf_date']},{item['pf_price']}\n")
        print(f"Wrote {count} lines")


if __name__ == '__main__':
    data = blam_download("BFIXED", "01-01-2024", "12-09-2025")
    # file to save data
    filename = "BFIXED-20250912.csv"
    if data:
        print("Matched:", data)
        save_as_csv(data, filename)