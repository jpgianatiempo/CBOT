#%%
#region Update Data
from os import close
import investpy
import pandas as pd
import plotly as plt

from datetime import datetime
hoy = datetime.today().strftime('%d/%m/%Y')

for grains in ["soybean","corn","wheat","soybean oil","soybean meal"]:
    search_result = investpy.search_quotes(text=grains, products=['commodities'],
                                       countries=['united states'], n_results=1)
    globals()[grains.replace(" ", "")] = search_result.retrieve_historical_data(from_date='01/01/1990', to_date=hoy)

#convierto a df
corn = pd.DataFrame(corn)
soybean = pd.DataFrame(soybean)
wheat = pd.DataFrame(wheat)
aceite = pd.DataFrame(soybeanoil)
harina = pd.DataFrame(soybeanmeal)

#acomodar las fechas ¿?
#corn = corn.loc['1990-01-02':]

#convierto a usd/tn
coef_soja = 0.367454
coef_trigo = 0.367437
coef_maiz = 0.39368
coef_aceite = 22.046
coef_harina = 1.1023

base_maiz = 93.59742
base_soja = 206.2335575
base_trigo = 150.1898738
base_aceite = 406.30778
base_harina = 198.08331

corn = corn.assign(Open = lambda x: x['Open'] * coef_maiz,
                   High = lambda x: x['High'] * coef_maiz,
                   Low = lambda x: x['Low'] *  coef_maiz, 
                   Close = lambda x: x['Close'] * coef_maiz,
                   Volatilidad = lambda x: x['High'] - x['Low'],
                   SMA_Volatilidad = lambda x: x["Volatilidad"].rolling(window=20).mean(),
                   Base_100_Close = lambda x: x['Close'] / base_maiz * 100,
                   SMA_Base_100_Close = lambda x: x["Base_100_Close"].rolling(window=20).mean(),
                   Grano = "Maiz")

soybean = soybean.assign(Open = lambda x: x['Open'] * coef_soja,
                   High = lambda x: x['High'] * coef_soja,
                   Low = lambda x: x['Low'] *  coef_soja, 
                   Close = lambda x: x['Close'] * coef_soja,
                   Volatilidad = lambda x: x['High'] - x['Low'],
                   SMA_Volatilidad = lambda x: x["Volatilidad"].rolling(window=20).mean(),
                   Base_100_Close = lambda x: x['Close'] / base_soja * 100,
                   SMA_Base_100_Close = lambda x: x["Base_100_Close"].rolling(window=20).mean(),
                   Grano = "Soja")

wheat = wheat.assign(Open = lambda x: x['Open'] * coef_trigo,
                   High = lambda x: x['High'] * coef_trigo,
                   Low = lambda x: x['Low'] *  coef_trigo, 
                   Close = lambda x: x['Close'] * coef_trigo,
                   Volatilidad = lambda x: x['High'] - x['Low'],
                   SMA_Volatilidad = lambda x: x["Volatilidad"].rolling(window=20).mean(),
                   Base_100_Close = lambda x: x['Close'] / base_trigo * 100,
                   SMA_Base_100_Close = lambda x: x["Base_100_Close"].rolling(window=20).mean(),
                   Grano = "Trigo")


aceite = aceite.assign(Open = lambda x: x['Open'] * coef_aceite,
                   High = lambda x: x['High'] * coef_aceite,
                   Low = lambda x: x['Low'] *  coef_aceite, 
                   Close = lambda x: x['Close'] * coef_aceite,
                   Volatilidad = lambda x: x['High'] - x['Low'],
                   SMA_Volatilidad = lambda x: x["Volatilidad"].rolling(window=20).mean(),
                   Base_100_Close = lambda x: x['Close'] / base_aceite * 100,
                   SMA_Base_100_Close = lambda x: x["Base_100_Close"].rolling(window=20).mean(),
                   Grano = "Aceite de Soja")


