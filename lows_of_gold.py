import csv

import matplotlib.pyplot as plt

from datetime import datetime

filename = 'goldprices.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high, and low temps
    dates, lows = [], []
    for row in reader:
        currert_date = datetime.strptime(row[0], '%Y-%m-%d')
        try:
            low = float(row[2])
        except ValueError:
            print(f"Missing data for {currert_date}")
        else:
            dates.append(currert_date)
            lows.append(low)

# Plot the high and low tempautres.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, lows, c='red', alpha=0.9)

# Format plot
title = "Lows of gold prices over past twenty years"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Prices(USD)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
