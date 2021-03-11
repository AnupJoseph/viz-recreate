# Internals
from typing import List

# scraping
from gazpacho import get,Soup

def url_string_builder(years: List[str]) -> List[str]:
    base_url:str =f"http://keralaassembly.org/"
    return [f"{base_url}winner{year}.html" for year in years]

years = ["82","87","91","96","01","06","11","16"]