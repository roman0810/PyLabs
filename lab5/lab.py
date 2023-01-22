import pandas as pd
df_xlc = pd.read_excel('mobile.xlsx',header=0) # читаем excel файл
print(df_xlc.head(15)) # смотрим что там есть - первые 15 записей
print(df_xlc.columns)
ds_proizv = df_xlc["Производитель"];
print (ds_proizv.head(50))
print (ds_proizv.tail(50))
lost = ds_proizv.tolist() # преобразовать в список
print(set(lost))

df_sony = df_xlc[df_xlc['Производитель']=="Sony"]
print(df_sony.head())
df_sony_filt = df_sony[['Производитель', 'Категория', 'Имя товара','Цена','Количество']]
print(df_sony_filt.head())


print(df_sony_filt. head())
df_sony_filt.loc[:,"Сумма"] = df_sony_filt.loc[:,'Количество'] * df_sony_filt.loc[:,'Цена']


print(df_sony_filt.head())
print(df_sony_filt.sum())
