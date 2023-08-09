#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 06:45:48 2023

@author: cris
"""
import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkTeal9')

layout = [
        [sg.Text('Per favore compile i siguenti righe:')],
        [sg.Text('Taglio max:', size = (15,1)), sg.InputText(key='Taglio max')],
        [sg.Text('Taglio min:', size = (15,1)), sg.InputText(key='Taglio min')],
        [sg.Text('Coagulo max:', size = (15,1)), sg.InputText(key='Coagulo max')],
        [sg.Text('Coagulo min:', size = (15,1)), sg.InputText(key='Coagulo min')],
        [sg.Text('Blend max:', size = (15,1)), sg.InputText(key='Blend max')],
        [sg.Text('Blend min:', size = (15,1)), sg.InputText(key='Blend min')],
        [sg.Text('Seleziona un archivio excel:'),sg.InputText(), sg.FileBrowse()],
        [sg.Submit(), sg.Exit()]
    ]

window = sg.Window('Calcoli CF Elettrobisturi', layout)

def tolerancia(filename):
    try:
        df = pd.read_excel(filename)
        taglio = df["Taglio"]
        taglio_max = int(values["Taglio max"])
        for value,n in enumerate(taglio, start = 1):
            if value > 10 and (value * 0.2) < taglio_max / n:
                print("ok")
            else: 
                print("not ok", round(value * 0.2), taglio / n)
    except Exception as e:
        print('Errore al caricare i dati', e)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Submit':
        filename = values[0]
        tolerancia(filename)
          
window.close()
          


