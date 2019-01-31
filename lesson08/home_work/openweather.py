
""" 
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.
    
    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID, 
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys
        
        Ключ имеет смысл сохранить в локальный файл, например, "app.id"

        
== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz
    
    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка 
     (воспользоваться модулем gzip 
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)
    
    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}
    
    
== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}    


== Сохранение данных в локальную БД ==    
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну 
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""

import requests
import sqlite3
import gzip
import json
import os
import collections
import datetime

def get_appkey():
    """
    Read key from file 'app.id' and delete non-key symbols.

    """
    with open('app.id', 'r') as f:
        return f.readlines()[1].strip()

def get_cities():
    """
    Get data about weather in cities in form of list of dicts like this:
    {"id":int,"name":str,"country":str,"coord":{"lon":float,"lat":float}}
    from site openweather.org

    """
    req = requests.get('http://bulk.openweathermap.org/sample/city.list.json.gz')
    if not os.path.exists('city.list.json.gz'):
        with open('city.list.json.gz', 'wb') as f:
            f.write(req.content)
    with gzip.open('city.list.json.gz', 'rb') as f:
        data_binary = f.read()
    data = json.loads(data_binary.decode('utf-8'))
    return data

City_weather = collections.namedtuple("City_weather",
        "id_city, city_name, date_today, temperature, id_weather")

def get_cities_weather(cities, cities_data=get_cities()):
    """
    Get weather data about given list of cities, 
    using http request to opeanweatermap.org

    cities_data - list of all the cities data. 
    See get_cities

    Output data: list of
    City_weather(id_city, city_name, date_today, temperature, id_weather)
    
    """
    cities_ids = ''
    cities_names = []
    for city in cities:
        for line in cities_data:
            if line['name'] == city:
                cities_ids += str(line['id']) + ','
                cities_names.append(city)

    cities_ids = cities_ids[:-1] # delete last comma
    
    # make request
    pattern = \
    """http://api.openweathermap.org/data/2.5/group?id={cities_ids}&units=metric&appid={appkey}"""

    content = requests.get(
                pattern.format(cities_ids=cities_ids,
                               appkey=get_appkey())
              ).content
    
    # clear content
    content = json.loads(content.decode('utf-8'))['list']

    def convertT(x):
        return x - 273.15 if x > 200 else x
    
    # fill data structure
    cities_ids = list(map(int, cities_ids.split(',')))
    list_ = []
    for i, rec in enumerate(content):
        list_.append(
                City_weather(cities_ids[i], cities_names[i],
                    datetime.date.today(), convertT(rec['main']['temp']),
                    rec['weather'][0]['id'])
                )
    return list_ 

class Weather:

    def __init__(self):
        self.db = 'weather.db'
        self.cities_data = get_cities()
        if not os.path.exists('weather.db'):
            with sqlite3.connect(self.db) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE weather(
                        id_city     text primary key,
                        city_name   text,
                        date_today  date,
                        temperature text,
                        id_weather  text
                    );
                """)

    def get_cities_weather(self):
        """
        Input cities names into console and see the weather. 
        Also add all new data to the database.
        
        """
        cities_list = input("Input cities list (like: Novinki Moscow] -> ")
        cities_list = cities_list.split()
        
        cities_weather = get_cities_weather(cities_list, self.cities_data) 
        print("Weather info:")
        for cw in cities_weather:
            print(cw)
        print("updating database ...")
        
        # adding new data to database
        with sqlite3.connect(self.db) as conn:
            cursor = conn.cursor()
            for cw in cities_weather:
                cursor.execute("""
                    INSERT INTO weather
                    VALUES ('{id_city}',
                            '{city_name}',
                            '{date_today}',
                            '{temperature}',
                            '{id_weather}'
                            );
                    """.format(**cw._asdict())
                    )

        print("update complete")

    def get_data_by_cityname(self, cityname):
        """
        Get weather data from local database.
        Input: str cityname
        Output: list of
            City_weather(id_city, city_name, date_today, temperature, id_weather)

        """
        with sqlite3.connect(self.db) as conn:
            cur = conn.cursor()
            sql = "SELECT * FROM weather WHERE city_name=?"
            cur.execute(sql, [(cityname)])
            results = cur.fetchall()

        output = []
        for line in results:
            output.append(City_weather(*line))
        return output
