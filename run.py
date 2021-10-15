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
    Get sales figures input from the user.
    """
    while True:
        print("Please enter sales data from the last market.")
        print("Data should be seven numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60,70\n")

        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid!")
            break

   

def validate_data(values):
    """
    raise error if not an integrer,
    or if there aren't exactly 7 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


data = get_sales_data()