"""
Test goes here

"""

from main import csvfile


def test_csvfile():
    main_data = "titanic_main_data.csv"
    result = csvfile(main_data)
    
    # mean value of the 1st column resting blood pressure
    mean_1_column = test_csvfile.iloc[:, 1]["mean"]
    # print(mean_4_column)
    assert mean_1_column == 446
    # standard deviation value of fourth column resting blood pressure
    std_4_column = summary_result.iloc[:, 1]["min"]
    # print(std_4_column)
    assert std_1_column == 1


if __name__ == "__main__":
    test_csvfile()
