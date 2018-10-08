# 谷歌.py
import pandas as pd
from pandas_datareader import data as pdr
import datetime
import fix_yahoo_finance as yf
import matplotlib.pyplot as plt
yf.pdr_override()
finace = pdr.get_data_yahoo("0939.HK",start=datetime.datetime(2017,9,21),end=datetime.datetime(2018,10,8))
print(finace.tail(20))

import matplotlib.pyplot as plt
plt.plot(finace.index,finace["Open"])
plt.show()


# ~  sudo rm -rf /var/lib/dpkg/lock

# ~     sudo rm -rf /var/cache/apt/archives/lock

# ~     sudo apt-get update
