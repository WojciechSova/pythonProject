import pandas as pd
import numpy as np

df = pd.read_csv('data.csv', header=None)
# df = pd.read_csv('data.csv', header=['Plec', 'dlugosc', 'srednica', 'wysokosc', 'masa calkowita', 'masa po wyjęciu z '
#                                                                                                   'muszli',
#                                      'masa trzewi', 'masa muszli', 'pierścienie'])

# print(df.to_string())
print(df[[0]])


def create_table_count():
    table_columns = ["count", "%"]
    table_rows = ["Male", "Infant", "Female"]
    letters = ['M', 'I', 'F']
    data = []
    for l in letters:
        data.append([df[[0]].value_counts()[l], 100 * df[[0]].value_counts()[l] / df[[0]].count()])
    table = pd.DataFrame(data, table_rows, table_columns)
    print(table)


def create_table_somtehing():
    print(df[[1]].describe()[1:].values)

    table_columns = ["mean", "std", 'min', '25%', '50%', '75%', 'max']
    table_rows = ["Lengt", "Diameter", "height", "whole weight", "shucked weight", "viscera weight", "shell weight",
                  "rings"]

    data = []
    for i in range(1, len(df.columns)):
        data.append(df[[i]].describe()[1:].values.reshape({1, 8}))
    table = pd.DataFrame(data, table_rows, table_columns)
    print(table)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create_table_count()

    create_table_somtehing()
