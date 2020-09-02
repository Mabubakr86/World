import argparse
from world import World


def main():
    parser = argparse.ArgumentParser('Explore The world with us')
    parser.add_argument('country', help='The country to get data for ')
    parser.add_argument('-o','--options', help='show specific info'
                        '[cap for capital,ur for currency,ang for language]'
                        )
    args = parser.parse_args()

    world = World()
    country_data = world.get_country_data(args.country)
    if args.options == 'cap':
        world.print_country_data(country_data, verbose='capital')
    elif args.options == 'cur':
        world.print_country_data(country_data, verbose='currency')
    elif args.options == 'lang':
        world.print_country_data(country_data, verbose='language') 
    else:     
        world.print_country_data(country_data, verbose='all')


if __name__ == '__main__':
    main()
