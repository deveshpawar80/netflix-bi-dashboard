import pandas as pd
import matplotlib.pyplot as plt
import os
# -----------------------------
# Create folders
# -----------------------------
os.makedirs("charts", exist_ok=True)
os.makedirs("report", exist_ok=True)
# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("data/netflix_titles.csv")
# -----------------------------
# Basic Cleaning
# -----------------------------
df = df.dropna(subset=["type", "country", "release_year"])
# -----------------------------
# Dashboard Summary
# -----------------------------
print("=" * 60)
print("NETFLIX ANALYTICS DASHBOARD")
print("=" * 60)
print("\nTotal Titles:")
print(len(df))
print("\nMovies vs TV Shows:")
print(df["type"].value_counts())
print("\nTop 10 Countries:")
print(df["country"].str.split(",").explode().str.strip().value_counts().head(10))
print("\nRatings:")
print(df["rating"].value_counts())
print("\nTop Genres:")
print(df["listed_in"].str.split(",").explode().str.strip().value_counts().head(10))
# -----------------------------
# Movies vs TV Shows
# -----------------------------
plt.figure(figsize=(6,4))
df["type"].value_counts().plot(kind="bar")
plt.title("Movies vs TV Shows")
plt.tight_layout()
plt.savefig("charts/type_distribution.png")
plt.close()
# -----------------------------
# Release Year Trend
# -----------------------------
plt.figure(figsize=(10,5))
df["release_year"].value_counts().sort_index().plot()
plt.title("Titles Released by Year")
plt.xlabel("Year")
plt.ylabel("Titles")
plt.tight_layout()
plt.savefig("charts/release_year.png")
plt.close()
# -----------------------------
# Ratings
# -----------------------------
plt.figure(figsize=(8,4))
df["rating"].value_counts().plot(kind="bar")
plt.title("Content Ratings")
plt.tight_layout()
plt.savefig("charts/ratings.png")
plt.close()
# -----------------------------
# Top Countries
# -----------------------------
countries = (
    df["country"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
    .head(10))
plt.figure(figsize=(10,5))
countries.plot(kind="bar")
plt.title("Top 10 Countries")
plt.tight_layout()
plt.savefig("charts/top_countries.png")
plt.close()
# -----------------------------
# Top Genres
# -----------------------------
genres = (
    df["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
    .value_counts()
    .head(10))
plt.figure(figsize=(10,5))
genres.plot(kind="bar")
plt.title("Top 10 Genres")
plt.tight_layout()
plt.savefig("charts/top_genres.png")
plt.close()
print("\nDashboard completed successfully!")