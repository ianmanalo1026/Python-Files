import psycopg2
from pycoingecko import CoinGeckoAPI
import datetime



con = psycopg2.connect(
    database="sample",
    user="postgres",
    password='soulgun21',
    host='127.0.0.1',
    port='5433'
)

cur = con.cursor()

#cur.execute("CREATE TABLE data_sample (id SERIAL PRIMARY KEY, categories VARCHAR, time_and_date VARCHAR, prices VARCHAR);")

#cur.execute("INSERT INTO data_sample (categories) VALUES(%s)", ("Ian",))
cg = CoinGeckoAPI()
content = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='usd', from_timestamp='1609718400', to_timestamp='1609804800')

for key, values in content.items():
    for value in values:
        prices = round(value[1],2)
        converted = str(value[0])[:-3]
        time_and_date = datetime.datetime.fromtimestamp(int(converted)).strftime("%x %X")
        cur.execute("INSERT INTO data_sample (categories, time_and_date, prices) VALUES(%s, %s, %s);", (key, time_and_date,prices,))

cur.execute("SELECT * FROM data_sample")
print(cur.fetchall())
con.commit()

cur.close()
con.close()