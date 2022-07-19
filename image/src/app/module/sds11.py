from sds011 import *
from time import *



sensor = SDS011("/dev/ttyUSB0")

def get_data(n=3):
    sensor.sleep(sleep=False)
    pmt_2_5 = 0
    pmt_10 = 0
    time.sleep(10)
    for i in range (n):
        x = sensor.query()
        pmt_2_5 = pmt_2_5 + x[0]
        pmt_10 = pmt_10 + x[1]
        time.sleep(2)
    pmt_2_5 = round(pmt_2_5/n, 1)
    pmt_10 = round(pmt_10/n, 1)
    sensor.sleep(sleep=True)
    time.sleep(2)
    return pmt_2_5, pmt_10

def conv_aqi(pmt_2_5, pmt_10):
    aqi_2_5 = aqi.to_iaqi(aqi.POLLUTANT_PM25, str(pmt_2_5))
    aqi_10 = aqi.to_iaqi(aqi.POLLUTANT_PM10, str(pmt_10))
    return aqi_2_5, aqi_10

# def save_log(): 
#     with open("YOUR PATH HERE/air_quality.csv", "a") as log:
#         timestamp = time.time()
#         log.write("{},{},{},{},{}\n".format(timestamp, pmt_2_5, aqi_2_5,       pmt_10,aqi_10))
#         log.close()

while(True): 
    pmt_2_5, pmt_10 = get_data()
    aqi_2_5, aqi_10 = conv_aqi(pmt_2_5, pmt_10)
    try:
        print("PM2.5 : ",pmt_2_5, "PM10 : ",pmt_10 )
        print("AQI_2.5 : ", aqi_2_5 ,"AQI_1O : ", aqi_10 )
    except:
        print ("[INFO] Failure in logging data") 
    time.sleep(1)