import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def display_line_plot():
    df = pd.read_csv("data/spotify.csv")

    # pick every 5th row in order to improve readability of visualization
    df = df[df.index % 5 == 0]

    plt.plot(df["Date"], df["Shape of You"],)
    plt.plot(df["Date"], df["Despacito"])
    plt.plot(df["Date"], df["Something Just Like This"])
    plt.plot(df["Date"], df["HUMBLE."])
    plt.plot(df["Date"], df["Unforgettable"])
    plt.legend(["Shape of You", "Despacito",
               "Something Just Like This", "HUMBLE.", "Unforgettable"])
    plt.xlabel("Dates")
    plt.ylabel("Global Daily Streams")
    plt.title("Streaming of Songs on Spotify")
    plt.xticks(rotation=90)
    plt.show()


def display_bar_plot_util(x, height, xLabel="", yLabel="", title=""):
    plt.bar(x, height)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.show()


def display_bar_plot():
    df = pd.read_csv("data/API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4687422.csv")
    countries = ["Australia", "Korea", "North America", "Pakistan",
                 "Europe & Central Asia", "Arab World", "United Kingdom", "United States"]
    df = df[df['Country Name'].isin(countries)]
    x = df["Country Name"].values.tolist()
    height = df["2021"].values.tolist()
    xLabel = "Countries"
    yLabel = "GDP"
    title = "GDP of Year 2021"
    display_bar_plot_util(x, height, xLabel, yLabel, title)


def display_scatter_plot():
    df = pd.read_csv("data/insurance.csv")
    print(df.head())
    plt.scatter(df["bmi"], df["charges"])
    plt.xlabel("BMI")
    plt.ylabel("Charges")
    plt.title("Depiction of Positive Corelation of BMI and Insurance Charges")
    plt.show()


def main():
    choice = input(
        "Choose 1 of the following: \n1.Line Plot\n2.Bar Plot\n3.Scatter Plot\nChoice: ")
    if choice == "1":
        display_line_plot()
    elif choice == "2":
        display_bar_plot()
    elif choice == "3":
        display_scatter_plot()
    else:
        print("Invalid Choice!")


if __name__ == "__main__":
    main()

# bar plot data set
# https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG

# line plot data set
# https://www.kaggle.com/code/alexisbcook/line-charts/data?select=spotify.csv

# scatter plot data set
# https://www.kaggle.com/code/alexisbcook/scatter-plots/data?select=insurance.csv