harina = harina.assign(Open = lambda x: x['Open'] * coef_harina,
                   High = lambda x: x['High'] * coef_harina,
                   Low = lambda x: x['Low'] *  coef_harina, 
                   Close = lambda x: x['Close'] * coef_harina,
                   Volatilidad = lambda x: x['High'] - x['Low'],
                   SMA_Volatilidad = lambda x: x["Volatilidad"].rolling(window=20).mean(),
                   Base_100_Close = lambda x: x['Close'] / base_harina * 100,
                   SMA_Base_100_Close = lambda x: x["Base_100_Close"].rolling(window=20).mean(),
                   Grano = "Harina de Soja")


df = pd.concat([corn, soybean, wheat, aceite, harina])

#df.to_csv("./Cbot.csv", encoding='utf-8')
df.to_excel("p:/Estudios_Gerencia/Balances/Precios/CBOT/Data/Cbot.xlsx",index=True)

#endregion Update data


#%%
#region Graficos volatilidad
import plotly.express as px

fig = px.line(corn.reset_index(), x='Date', y="SMA_Volatilidad",
template='simple_white', title="Volatilidad intradiaria del maíz en CBOT")
fig.update_xaxes(title_text='Fecha',nticks=16)
fig.update_yaxes(title_text='Volatilidad intradiaria (usd/tn)')
fig.write_html("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Maiz_volatilidad_intradiaria.html")

fig = px.line(wheat.reset_index(), x='Date', y="SMA_Volatilidad",
template='simple_white', title="Volatilidad intradiaria del trigo en CBOT")
fig.update_xaxes(title_text='Fecha',nticks=16)
fig.update_yaxes(title_text='Volatilidad intradiaria (usd/tn)')
fig.update_traces(line_color='#147852')
fig.write_html("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Trigo_volatilidad_intradiaria.html")

fig = px.line(soybean.reset_index(), x='Date', y="SMA_Volatilidad",
template='simple_white', title="Volatilidad intradiaria de la soja en CBOT")
fig.update_xaxes(title_text='Fecha',nticks=16)
fig.update_yaxes(title_text='Volatilidad intradiaria (usd/tn)')
fig.update_traces(line_color='#FECB52')
fig.write_html("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Soja_volatilidad_intradiaria.html")

fig = px.line(aceite.reset_index(), x='Date', y="SMA_Volatilidad",
template='simple_white', title="Volatilidad intradiaria del aceite de soja en CBOT")
fig.update_xaxes(title_text='Fecha',nticks=16)
fig.update_yaxes(title_text='Volatilidad intradiaria (usd/tn)')
fig.update_traces(line_color='#5E069D')
fig.write_html("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Aceite_Soja_volatilidad_intradiaria.html")

fig = px.line(harina.reset_index(), x='Date', y="SMA_Volatilidad",
template='simple_white', title="Volatilidad intradiaria de la harina de soja en CBOT")
fig.update_xaxes(title_text='Fecha',nticks=16)
fig.update_yaxes(title_text='Volatilidad intradiaria (usd/tn)')
fig.update_traces(line_color='#576675')
fig.write_html("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Harina_Soja_volatilidad_intradiaria.html")


#endregion


#%%
#region Graficos de precios
from plotnine import *
from mizani.breaks import date_breaks
from mizani.formatters import date_format

myPlot = (
    ggplot(corn.reset_index())  # What data to use
    + aes(x="Date", y="Close", color="Close")  # What variable to use
    + geom_line()+
    #facet_wrap(facets="Grano", scales="free_y")+
    labs(title="Maíz: Primera posición CBOT",
         subtitle="En dólares por tonelada",
         y = "Precio de cierre (usd/tn)",
         x = "Fecha")+
    scale_color_continuous(guide=False)+
    scale_x_datetime(breaks=date_breaks('3 years'), labels=date_format('%Y'))+
    theme_bw() # Geometric object to use for drawing
)
myPlot.save("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Precio_Maíz.png", dpi=600)

