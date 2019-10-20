#Carreguem les bibiloteques necessaries

import csv
import requests
from bs4 import BeautifulSoup


#Introduim la url d'on volem descarregar el contingut
page = requests.get("https://investmentpolicy.unctad.org/international-investment-agreements/iia-mapping")
soup = BeautifulSoup(page.content)

soup.prettify()

  
 #Creem una llista on anirem guardant les dades que ens baixem   
treaties=[]   
variables=["Title", "Status", "Country 1", "County 2", "Date of signature", "Date of entry into force", "Termination date"]
treaties.append(variables)


#Ens baixem les dades. Com que no ens interessen totes les dades introduim condicions if per seleccionar el que volem
for treaty in soup.table.tbody.find_all("tr"):
    data=[]
    for variable in treaty.find_all("td"):
        if variable.get("data-index")=="2" or variable.get("data-index")=="4": 
            data.append(variable.string)
        if variable.get("data-index")=="5":
            for country in variable.find_all("a"):
                data.append(country.string)
        if variable.get("data-index")=="6" or variable.get("data-index")=="7" or variable.get("data-index")=="8":
            data.append(variable.string)
    treaties.append(data)


#Ho guardem en foram csv
with open("treaties.csv", 'w', newline='') as csvFile:
  writer = csv.writer(csvFile, delimiter=";")
  for treaty in treaties:
    writer.writerow(treaty)