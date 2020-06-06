# easyOpenWeather module

This module is used to get or print the weather deatils using open weather API easily

install module using pip command
```shell
pip install easyOpenWeather
```

### external dependencies required - 
1. requests
```shell
pip install requests
```

2. tabulate
```shell
pip install tabulate
```


To import in project - 
```python
from easyOpenWeather import module
```

Then make a object instance of WeatherDataClass
```python
obj = module.WeatherDataClass()
```

Now you need to at least set the city name and api key first
```python
obj.setCityName("london")
obj.setApiKey("fe82651e607e4******ba45e39aa7e17")
```

To know how to get your own api key from open weather [click here](https://openweathermap.org/appid#:~:text=1.,activated%20and%20ready%20to%20use.)

Now you need to pass a list containing attributes for which you need weather data

List Attributes - 
1.  temp        		-> for temperature in kelvin
2.  tempInC     		-> for temperature in celcius
3.  tempInF     		-> for temperature in f
4.  tempMin     		-> for min temp - unit is decided from above 
5.  tempMax     		-> for max temp - unit is decided from above
6.  pressure			-> for pressure 
7.  humidity			-> for humidity
8.  wind speed			-> for wind speed 
9.  wind direction 		-> for wind direction
10. description  		-> for description - like clear sky etc

##### Note - use only one at a time from temp , tempInC , tempInF

##### All output data is in SI units

To set list Use - 
```python
listPass = ["tempInC" , "tempMin" , "tempMax" , "pressure" , "humidity" , "windSpeed" , "windDirection" , "clouds" , "description"]
obj.setList(listPass)
```

To get data in dictionary format - 
```python
obj.getInfo()
```

The function will return a dictionary.

Sample dictionary that you will get for listPass = ["tempInC" , "tempMin" , "tempMax" , "pressure" , "humidity" , "windSpeed" , "windDirection" , "clouds" , "description"] :

{'tempInC': 11.01, 'tempMin': 10.71, 'tempMax': 11.82, 'pressure': 998, 'humidity': 53, 'windSpeed': 8.7, 'windDirection': 260, 'clouds': 9, 'description': 'clear sky'}


This module also include a inbuilt function to directly print the data in a tabular format
```python
obj.printData()
```

Other methods - 
1. obj.setStringKey(stringKey) - To set custom api url. Default url - https://api.openweathermap.org/data/2.5/weather?q=
	
   Some getters - 
2. obj.getStringKey()
3. obj.getApiKey()
4. obj.getCityName()


### Sample program - 
```python 
from easyOpenWeather import module

obj = module.WeatherDataClass()

obj.setCityName("london")
obj.setApiKey("fe82651e607e46db61dba45e39aa7e17")
    
listPass = ["tempInC" , "tempMin" , "tempMax" , "pressure" , "humidity" , "windSpeed" , "windDirection" , "clouds" , "description"]

obj.setList(listPass)
obj.printData()
```

### Contibute - 

[Post any issues on github](https://github.com/harshnative/nativeOpenWeather_Module)

[Check out code on github](https://github.com/harshnative/nativeOpenWeather_Module)