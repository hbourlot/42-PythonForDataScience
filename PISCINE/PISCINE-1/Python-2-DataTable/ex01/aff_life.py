from load_csv import load
import matplotlib.pyplot as plt
import numpy as np


def select_points(data: list, n: int) -> list:
    """Select n distributed points from a list

    Args:
            data (list): list of values
            n (int): quantity of n values to select

    Returns:
            list: New list containing the selected values
    """

    indices = np.linspace(0, len(data) - 1, n, dtype=int)
    return [data[i] for i in indices]


def main():
    """Display France's life expectancy over the years.

    Returns:
        int: 0 on success, 1 if the dataset could not be loaded.
    """

    dataFrame = load("life_expectancy_years.csv")

    if dataFrame is None:
        return 1

    dataFrame = dataFrame.set_index("country")

    country = "France"

    france_data = dataFrame.loc[country].tolist()

    x_axis = [int(year) for year in dataFrame.columns.tolist()]
    y_axis = france_data

    plt.plot(x_axis, y_axis)

    x_ticks = [x_axis[0] + i * 40 for i in range(8)]
    plt.xticks(x_ticks)
    plt.yticks([round(value, -1) for value in select_points(y_axis, 7)])

    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.title(f"{country} Life expectancy Projections")

    plt.show()

    return 0


if __name__ == "__main__":
    main()
