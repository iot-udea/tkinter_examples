import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

""" 
-----------------------  Datos  -----------------------  
"""
Data1 = {
        'Country': ['US','CA','GER','UK','FR'],
        'GDP_Per_Capita': [45000,42000,52000,49000,47000]
}
df1 = DataFrame(Data1, columns= ['Country', 'GDP_Per_Capita'])
df1 = df1[['Country', 'GDP_Per_Capita']].groupby('Country').sum()

Data2 = {
       'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
       'Unemployment_Rate': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
}  
df2 = DataFrame(Data2,columns=['Year','Unemployment_Rate'])
df2 = df2[['Year', 'Unemployment_Rate']].groupby('Year').sum()

Data3 = {
       'Interest_Rate': [5,5.5,6,5.5,5.25,6.5,7,8,7.5,8.5],
       'Stock_Index_Price': [1500,1520,1525,1523,1515,1540,1545,1560,1555,1565]
}  
df3 = DataFrame(Data3,columns=['Interest_Rate','Stock_Index_Price'])

"""
-----------------------  Ventana principal  -----------------------  
"""

# Creacion de la ventana principal
root= tk.Tk() 

# ---------------------------------------------------------------------------
# Paso 1: Agregando los elementos en la ventana principal
# ---------------------------------------------------------------------------

# 1 -> figure1
figure1 = plt.Figure(figsize=(4,6), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)  
df1.plot(kind='bar', legend=True, ax=ax1, fontsize=8)
ax1.set_title('Country Vs. GDP Per Capita')

# 2 -> figure2
figure2 = plt.Figure(figsize=(4,6), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH) 
df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=8)   
ax2.set_title('Year Vs. Unemployment Rate')

# 2 -> figure3
figure3 = plt.Figure(figsize=(4,6), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Interest_Rate'],df3['Stock_Index_Price'], color = 'g')
scatter3 = FigureCanvasTkAgg(figure3, root) 
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend() 
ax3.tick_params(axis='both', labelsize=8)
ax3.set_xlabel('Interest Rate')
ax3.set_title('Interest Rate Vs. Stock Index Price')


root.mainloop()