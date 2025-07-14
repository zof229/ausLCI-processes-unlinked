# scraper-python.py
# To run this script, paste `python scraper-python.py` in the terminal

import requests
import re
from urllib.request import urlopen, urlretrieve, quote

from bs4 import BeautifulSoup

def scrape(url = 'https://www.auslci.com.au/index.php/Datasets',i=0, output=""):
    ROOT = 'https://www.auslci.com.au'
    # url = 'https://www.example.com'
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    print(soup)

    title = soup.select_one('h1').text
    # text = soup.select_one('p').text
    link = soup.select_one('a').get('href')

    print("TITLE",title)
    # print("TEXT",text)
    print("LINK",link)

    links = soup.find_all('a')
    print("LINKs",links)
    hrefs = [x.get('href') for x in links]
    print("HREFS",hrefs, "\n end hrefs")
    # trying to get rid of nonetypes?
    links = [item for item in links if item.get('href') is not None]
    print("\n\n",links, "\n\n")

    # pattern = ".*php"
    # dataset_hrefs = [ROOT.join(link) for link in hrefs if re.match(pattern, link)]
    # dataset_hrefs = [link for link in hrefs if re.fullmatch(pattern, link)]
    # dataset_hrefs = [ROOT + link for link in dataset_hrefs]
    # print("Links to dataset pages \n",dataset_hrefs)

    # if i<=2:
    #     i+=1
    #     for link in dataset_hrefs:
    #         scrape(url=link,i=i)

    # download_pattern = ".*.xlsx"
    # download_links = [ROOT + link for link in hrefs if re.fullmatch(download_pattern, link)]
    # download_links = [ROOT + link for link in hrefs if link.endswith(".xlsx")]
    # print("downloads \n",download_links)

    link_name_pairs = [(link.get_text(), ROOT+link.get('href').replace(" ", "%20")) for link in links if link.get('href').endswith(".xlsx")]
    print("\n link name pairs\n", link_name_pairs)

    # download time!!
    for link in link_name_pairs:
        # filename = "scraper-output/"+link[0]+".xlsx"
        filename = output+link[0]+".xlsx"
        href = link[1].replace(" ", "%20")
        # urlretrieve(url=href, filename=filename)
        try:
            print('downloading',link, '\n to ', output)
            urlretrieve(url=href, filename=filename)
            print('Complete! yay!')
        except:
            print('failed to download', link)
    
# https://www.auslci.com.au/Datasets/ExcelFiles/almond%20hulls%20and%20shells,%20at%20huller%20and%20sheller%20AU%20U.xlsx


if __name__ == '__main__':
    # url = "https://www.auslci.com.au/Datasets/WasteTreatment/Recycling.php"
    ### Materials
    # url = "https://www.auslci.com.au/Datasets/Material/Agricultural.php"
    # url = "https://www.auslci.com.au/Datasets/Material/Chemicals.php"
    # url = "https://www.auslci.com.au/Datasets/Material/Construction.php"
    # url = "https://www.auslci.com.au/Datasets/Material/Fuels.php"
    # url = "https://www.auslci.com.au/Datasets/Material/Minerals.php"
    # url = "https://www.auslci.com.au/Datasets/Material/Plastics.php"
    # url = "https://www.auslci.com.au/Datasets/Material/Textiles.php"
    # url = "https://www.auslci.com.au/Datasets/Material/Water.php"
    # url = "https://www.auslci.com.au/Datasets/Material/Wood.php"
    # output="scraper-output/materials/agriculture/"
    # output="scraper-output/materials/chemicals/"
    # output="scraper-output/materials/construction/"
    # output="scraper-output/materials/fuels/"
    # output="scraper-output/materials/minerals/"
    # output="scraper-output/materials/plastics/"
    # output="scraper-output/materials/textiles/"
    # output="scraper-output/materials/water/"
    # output="scraper-output/materials/wood/"

    ### Energy
    # url = "https://www.auslci.com.au/Datasets/Energy/ElectricitybyFuel.php"
    # output="scraper-output/energy/ElectricitybyFuel/"
    # url = "https://www.auslci.com.au/Datasets/Energy/Electricitycountrymix.php"
    # output="scraper-output/energy/Electricitycountrymix/"
    # url = "https://www.auslci.com.au/Datasets/Energy/Heat.php"
    # output="scraper-output/energy/heat/"
    # url = "https://www.auslci.com.au/Datasets/Energy/Mechanical.php"
    # output="scraper-output/energy/mechanical/"


    ### transport TODO tomorrow morning come back to this and set up a nice little loop to automate the whole business. For tonight, sleep easy knowing that you've done most of materials and energy
    # url = "https://www.auslci.com.au/Datasets/Transport.php"
    # output="scraper-output/transport/"
    # url = "https://www.auslci.com.au/Datasets/Transport/Air.php"
    # output="scraper-output/transport/air/"
    # url = "https://www.auslci.com.au/Datasets/Transport/Rail.php"
    # output="scraper-output/transport/rail/"
    # url = "https://www.auslci.com.au/Datasets/Transport/Road.php"
    # output="scraper-output/transport/road/"
    # url = "https://www.auslci.com.au/Datasets/Transport/Water.php"
    # output="scraper-output/transport/water/"

    ### processing
    # url = "https://www.auslci.com.au/Datasets/Processing/Agricultural.php"
    # output="scraper-output/processing/agricultural/"
    # url = "https://www.auslci.com.au/Datasets/Processing/Reprocessingmaterials.php"
    # output="scraper-output/processing/reprocessing/"

    ### TODO tomorrow, we do waste treatment
    # url = "https://www.auslci.com.au/Datasets/WasteTreatment/Incineration.php"
    # output="scraper-output/waste/incineration/"
    url = "https://www.auslci.com.au/Datasets/WasteTreatment/Landfill.php"
    output="scraper-output/waste/landfill/"
    url = "https://www.auslci.com.au/Datasets/WasteTreatment/WastewaterTreatment.php"
    output="scraper-output/waste/wastewater/"




    
    scrape(url=url,i=0,output=output)