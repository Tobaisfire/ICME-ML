import requests
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor
import math
import os
class Scrapper1:

    """
    Class for Scrapping H1 Dataset Using year details.

    """

    def get_list( year):
        """
        To get number of CDF/Dataset available in a given year.
        
        """
       
        url = f'https://cdaweb.gsfc.nasa.gov/pub/data/wind/swe/swe_h1/{year}'
        dataset_response = requests.get(url)
        name_list = [i.text for i in bs(dataset_response.content, 'html.parser').find_all('td') if i.text[-3:] == 'cdf']
        print(f"Year {year} has {len(name_list)} dataset")

        return name_list

  
    def download_file(name, year,path, MAX_RETRIES=3):

      
        retries = 0
        while retries < MAX_RETRIES:
            try:
            
                response = requests.get(f'https://cdaweb.gsfc.nasa.gov/pub/data/wind/swe/swe_h1/{year}/{name}')
                if response.status_code == 200:
                    if not os.path.exists(f'{path}/{year}'):
                        os.makedirs(f'{path}/{year}')
                    with open(f'{path}/{year}/{name}', 'wb') as fp:
                        fp.write(response.content)
                    print(f"Downloaded: {name}\n")
                    break
                if response.status_code == 404:
                    print('No Data!')
                    break

                else:
                    print(f"Error downloading {name}: Got status code {response.status_code}")
            except Exception as e:
                print(f"Error downloading {name}: {e}")
            retries += 1
            print(f"Retrying ({retries}/{MAX_RETRIES})...")



    def download_files_with_threadpool(list_of_dates_in_yr, year ,path,max_workers=10):
        chunk_size = math.ceil(len(list_of_dates_in_yr) / max_workers)
        chunks = [list_of_dates_in_yr[i:i+chunk_size] for i in range(0, len(list_of_dates_in_yr), chunk_size)]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            for chunk in chunks:
                executor.map(lambda name: Scrapper1.download_file(name, year,path), chunk)



    def run(year, list_of_dates_in_yr,path):

        """
        year -> year of SWE H1 Dataset you want to scrape. \
        path -> where you want to save cdf. \
        list_of_dates_in_yr -> list of all filenames in that year. \

        """

        Scrapper1.download_files_with_threadpool(list_of_dates_in_yr, year,path)
