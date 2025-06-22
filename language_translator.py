# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 19:56:10 2025

@author: Madhumitha
"""

from deep_translator import GoogleTranslator
import tkinter as t
from tkinter.ttk import Combobox  
from tkinter import messagebox

def clear_text():
    txt.delete(0, 'end')
    result_label.config(text="")

def translate_text():
    input_text = txt.get()
    selected_language = combo.get()

    language_codes = {
        "English": "en",
        "Tamil": "ta",
        "Telugu": "te",
        "Hindi": "hi",
        "Malayalam": "ml",
        "Kannada": "kn",
        "Bengali": "bn",
        "Japanese": "ja",
        "Arabic": "ar",
        "Spanish": "es",
        "French": "fr"
    }

    lang_code = language_codes.get(selected_language)

    if lang_code:
        try:
            translated = GoogleTranslator(source='auto', target=lang_code).translate(input_text)
            result_label.config(text=translated)
        except Exception as e:
            messagebox.showerror("Translation Error", str(e))
    else:
        messagebox.showerror("Error", "Please select a valid language.")

window = t.Tk()
window.title("Language Translator")
window.geometry("500x300")

l = t.Label(window, text="Enter Text:", font=("Calibri", 18, "bold"))
l.grid(column=0, row=0, padx=10, pady=10)

txt = t.Entry(window, width=25, font=("Calibri", 18))
txt.grid(column=1, row=0, padx=10, pady=10)

combo = Combobox(window, font=("Calibri", 15))
combo['values'] = ("Select Language", "English", "Tamil", "Telugu", "Hindi", "Malayalam", "Kannada", "Bengali", "Japanese", "Arabic", "Spanish", "French")
combo.current(0)
combo.grid(column=1, row=1, padx=10, pady=10)

btn1 = t.Button(window, text="Translate", font=("Calibri", 15, "bold"),
               bg="#1e90ff", fg="#fdfff5", activebackground="#1084f9",
               activeforeground="#fdfff5", command=translate_text)
btn1.grid(column=1, row=2, padx=10, pady=10)

btn2 = t.Button(window, text="Clear Text", font=("Calibri", 15, "bold"),
               bg="#ff1e1e", fg="#fdfff5", activebackground="#ff261e",
               activeforeground="#fdfff5", command=clear_text)
btn2.grid(column=0, row=2, padx=10, pady=10)

result_label = t.Label(window, text="", font=("Calibri", 16), wraplength=400, justify="left")
result_label.grid(column=0, row=3, columnspan=3, padx=10, pady=10)

window.mainloop()
