#print("Hello World")
import pandas as pd
#data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
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

#df = pd.DataFrame(data)
#print(df)

#df = pd.DataFrame(data_frame)
#print(df.iloc[133,6])

#print(df.head(3))

#print(df.tail(3))

#print(df[['Name','Type 1']][0:10])

#print(df.loc[df['Attack']>80])

#print(len(df.loc[df['Legendary'] == True]))

baby_names = pd.read_csv(".learn/assets/us_baby_names_right.csv")
#print(baby_names.head())

#del baby_names[baby_names.columns[0]]

#print(baby_names.head(5))

#print(baby_names.value_counts('Gender'))

print(len(sum(baby_names.groupby('Name'))))
