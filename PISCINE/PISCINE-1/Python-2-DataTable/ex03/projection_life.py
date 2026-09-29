from load_csv import load
import matplotlib.pyplot as plt


def main() -> int:
    """
        Loads GDP per capita and life expectancy data, then displays
        a scatter plot comparing both values for the year 1900.

    Returns:
        int 0 on success, 1 if the data could not be loaded.

    """
    data_frame_gdb_per_capita = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    data_frame_life_expectancy = load("life_expectancy_years.csv")

    if data_frame_gdb_per_capita is None or data_frame_life_expectancy is None:
        return 1

    try:
        gross_domestic_product = data_frame_gdb_per_capita.loc[:, "1900"]
        life_expectancy = data_frame_life_expectancy.loc[:, "1900"]

        y_axis = life_expectancy
        x_axis = gross_domestic_product

        plt.xscale("log")
        ticks = [300, 1000, 10000]
        plt.xticks(ticks, ["300", "1k", "10k"])
        plt.xlim(left=300)
        plt.scatter(x_axis, y_axis)
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.show()

    except Exception as error:
        print("Error: ", error)

    return 0


if __name__ == "__main__":
    main()
