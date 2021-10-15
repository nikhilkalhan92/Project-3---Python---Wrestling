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
    print("Please enter the figures of sold t-shirt items.")
    print("Data could be up to 7 numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60,70,\n")
  
    data_str = input("Enter your data here: ")
    
    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """ raise value error if numbers entered are more then 7 and its not in a list format """

    try: 
        if len(values) != 7:
            raise ValueError(
                f"please enter the 7 numbers required, you only provided {len(values)}"
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

    print(values)

 

get_sales_data()
