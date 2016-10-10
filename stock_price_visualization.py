from yahoo_finance import Share
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, \
    DayLocator, MONDAY
from matplotlib.finance import *

apple = Share('AAPL')
historical_data = apple.get_historical('2013-01-01', '2016-01-01')
data = DataFrame(historical_data)[['Close', 'Date', 'Volume']].reindex(columns=['Date', 'Close', 'Volume'])
price = data['Close'].tolist()
price = list(map(float, price))
volume = data['Volume'].tolist()
volume = list(map(int, volume))
tmp = data['Date'].tolist()
date = list(range(0, len(tmp)))

mondays = WeekdayLocator(MONDAY)  # major ticks on the mondays
alldays = DayLocator()  # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
# ax.xaxis.set_minor_formatter(dayFormatter)

# plot_day_summary(ax, quotes, ticksize=3)
candlestick_ohlc(ax, quotes, width=0.6)

ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()

print('end')
