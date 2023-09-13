"""
Test goes here

"""

from main import csvfile


def test_csvfile():
    main_data = "titanic_main_data.csv"
    result = csvfile(main_data)
    
    # mean value of the 1st column resting blood pressure
    mean_1_column = test_csvfile.iloc[:, 3]["mean"]
    # print(mean_4_column)
    assert mean_1_column == 
    # standard deviation value of fourth column resting blood pressure
    std_4_column = summary_result.iloc[:, 3]["std"]
    # print(std_4_column)
    assert std_4_column == 17.5381428135171


if __name__ == "__main__":
    test_csvfile()
