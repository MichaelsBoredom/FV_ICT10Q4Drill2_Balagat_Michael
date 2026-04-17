from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

def numpy(e):
    document.getElementById('output').innerHTML = " "

    calories =  np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
    burned_calories = np.array([500, 100, 600, 300, 200, 400, 700])
    graph = plt.plot(calories, burned_calories)
    plt.show(graph)

    plt.title("Calories Burned by Day")
    plt.xlabel('Days')
    plt.ylabel('Calories Burned')
