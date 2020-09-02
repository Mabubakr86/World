#import package
import pandas as pd
from pprint import pprint as pp
import os
import difflib


#create world class
class World:
    def __init__(self, src):
        self.data = self._get_data(src)

    def _get_data(self, src):
        try:
            data_df = pd.read_excel(src)
            columns = data_df.columns.tolist()[1:] 
            assert len(columns)==4, 'columns in source file do not fit'
            countries, capitals, currencies, langs = [data_df[col].to_list() 
                                                      for col in columns]
            zipped_data = zip(countries,capitals,currencies,langs)
            mapped_data = {item[0].lower():item[1:] for item in zipped_data}
            return mapped_data
        except Exception as e:
            print(e)

    def _check_country(self, country):
        if country not in self.data.keys():
            search_results = difflib.get_close_matches(country.lower(), self.data.keys(),n=2)
            if search_results:
                for result in search_results:
                    res = input(f'Do you mean {result}\n[y/n?]')
                    if res.lower() == 'y':
                        return result
            print('Sorry!! No Matches Were Found')
            return
        return country

    def print_country_data(self,country_data, verbose='all'):
        options = [
                    f"\nThe capital of {country_data['country']} >>>> {country_data['capital']}\n",
                    f"\nThe currency of {country_data['country']} >>>> {country_data['currency']}\n",
                    f"\nThe language of {country_data['country']} >>>> {country_data['language']}\n"
                    ]
        if verbose == 'all':
            print(''.join(options))
        elif verbose == 'capital':
            print(options[0])
        elif verbose == 'currency':
            print(options[1])
        elif verbose == 'language':
            print(options[2])

    def get_country_data(self, country):
        country = self._check_country(country)
        if country:
            country_data = {
                            'country':country,
                            'capital':self.data[country][0],
                            'currency':self.data[country][1],
                            'language':self.data[country][2],
                            }   
            return country_data 



if __name__ == '__main__':
    world = World(src='world.xlsx')
    country_data = world.get_country_data(input('Serach Countries For: '))
    world.print_country_data(country_data, verbose='all')




