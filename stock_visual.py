import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'indexProcessed.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high, and low temps
    dates, highs, lows, totals = [], [], [], []
    for row in reader:
        currert_date = datetime.strptime(row[1], '%Y-%m-%d')
        try:
            stocks_high = float(row[3])
            stocks_low = float(row[4])
            total = stocks_high - stocks_low
        except ValueError:
            print(f"Missing data for {currert_date}")
        else:
            dates.append(currert_date)
            highs.append(stocks_high)
            lows.append(stocks_low)
            totals.append(total)

# Plot the high and low tempautres.
plt.style.use('seaborn-whitegrid')
fig, ax = plt.subplots()

ax.plot(dates, totals, c='red', alpha=0.7)
ax.plot(dates, lows, c='green', alpha=0.5)

# Format plot
title = "Stock from 1986 to 2020"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Stock Price', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
