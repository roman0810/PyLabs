import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("m_fact.csv" , sep=";" , encoding = "cp1251" , encoding_errors = "ignore" , header = 0 , decimal = ",")
df_man = pd.read_csv("m_manager.csv" , sep=";" , encoding = "cp1251" , encoding_errors = "ignore" , header = 0 , decimal = ",")
df_Office = pd.read_csv("m_office.csv" , sep=";" , encoding = "cp1251" , encoding_errors = "ignore" , header = 0 , decimal = ",")

lst = []

for manID in df_man["ID"].tolist():
	dff = df_man[df_man["ID"] == manID]
	manFIO = dff.loc[:,"Фамилия"] + " " + dff.loc[:,"Имя"]

	df_Iman = df[df["Менеджер ID"] == manID]
	df_Iman = df_Iman[["Количество" , "Сумма"]]

	df_ImanSum = df_Iman.sum()

	lst.append([manID , manFIO.iloc[0]] + df_ImanSum.tolist())
df_man = pd.DataFrame(lst , columns = ["ID" , "NAME" , "QANTITY" , "SUM"])
df_man = df_man.sort_values(by = ["SUM"])
print(df_man)

