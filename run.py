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

def get_sales_data():
    """
    Get wrestling t shirt  input from the user.
    """
    print("Please enter the figures of sold items.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")
  
    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

 

get_sales_data()
