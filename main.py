from classes.cairocamerarentals import CCR_cam


def main():

    df = CCR_cam.get_dataframe()

    print(df)


main()