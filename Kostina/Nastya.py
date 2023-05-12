import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import math

def main():
    root = tk.Tk()
    root.title("Программа для вывода информации из файла в Excel")
    def DiagramData():
        file = pd.read_excel('число въездных поездок в Россию.xlsx')
        df = pd.DataFrame(file)
        name = df['Страны']
        tourists = df.iloc[:, 2:11]
        # Вычисляем количество диаграмм, округляя до ближайшего большего целого
        num_diagrams = math.ceil(tourists.shape[1] / 3)
        # Создаем общую фигуру
        fig, axs = plt.subplots(nrows=num_diagrams, ncols=3, figsize=(16, 6*num_diagrams))
        axs = axs.flatten()  # Преобразуем массив осей в одномерный массив
        # Создаем графики
        for i in range(tourists.shape[1]):
            ax = axs[i]
            ax.barh(name, tourists.iloc[:, i], align='center', color=f'C{i}')
            ax.grid(True, color='grey', linestyle='-.', linewidth=0.5)
            ax.invert_yaxis()
            for j, value in enumerate(tourists.iloc[:, i]):
                ax.text(value, j, str(value), fontsize=6, va='center')
            ax.tick_params(axis='both', labelsize=6)
            ax.legend([tourists.columns[i]], fontsize=8, loc='upper right')
