import psycopg2
from pycoingecko import CoinGeckoAPI
import schedule
import datetime
import time


class TickerScheduler():
    
    def ticker_trigger(self):
        cg = CoinGeckoAPI()
        content = cg.get_price(ids=['bitcoin', 'ripple', 'ethereum'], vs_currencies=["php","usd","eur"])
        print(content)

    def ticker_timer(self):
        print('Timestamp: {:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()))
        

class HistoricalData():
    
    
    def data_download(self):
        con = psycopg2.connect(
            database="sample",
            user="postgres",
            password='soulgun21',
            host='127.0.0.1',
            port='5433'
            )
        cur = con.cursor()
        content = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='usd', from_timestamp='1609718400', to_timestamp='1609804800')
        for key, values in content.items():
            for value in values:
                prices = round(value[1],2)
                converted = str(value[0])[:-3]
                time_and_date = datetime.datetime.fromtimestamp(int(converted)).strftime("%x %X")
                cur.execute("INSERT INTO data_sample (categories, time_and_date, prices) VALUES(%s, %s, %s);", (key, time_and_date,prices,))

        print("Database has been updated")
        cur.execute("SELECT * FROM data_sample")
        con.commit()

        cur.close()
        con.close()
    
show = TickerScheduler()

schedule.every(5).seconds.do(show.ticker_timer)
schedule.every(5).seconds.do(show.ticker_trigger)

while True:
    schedule.run_pending()
    time.sleep(1)



"""      


class DownloadData(TickerScheduler):
    



    
        schedule.every(5).seconds.do(data_transfer)

        while True:
            schedule.run_pending()
            time.sleep(10)


    
    
    
    
#cur.execute("CREATE TABLE data_sample (id SERIAL PRIMARY KEY, categories VARCHAR, time_and_date VARCHAR, prices VARCHAR);")

#cur.execute("INSERT INTO data_sample (categories) VALUES(%s)", ("Ian",))
"""