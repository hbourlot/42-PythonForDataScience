import matplotlib.pyplot as plt
from load_csv import load

def convert_population_value(value: str) -> float:
    """Convert a population value from M to number.

    Args:
        value (str): Population value ending in M.

    Returns:
        float: Population as a number.
    """
    return float(value[:-1]) * 1_000_000


def main():
    """Display population projections for Belgium and France

    Returns:
        int: 0 on success, 1 on error.
    """
    dataFrame = load("population_total.csv")

    if dataFrame is None:
        return 1
    try:
        x_axis = [int(year) for year in dataFrame.columns.tolist()[1:]]
        
        end = x_axis.index(2050) + 1
        x_axis = x_axis[:end]
        
        x_ticks = [x_axis[0] + i * 40 for i in range(7)]

        b_country = dataFrame.loc[dataFrame["country"] == "Belgium"].squeeze()
        b_y_axis = [convert_population_value(value) for value in b_country.tolist()[1:end + 1]]
        plt.plot(x_axis, b_y_axis, label='Belgium', color='blue')

        
        f_country = dataFrame.loc[dataFrame["country"] == "France"].squeeze()
        f_y_axis = [convert_population_value(value) for value in f_country.tolist()[1:end + 1]]
        plt.plot(x_axis, f_y_axis, label="France", color="green")
        

        plt.yticks([20_000_000, 40_000_000, 60_000_000], ["20M", "40M", "60M"])
        plt.xticks(x_ticks)

        plt.legend(loc="lower right")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("Population Projections")
        plt.show()
    except Exception as error:
        print("Error: ", error)
        return 1

    return 0


if __name__ == "__main__":
    main()