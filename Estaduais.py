import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
#from PIL import image
import numpy as np
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode
import plotly.express as px
import io
import matplotlib.pyplot as plt
from soccerplots.radar_chart import Radar
from sklearn.decomposition import PCA
from PIL import Image

#CABEÇALHO DO FORM
st.markdown("<h1 style='text-align: center;'>Melhores dos Estaduais</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>app by @JAmerico1898</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>MG, RJ, RS, SP com +500 minutos em campo.<br>Dados do Wyscout em 5Abr2024.</h6>", unsafe_allow_html=True)
st.markdown("---")

#df5 = pd.read_csv("ligas.csv")
df6 = pd.read_csv("Posições.csv")

ligas = ("MG", "RJ", "RS", "SP")
posições = df6["Posição"]
temporada = 2024
liga = st.selectbox("Escolha a Liga", options=ligas, index=None)
posição = st.selectbox("Escolha a posição", options=posições, index=None)

if liga and temporada:
    if posição == "Goleiro":
        st.markdown("<h4 style='text-align: center;'>10 Goleiros Clássicos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_3 = pd.read_csv("1_Role_Goleiro.csv")
        tabela_3 = tabela_3[(tabela_3['Liga']==liga)&(tabela_3['Versão_Temporada']==temporada)]
        tabela_3 = tabela_3.iloc[:, np.r_[1, 30, 3, 4, 7, 8:12, 15, 18:27]]
        tabela_3 = tabela_3.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Posição_Wyscout':'Posição', 'Versão_Temporada':'Janela de Análise', 'Interceptações.1':'Interceptações'})
        tabela_3 = tabela_3.sort_values(by='Rating', ascending=False)
        tabela_3 = tabela_3.head(10)
        st.dataframe(tabela_3, use_container_width=True, hide_index=False)

        st.markdown("<h4 style='text-align: center;'>10 Goleiros Líberos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_4 = pd.read_csv("2_Role_Goleiro_Líbero.csv")
        tabela_4 = tabela_4[(tabela_4['Liga']==liga)&(tabela_4['Versão_Temporada']==temporada)]
        tabela_4 = tabela_4.iloc[:, np.r_[1, 33, 3, 4, 7, 8:12, 15, 18:28]]
        tabela_4 = tabela_4.rename(columns={'Equipe_Janela_Análise':'Equipe', 'Posição_Wyscout':'Posição', 'Versão_Temporada':'Janela de Análise', 'Interceptações.1':'Interceptações'})
        tabela_4 = tabela_4.sort_values(by='Rating', ascending=False)
        tabela_4 = tabela_4.head(10)
        st.dataframe(tabela_4, use_container_width=True, hide_index=True)

    elif posição == "Lateral":
        st.markdown("<h4 style='text-align: center;'>10 Laterais Defensivos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_3 = pd.read_csv("3_Role_Lateral_Defensivo.csv")
        tabela_3 = tabela_3[(tabela_3['Liga']==liga)&(tabela_3['Versão_Temporada']==temporada)]
        tabela_3 = tabela_3.iloc[:, np.r_[1, 29, 3, 4, 7, 8:12, 15, 18:23]]
        tabela_3 = tabela_3.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_3 = tabela_3.sort_values(by='Rating', ascending=False)
        tabela_3 = tabela_3.head(10)
        st.dataframe(tabela_3, use_container_width=True, hide_index=True)

        st.markdown("<h4 style='text-align: center;'>10 Laterais Ofensivos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_4 = pd.read_csv("4_Role_Lateral_Ofensivo.csv")
        tabela_4 = tabela_4[(tabela_4['Liga']==liga)&(tabela_4['Versão_Temporada']==temporada)]
        tabela_4 = tabela_4.iloc[:, np.r_[1, 38, 3, 4, 7, 8:12, 15, 18:33]]
        tabela_4 = tabela_4.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_4 = tabela_4.sort_values(by='Rating', ascending=False)
        tabela_4 = tabela_4.head(10)
        st.dataframe(tabela_4, use_container_width=True, hide_index=True)

        st.markdown("<h4 style='text-align: center;'>10 Laterais Equilibrados Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_5 = pd.read_csv("5_Role_Lateral_Equilibrado.csv")
        tabela_5 = tabela_5[(tabela_5['Liga']==liga)&(tabela_5['Versão_Temporada']==temporada)]
        tabela_5 = tabela_5.iloc[:, np.r_[1, 41, 3, 4, 7, 8:12, 15, 18:35]]
        tabela_5 = tabela_5.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_5 = tabela_5.sort_values(by='Rating', ascending=False)
        tabela_5 = tabela_5.head(10)
        st.dataframe(tabela_5, use_container_width=True, hide_index=True)

    elif posição == "Zagueiro":
        st.markdown("<h4 style='text-align: center;'>10 Zagueiros Clássicos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_6 = pd.read_csv("6_Role_Zagueiro_Defensivo.csv")
        tabela_6 = tabela_6[(tabela_6['Liga']==liga)&(tabela_6['Versão_Temporada']==temporada)]
        tabela_6 = tabela_6.iloc[:, np.r_[1, 29, 3, 4, 7, 8:12, 15, 18:23]]
        tabela_6 = tabela_6.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_6 = tabela_6.sort_values(by='Rating', ascending=False)
        tabela_6 = tabela_6.head(10)
        st.dataframe(tabela_6, use_container_width=True, hide_index=True)

        st.markdown("<h4 style='text-align: center;'>10 Zagueiros Construtores Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_7 = pd.read_csv("7_Role_Zagueiro_Construtor.csv")
        tabela_7 = tabela_7[(tabela_7['Liga']==liga)&(tabela_7['Versão_Temporada']==temporada)]
        tabela_7 = tabela_7.iloc[:, np.r_[1, 33, 3, 4, 7, 8:12, 15, 18:28]]
        tabela_7 = tabela_7.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_7 = tabela_7.sort_values(by='Rating', ascending=False)
        tabela_7 = tabela_7.head(10)
        st.dataframe(tabela_7, use_container_width=True, hide_index=True)

        st.markdown("<h4 style='text-align: center;'>10 Zagueiros Equilibrados Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_8 = pd.read_csv("8_Role_Zagueiro_Equilibrado.csv")
        tabela_8 = tabela_8[(tabela_8['Liga']==liga)&(tabela_8['Versão_Temporada']==temporada)]
        tabela_8 = tabela_8.iloc[:, np.r_[1, 36, 3, 4, 7, 8:12, 15, 18:32]]
        tabela_8 = tabela_8.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_8 = tabela_8.sort_values(by='Rating', ascending=False)
        tabela_8 = tabela_8.head(10)
        st.dataframe(tabela_8, use_container_width=True, hide_index=True)

    elif posição == "Primeiro Volante":
        st.markdown("<h4 style='text-align: center;'>10 Primeiros Volantes Defensivos Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_12 = pd.read_csv("9_Role_Volante_Defensivo.csv")
        tabela_12 = tabela_12[(tabela_12['Liga']==liga)&(tabela_12['Versão_Temporada']==temporada)]
        tabela_12 = tabela_12.iloc[:, np.r_[1, 27, 3, 4, 7, 8:12, 15, 18:22]]
        tabela_12 = tabela_12.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_12 = tabela_12.sort_values(by='Rating', ascending=False)
        tabela_12 = tabela_12.head(10)
        st.dataframe(tabela_12, use_container_width=True, hide_index=True)

        st.markdown("<h4 style='text-align: center;'>10 Primeiros Volantes Construtores Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_13 = pd.read_csv("10_Role_Volante_Construtor.csv")
        tabela_13 = tabela_13[(tabela_13['Liga']==liga)&(tabela_13['Versão_Temporada']==temporada)]
        tabela_13 = tabela_13.iloc[:, np.r_[1, 32, 3, 4, 7, 8:12, 15, 18:27]]
        tabela_13 = tabela_13.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_13 = tabela_13.sort_values(by='Rating', ascending=False)
        tabela_13 = tabela_13.head(10)
        st.dataframe(tabela_13, use_container_width=True, hide_index=True)

        st.markdown("<h4 style='text-align: center;'>10 Primeiros Volantes Equilibrados Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_14 = pd.read_csv("11_Role_Volante_Equilibrado.csv")
        tabela_14 = tabela_14[(tabela_14['Liga']==liga)&(tabela_14['Versão_Temporada']==temporada)]
        tabela_14 = tabela_14.iloc[:, np.r_[1, 34, 3, 4, 7, 8:12, 15, 18:29]]
        tabela_14 = tabela_14.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_14 = tabela_14.sort_values(by='Rating', ascending=False)
        tabela_14 = tabela_14.head(10)
        st.dataframe(tabela_14, use_container_width=True, hide_index=True)

    elif posição == "Segundo Volante":
        st.markdown("<h4 style='text-align: center;'>10 Segundos Volantes Box-to-Box Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_12 = pd.read_csv("12_Role_Segundo_Volante_Box_to_Box.csv")
        tabela_12 = tabela_12[(tabela_12['Liga']==liga)&(tabela_12['Versão_Temporada']==temporada)]
        tabela_12 = tabela_12.iloc[:, np.r_[1, 36, 3, 4, 7, 8:12, 15, 18:31]]
        tabela_12 = tabela_12.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_12 = tabela_12.sort_values(by='Rating', ascending=False)
        tabela_12 = tabela_12.head(10)
        st.dataframe(tabela_12, use_container_width=True, hide_index=True)

        st.markdown("<h4 style='text-align: center;'>10 Segundos Volantes Organizadores Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_13 = pd.read_csv("13_Role_Segundo_Volante_Organizador.csv")
        tabela_13 = tabela_13[(tabela_13['Liga']==liga)&(tabela_13['Versão_Temporada']==temporada)]
        tabela_13 = tabela_13.iloc[:, np.r_[1, 33, 3, 4, 7, 8:12, 15, 18:28]]
        tabela_13 = tabela_13.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_13 = tabela_13.sort_values(by='Rating', ascending=False)
        tabela_13 = tabela_13.head(10)
        st.dataframe(tabela_13, use_container_width=True, hide_index=True)

        st.markdown("<h4 style='text-align: center;'>10 Segundos Volantes Equilibrados Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_14 = pd.read_csv("14_Role_Segundo_Volante_Equilibrado.csv")
        tabela_14 = tabela_14[(tabela_14['Liga']==liga)&(tabela_14['Versão_Temporada']==temporada)]
        tabela_14 = tabela_14.iloc[:, np.r_[1, 36, 3, 4, 7, 8:12, 15, 18:31]]
        tabela_14 = tabela_14.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_14 = tabela_14.sort_values(by='Rating', ascending=False)
        tabela_14 = tabela_14.head(10)
        st.dataframe(tabela_14, use_container_width=True, hide_index=True)

    elif posição == "Meia":
        st.markdown("<h4 style='text-align: center;'>10 Meias Organizadores Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_15 = pd.read_csv("15_Role_Meia_Organizador.csv")
        tabela_15 = tabela_15[(tabela_15['Liga']==liga)&(tabela_15['Versão_Temporada']==temporada)]
        tabela_15 = tabela_15.iloc[:, np.r_[1, 33, 3, 4, 7, 8:12, 15, 18:28]]
        tabela_15 = tabela_15.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_15 = tabela_15.sort_values(by='Rating', ascending=False)
        tabela_15 = tabela_15.head(10)
        st.dataframe(tabela_15, use_container_width=True, hide_index=True)

        st.markdown("<h4 style='text-align: center;'>10 Meias Atacantes Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_16 = pd.read_csv("16_Role_Meia_Atacante.csv")
        tabela_16 = tabela_16[(tabela_16['Liga']==liga)&(tabela_16['Versão_Temporada']==temporada)]
        tabela_16 = tabela_16.iloc[:, np.r_[1, 40, 3, 4, 7, 8:12, 15, 18:35]]
        tabela_16 = tabela_16.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_16 = tabela_16.sort_values(by='Rating', ascending=False)
        tabela_16 = tabela_16.head(10)
        st.dataframe(tabela_16, use_container_width=True, hide_index=True)

    elif posição == "Extremo":
        st.markdown("<h4 style='text-align: center;'>10 Extremos Organizadores Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_17 = pd.read_csv("17_Role_Extremo_Organizador.csv")
        tabela_17 = tabela_17[(tabela_17['Liga']==liga)&(tabela_17['Versão_Temporada']==temporada)]
        tabela_17 = tabela_17.iloc[:, np.r_[1, 36, 3, 4, 7, 8:12, 15, 18:31]]
        tabela_17 = tabela_17.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_17 = tabela_17.sort_values(by='Rating', ascending=False)
        tabela_17 = tabela_17.head(10)
        st.dataframe(tabela_17, use_container_width=True, hide_index=True)
            
        st.markdown("<h4 style='text-align: center;'>10 Extremos Táticos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_18 = pd.read_csv("18_Role_Extremo_Tático.csv")
        tabela_18 = tabela_18[(tabela_18['Liga']==liga)&(tabela_18['Versão_Temporada']==temporada)]
        tabela_18 = tabela_18.iloc[:, np.r_[1, 30, 3, 4, 7, 8:12, 15, 18:25]]
        tabela_18 = tabela_18.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_18 = tabela_18.sort_values(by='Rating', ascending=False)
        tabela_18 = tabela_18.head(10)
        st.dataframe(tabela_18, use_container_width=True, hide_index=True)

        st.markdown("<h4 style='text-align: center;'>10 Extremos Agudos Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_19 = pd.read_csv("19_Role_Extremo_Agudo.csv")
        tabela_19 = tabela_19[(tabela_19['Liga']==liga)&(tabela_19['Versão_Temporada']==temporada)]
        tabela_19 = tabela_19.iloc[:, np.r_[1, 36, 3, 4, 7, 8:12, 15, 18:31]]
        tabela_19 = tabela_19.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_19 = tabela_19.sort_values(by='Rating', ascending=False)
        tabela_19 = tabela_19.head(10)
        st.dataframe(tabela_19, use_container_width=True, hide_index=True)

    elif posição == "Atacante":
        st.markdown("<h4 style='text-align: center;'>10 Atacantes Referências Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_17 = pd.read_csv("20_Role_Atacante_Referência.csv")
        tabela_17 = tabela_17[(tabela_17['Liga']==liga)&(tabela_17['Versão_Temporada']==temporada)]
        tabela_17 = tabela_17.iloc[:, np.r_[1, 33, 3, 4, 7, 8:12, 15, 18:27]]
        tabela_17 = tabela_17.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_17 = tabela_17.sort_values(by='Rating', ascending=False)
        tabela_17 = tabela_17.head(10)
        st.dataframe(tabela_17, use_container_width=True, hide_index=True)
            
        st.markdown("<h4 style='text-align: center;'>10 Atacantes Móveis Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_18 = pd.read_csv("21_Role_Atacante_Móvel.csv")
        tabela_18 = tabela_18[(tabela_18['Liga']==liga)&(tabela_18['Versão_Temporada']==temporada)]
        tabela_18 = tabela_18.iloc[:, np.r_[1, 32, 3, 4, 7, 8:12, 15, 18:27]]
        tabela_18 = tabela_18.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_18 = tabela_18.sort_values(by='Rating', ascending=False)
        tabela_18 = tabela_18.head(10)
        st.dataframe(tabela_18, use_container_width=True, hide_index=True)

        st.markdown("<h4 style='text-align: center;'>10 Segundos Atacantes Mais Bem Ranqueados</b></h4>", unsafe_allow_html=True)
        tabela_19 = pd.read_csv("22_Role_Segundo_Atacante.csv")
        tabela_19 = tabela_19[(tabela_19['Liga']==liga)&(tabela_19['Versão_Temporada']==temporada)]
        tabela_19 = tabela_19.iloc[:, np.r_[1, 36, 3, 4, 7, 8:12, 15, 18:31]]
        tabela_19 = tabela_19.rename(columns={'Equipe_Janela_Análise':'Equipe'})
        tabela_19 = tabela_19.sort_values(by='Rating', ascending=False)
        tabela_19 = tabela_19.head(10)
        st.dataframe(tabela_19, use_container_width=True, hide_index=True)
