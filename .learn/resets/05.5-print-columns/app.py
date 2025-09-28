#print("Hello World")
import pandas as pd
data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
#print(data_frame)

#edades = pd.Series([23, 45, 7, 34, 6, 63, 36, 78, 54, 34])
#print(edades)

#años = pd.date_range(start='2021-05-01', end='2021-05-12')
#print(años)

#my_series = pd.Series([2, 4, 6, 8, 10])
#new_serie = my_series.apply(lambda x: x/2)
#print(new_serie)

#data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
#df = pd.DataFrame(data, columns=['Brand','Model','Color'])
#print(df)

data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    },
    {
        "brand": "Tesla", 
        "model": "Model S",
        "color": "Red"
    }
]

df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data_frame)
print(df.iloc[133,6])

print(df.head(3))
print(df.tail(3))
print(df.head(10)['Name','Type 1'])