myPlot = (
    ggplot(soybean.reset_index())  # What data to use
    + aes(x="Date", y="Close", color="Close")  # What variable to use
    + geom_line()+
    #facet_wrap(facets="Grano", scales="free_y")+
    labs(title="Soja: Primera posición CBOT",
         subtitle="En dólares por tonelada",
         y = "Precio de cierre (usd/tn)",
         x = "Fecha",
         fill = "Precio de cierre (usd/tn)")+
    scale_color_continuous(guide=False)+
    scale_x_datetime(breaks=date_breaks('5 years'), labels=date_format('%Y'))+
    theme_bw() # Geometric object to use for drawing
)
myPlot.save("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Precio_Soja.png", dpi=600)

myPlot = (
    ggplot(wheat.reset_index())  # What data to use
    + aes(x="Date", y="Close", color="Close")  # What variable to use
    + geom_line()+
    #facet_wrap(facets="Grano", scales="free_y")+
    labs(title="Trigo: Primera posición CBOT",
         subtitle="En dólares por tonelada",
         y = "Precio de cierre (usd/tn)",
         x = "Fecha",
         fill = "Precio de cierre (usd/tn)")+
    scale_color_continuous(guide=False)+
    scale_x_datetime(breaks=date_breaks('5 years'), labels=date_format('%Y'))+
    theme_bw() # Geometric object to use for drawing
)
myPlot.save("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Precio_Trigo.png", dpi=600)


myPlot = (
    ggplot(aceite.reset_index())  # What data to use
    + aes(x="Date", y="Close", color="Close")  # What variable to use
    + geom_line()+
    #facet_wrap(facets="Grano", scales="free_y")+
    labs(title="Aceite de Soja: Primera posición CBOT",
         subtitle="En dólares por tonelada",
         y = "Precio de cierre (usd/tn)",
         x = "Fecha",
         fill = "Precio de cierre (usd/tn)")+
    scale_color_continuous(guide=False)+
    scale_x_datetime(breaks=date_breaks('5 years'), labels=date_format('%Y'))+
    theme_bw() # Geometric object to use for drawing
)
myPlot.save("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Precio_Aceite_Soja.png", dpi=600)

myPlot = (
    ggplot(harina.reset_index())  # What data to use
    + aes(x="Date", y="Close", color="Close")  # What variable to use
    + geom_line()+
    #facet_wrap(facets="Grano", scales="free_y")+
    labs(title="Harina de Soja: Primera posición CBOT",
         subtitle="En dólares por tonelada",
         y = "Precio de cierre (usd/tn)",
         x = "Fecha",
         fill = "Precio de cierre (usd/tn)")+
    scale_color_continuous(guide=False)+
    scale_x_datetime(breaks=date_breaks('5 years'), labels=date_format('%Y'))+
    theme_bw() # Geometric object to use for drawing
)
myPlot.save("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Precio_Harina_Soja.png", dpi=600)

#endregion


#%%
#region Histograma de precios


myPlot = (
    ggplot(soybean.reset_index())  # What data to use
    + aes(x="Close")  # What variable to use
    + geom_histogram()+
    #facet_wrap(facets="Grano", scales="free_y")+
    labs(title="Histograma del precio de la soja primera posición CBOT",
         subtitle="En dólares por tonelada",
         y = "Frecuencia",
         x = "Precio de cierre (usd/tn)",
         fill = "Precio de cierre (usd/tn)")+
    theme_bw() +
    geom_vline(xintercept = soybean.Close[-1], linetype="dotted", 
                color = "blue", size=1.5)+ # Geometric object to use for drawing
    annotate('text', color = "blue", x=soybean.Close[-1]+30, y = 50, label=str(int(len(soybean[soybean["Close"] > soybean.Close[-1]]) / len(soybean) * 100))+"%")
)
myPlot.save("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Histograma_Soja.png", dpi=600)


