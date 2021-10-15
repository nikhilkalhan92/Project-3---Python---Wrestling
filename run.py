import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('wrestlingshirts')

sales = SHEET.worksheet('sales')
stock = SHEET.worksheet('stock')
profit = SHEET.worksheet('profit')

sales_data = sales.get_all_values()
stock_data = stock.get_all_values()
profit_data = profit.get_all_values()

def get_days_sales_data(date: str):
    """method to get sales data for a specific day"""
    headings = []
    data = []
    for i, row in enumerate(sales_data):
        if i == 0: 
            headings = row
        else:
            if row[0] == date:
                data = row
    for i, item in enumerate(headings):
        if i > 0:
            print(item, data[i])



def main():
    """this is the main executiable function"""
    print("some instructions")  #write a series of print function to explain to the user what the application does
   
   
    print("pick a date")
    date = input("")
    #do some form of data validation
    get_days_sales_data(date)

main()
