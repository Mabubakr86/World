import pandas as pd
import requests


url = 'https://www.worldclasslearning.com/general-knowledge/list-countries-capital-currencies-languages.html' 
def get_data(url):
    try:
        tables = pd.read_html(url, header=0)
        world_df = tables[0].to_excel('world.xlsx')
        print('Data was downloaded')
    except Exception as e:
        print(e)

def main():
    get_data(url)

if __name__ == '__main__':
    main()


