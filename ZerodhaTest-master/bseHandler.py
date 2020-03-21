import zipfile, requests, io, csv, redis
from datetime import date, datetime , timedelta
from bs4 import BeautifulSoup


TARGET_URL = 'https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx'
ZIP_URL = ''

def genFileName(): #not used
    ''' generates filename for url as well gives date for which file is fetched - can be used for validation '''
    date_today = datetime.strftime(datetime.now() - timedelta(1), '%d%m%y')
    url_file_name = 'EQ'+str(date_today)+'_CSV'
    file_name = url_file_name.replace('_','.')
    return url_file_name, file_name , date_today

def redisClient():
    #return redis.Redis.from_url("redis://127.0.0.1:6379",db=0,charset='utf-8', decode_responses=True)
    return redis.Redis.from_url("redis://127.0.0.1:6379",db=0)
    #return redis.StrictRedis(host='localhost',port=6379,db=0)

def zipFromBSE():
    global ZIP_URL
    try: 
        _page = requests.get(TARGET_URL)
        soup_obj = BeautifulSoup(_page.content,'lxml')
        ZIP_URL = soup_obj.find('li').contents[1].attrs.get('href')
        zip_file = requests.get(ZIP_URL)
        z = zipfile.ZipFile(io.BytesIO(zip_file.content))
        z.extractall('zips')
        return str('zips' + '/' + z.namelist()[0])
    except Exception as ex: 
        raise ("There was a issue in zipfile extraction from URL: " +  str(ex))

def saveToRedis(): #call zipFromBSE
    '''initiates redis connection and stored data of zip'''
    client = redisClient()
    client.flushall() #clear existing records if any
    csv_values = csv.DictReader(open(zipFromBSE(), 'r'))
    for row in csv_values:
        client.hmset(row['SC_NAME'].rstrip(), dict(row))
    client.set('FetchDate', str(datetime.today()))
    client.set('Source', str(ZIP_URL))

def stockByName(name):
    _data = []
    client = redisClient()
    for rec in client.scan_iter( match= '*'+str(name.upper())+'*', count= 5):
        _data.append(client.hgetall(rec)) if rec else None
    return _data

def getOperationDetails():
    client = redisClient()
    _fetchDate = client.get('FetchDate')
    if _fetchDate:
        datetime_object = datetime.strptime(_fetchDate.decode(), '%Y-%m-%d %H:%M:%S.%f')
        date_object = str(datetime_object.date())
        time_object = str(datetime_object.time())
        time_object = time_object.split('.')
        #_source = client.get('Source')
        _source = None
        return date_object, time_object[0],  _source

def stockTopTen():
    data = []
    ignoreList = ['FetchDate' , 'Source']
    client = redisClient()
    keys = client.keys('*')
    for stock in keys:
        if str(stock) not in ignoreList:
            try:
                #data.append({client.hgetall(stock).items()})  
                data.append({k.decode("utf-8"):v.decode("utf-8") for k,v in client.hgetall(stock).items()})  
            except:
                pass     
    sortedData = sorted(data, key=lambda x: (float(x['PREVCLOSE'])-float(x['CLOSE']))/float(x['LAST']))
    sortedData = sortedData[:10]
    #sortedData = sortedData.reverse()
    return sortedData
