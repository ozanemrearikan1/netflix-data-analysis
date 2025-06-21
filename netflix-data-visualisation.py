#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 19:04:28 2025

@author: ozanemrearikan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


df = pd.read_csv("/Users/ozanemrearikan/Downloads/netflix/netflix_titles.csv")
df.head()

print(df.isnull().sum()) # Eksik veriler
print((df.isnull().sum() / len(df)) * 100)
df_clean = df.dropna(subset=["country", "rating", "date_added"])
df_clean.info() # Temizlenmiş tablo

all_genres = df_clean['listed_in'].str.split(',').explode().str.strip()
top_genres = all_genres.value_counts().head(10) # En popüler genres ayıklandı


plt.figure(figsize=(10,6))
sns.barplot(x=top_genres.values, y=top_genres.index, palette="viridis")
plt.title("En Popüler Netflix Türleri")
plt.xlabel("İçerik Sayısı")
plt.ylabel("Tür")
plt.show() # Popüler genres show işlemi


df_clean['release_year'] = df_clean['release_year'].astype(int)
year_counts = df_clean['release_year'].value_counts().sort_index()
plt.figure(figsize=(14,6))
sns.lineplot(x=year_counts.index, y=year_counts.values, marker="o")
plt.title("Yıllara Göre Yayınlanan İçerik Sayısı")
plt.xlabel("Yıl")
plt.ylabel("İçerik Sayısı")
plt.grid(True)
plt.show() # Yıllara göre içerik sayısı

# Ülkelere göre içerik dağılımına bakmak istersek:
country_counts = df_clean['country'].str.split(',').explode().str.strip().value_counts().head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=country_counts.values, y=country_counts.index, palette="rocket")
plt.title("Ülkelere Göre İçerik Dağılımı (İlk 10)")
plt.xlabel("İçerik Sayısı")
plt.ylabel("Ülke")
plt.show()