myPlot = (
    ggplot(wheat.reset_index())  # What data to use
    + aes(x="Close")  # What variable to use
    + geom_histogram()+
    #facet_wrap(facets="Grano", scales="free_y")+
    labs(title="Histograma del precio del trigo primera posición CBOT",
         subtitle="En dólares por tonelada",
         y = "Frecuencia",
         x = "Precio de cierre (usd/tn)",
         fill = "Precio de cierre (usd/tn)")+
    theme_bw() +
    geom_vline(xintercept = wheat.Close[-1], linetype="dotted", 
                color = "red", size=1.5)+ # Geometric object to use for drawing
    annotate('text', color = "red", x=wheat.Close[-1]+25, y = 35, label=str(int(len(wheat[wheat["Close"] > wheat.Close[-1]]) / len(wheat) * 100))+"%")
)
myPlot.save("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Histograma_Trigo.png", dpi=600)



myPlot = (
    ggplot(corn.reset_index())  # What data to use
    + aes(x="Close")  # What variable to use
    + geom_histogram()+
    #facet_wrap(facets="Grano", scales="free_y")+
    labs(title="Histograma del precio del maíz primera posición CBOT",
         subtitle="En dólares por tonelada",
         y = "Frecuencia",
         x = "Precio de cierre (usd/tn)",
         fill = "Precio de cierre (usd/tn)")+
    theme_bw() +
    geom_vline(xintercept = corn.Close[-1], linetype="dotted", 
                color = "green", size=1.5) +# Geometric object to use for drawing
    annotate('text', color = "green", x=corn.Close[-1]+15, y = 20, label=str(int(len(corn[corn["Close"] > corn.Close[-1]]) / len(corn) * 100))+"%")
)
myPlot.save("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Histograma_Maiz.png", dpi=600)


myPlot = (
    ggplot(aceite.reset_index())  # What data to use
    + aes(x="Close")  # What variable to use
    + geom_histogram()+
    #facet_wrap(facets="Grano", scales="free_y")+
    labs(title="Histograma del precio del aceite de soja primera posición CBOT",
         subtitle="En dólares por tonelada",
         y = "Frecuencia",
         x = "Precio de cierre (usd/tn)",
         fill = "Precio de cierre (usd/tn)")+
    theme_bw() +
    geom_vline(xintercept = aceite.Close[-1], linetype="dotted", 
                color = "blue", size=1.5) +# Geometric object to use for drawing
    annotate('text', color = "blue", x=aceite.Close[-1]+50, y = 15, label=str(int(len(aceite[aceite["Close"] > aceite.Close[-1]]) / len(aceite) * 100))+"%")
)
myPlot.save("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Histograma_Aceite_Soja.png", dpi=600)


myPlot = (
    ggplot(harina.reset_index())  # What data to use
    + aes(x="Close")  # What variable to use
    + geom_histogram()+
    #facet_wrap(facets="Grano", scales="free_y")+
    labs(title="Histograma del precio de la harina de soja primera posición CBOT",
         subtitle="En dólares por tonelada",
         y = "Frecuencia",
         x = "Precio de cierre (usd/tn)",
         fill = "Precio de cierre (usd/tn)")+
    theme_bw() +
    geom_vline(xintercept = harina.Close[-1], linetype="dotted", 
                color = "blue", size=1.5) +# Geometric object to use for drawing
    annotate('text', color = "blue", x=harina.Close[-1]+25, y = 30, label=str(int(len(harina[harina["Close"] > harina.Close[-1]]) / len(harina) * 100))+"%")
)
myPlot.save("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Histograma_Harina_Soja.png", dpi=600)


#endregion



#%%
#region GRÁFICO ÍNDICE BASE 100
fig = px.line(df.reset_index(), x='Date', y="SMA_Base_100_Close", color='Grano',
template='simple_white', title="Índice de precios primera posición CBOT")
fig.update_xaxes(title_text='Fecha',nticks=16)
fig.update_yaxes(title_text='Base 100 = 01/01/1990')
fig.write_html("p:/Estudios_Gerencia/Balances/Precios/CBOT/Grafs/Indice_Base_100.html")

#endregion

# %%
