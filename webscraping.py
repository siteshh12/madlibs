import openpyxl
from bs4 import BeautifulSoup

# Load the HTML file
with open('website.html', 'r',encoding="utf8") as f:
    content = f.read()

# Parse the HTML with Beautiful Soup
soup = BeautifulSoup(content, 'html.parser')

# Find all the product containers
products = soup.find_all('div', {'class': "s-card-container s-overflow-hidden aok-relative puis-wide-grid-style puis-wide-grid-style-t3 puis-include-content-margin puis s-latency-cf-section s-card-border"})

# create a new workbook
wb = openpyxl.Workbook()

#Get the active worksheet
ws = wb.active

#write the header row
ws.append(['Name','Price','Review'])

#Loop through each product and extract the data
for product in products:
    try:
       name = product.find('span',{'class': 'a-size-medium a-color-base a-text-normal'})
    except:
        name = ""
    try:
        price = product.find('span',{'class':'a-price-whole'}).get_text().strip()
    except:
        price=" "
    try:
        reviews = product.find('span',{'class': 'a-size-base'}).get_text().strip()
    except:
        reviews = " "
    #write the data into the worksheet
    ws.append([name,price, reviews])

# Save the workbook
wb.save('website_data.xlsx')






