cities = {}

mumbai = {
    'country': 'India',
    'population': 20000000,
    'fact': 'Financial capital of India',
}

delhi = {
    'country': 'India',
    'population': 30000000,
    'fact': 'Capital of India',
}

bangalore = {
    'country': 'India',
    'population': 10000000,
    'fact': 'Silicon Valley of India',
}

cities['mumbai'] = mumbai
cities['delhi'] = delhi
cities['bangalore'] = bangalore

for city, info in cities.items():
    print(f"\n{city.title()}:")
    print(f"\tCountry: {info['country']}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact']}")