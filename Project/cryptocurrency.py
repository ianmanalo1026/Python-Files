import psycopg2
from pycoingecko import CoinGeckoAPI
import schedule
from datetime import datetime
from time import mktime
import time


class CrytoTicker:
    
    def __init__(self):
        self.cg = CoinGeckoAPI()
    
    def ping(self):
        status_code = self.cg.ping()
        print(status_code)
    
    def get_price(self):
        content = self.cg.get_price(ids=['bitcoin', 'ripple', 'ethereum'], vs_currencies=["php","usd","eur"])
        return content

    
class TimeControl(CrytoTicker):
    
    def __init__(self):
        super().__init__()
        self.date_time = None
        self.date_time_database = None
        self.unix_time = None
    
    def running_datetime(self):
        self.date_time = datetime.now()
        return self.date_time
        
    def datetime_database(self):
        self.running_datetime()
        date = datetime.now()
        self.date_time_database = date.strftime("%Y-%m-%d %H:%M:%S")
        return self.date_time_database

    def convert_to_unixtime(self):
        self.datetime_database()
        self.unix_time = mktime(self.date_time.timetuple())
        return self.unix_time
        
    def run_all_time(self):
        self.running_datetime()
        self.datetime_database()
        self.convert_to_unixtime()
    
class GetData(TimeControl):
    
    def __init__(self):
        super().__init__()
        self.bit_key = None
        self.bit_php = None
        self.bit_usd = None
        self.bit_eur = None
        
        self.eth_key = None
        self.eth_php = None
        self.eth_usd = None
        self.eth_eur = None
        
        self.xrp_key = None
        self.xrp_php = None
        self.xrp_usd = None
        self.xrp_eur = None
        
    def get_bitcoin(self):
        self.bit_key = "bitcoin"
        self.bit_php = self.get_price()[self.bit_key]["php"]
        self.bit_usd = self.get_price()[self.bit_key]["usd"]
        self.bit_eur = self.get_price()[self.bit_key]["eur"]
        
    def get_ethereum(self):
        self.eth_key = "ethereum"
        self.eth_php = self.get_price()[self.eth_key]["php"]
        self.eth_usd = self.get_price()[self.eth_key]["usd"]
        self.eth_eur = self.get_price()[self.eth_key]["eur"]
        
    def get_ripple(self):
        self.xrp_key = "ripple"
        self.xrp_php = self.get_price()[self.xrp_key]["php"]
        self.xrp_usd = self.get_price()[self.xrp_key]["usd"]
        self.xrp_eur = self.get_price()[self.xrp_key]["eur"]
        
    def arrange_data(self):
        self.get_bitcoin()
        self.get_ethereum()
        self.get_ripple()
        self.run_all_time()
        date = self.date_time_database
        data = {"Time": self.date_time_database, "Unix Time": self.unix_time, "Bitcoin": self.bit_php, "Ethereum": self.eth_php, "Ripple": self.xrp_php  }
        print(data)


class Database(GetData):
    
    def __init__(self):
        super().__init__()
        self.con = psycopg2.connect(
                                    database="sample",
                                    user="postgres",
                                    password='soulgun21',
                                    host='127.0.0.1',
                                    port='5433'
                                    )
        self.cur = self.con.cursor()
    
    def create_table(self):
        self.cur.execute("CREATE TABLE Cryptocurrency (id SERIAL PRIMARY KEY, time_and_date VARCHAR, unix_time VARCHAR, bitcoin_price VARCHAR, ethereum_price VARCHAR, ripple_price VARCHAR);")
        self.cur.close()
        self.con.commit()
        self.con.close()
        print("Succesfully created a table")
    
    def store_data(self):
        self.arrange_data()
        self.cur.execute("INSERT INTO data_sample (time_and_date, unix_time, bitcoin_price, ethereum_price, ripple_price) VALUES(%s, %s, %s, %s, %s);", (self.date_time_database, self.unix_time, self.bit_php, self.eth_php, self.xrp_php))
        self.cur.close()
        self.con.commit()
        self.con.close()

main_prog = Database()
        
# def main():
#      main_prog.store_data()
     

# main()     
        
        
        
        
        

schedule.every(5).seconds.do(main_prog.arrange_data)

while True:
    schedule.run_pending()
    time.sleep(1)
        
# class HistoricalData():
    
    
#     def data_download(self):
#         con = psycopg2.connect(
#             database="sample",
#             user="postgres",
#             password='soulgun21',
#             host='127.0.0.1',
#             port='5433'
#             )
#         cur = con.cursor()
#         content = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='usd', from_timestamp='1609718400', to_timestamp='1609804800')
#         for key, values in content.items():
#             for value in values:
#                 prices = round(value[1],2)
#                 converted = str(value[0])[:-3]
#                 time_and_date = datetime.datetime.fromtimestamp(int(converted)).strftime("%x %X")
#                 cur.execute("INSERT INTO data_sample (categories, time_and_date, prices) VALUES(%s, %s, %s);", (key, time_and_date,prices,))

#         print("Database has been updated")
#         cur.execute("SELECT * FROM data_sample")
#         con.commit()

#         cur.close()
#         con.close()
    


# schedule.every(5).seconds.do(main_prog.arrange_data)



"""      


class DownloadData(TickerScheduler):
    



    
        schedule.every(5).seconds.do(data_transfer)

        while True:
            schedule.run_pending()
            time.sleep(10)


    
    
    
    
#cur.execute("CREATE TABLE data_sample (id SERIAL PRIMARY KEY, categories VARCHAR, time_and_date VARCHAR, prices VARCHAR);")

#cur.execute("INSERT INTO data_sample (categories) VALUES(%s)", ("Ian",))
"""