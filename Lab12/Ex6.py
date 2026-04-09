import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"

# Get the page
response = requests.get(url)
html = response.text

# Parse with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find the table
table = soup.find("table")

# Loop through rows
rows = table.find_all("tr")

for row in rows[1:]:  # skip header row
    cols = row.find_all("td")
    
    if len(cols) > 0:
        bank = cols[0].get_text(strip=True)
        rates = [col.get_text(strip=True) for col in cols[1:]]
        
        print("Bank:", bank)
        print("Rates:", rates)
        print("-------------------")