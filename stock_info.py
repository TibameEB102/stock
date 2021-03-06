import requests
import numpy as np
import pandas as pd

# 取得股市相關資訊
url = 'https://quality.data.gov.tw/dq_download_json.php?nid=11549&md5_url=bb878d47ffbe7b83bfc1b41d0b24946e'
r = requests.get(url)
data = pd.DataFrame(r.json())

data.to_csv('data/stock_info.csv', index=False, header = True,encoding='utf-8-sig')
