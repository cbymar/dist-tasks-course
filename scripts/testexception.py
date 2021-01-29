
class SalaryError(Exception):
    """Custom exception, the likes of which we may need to write"""
    pass


while True:
    try:
        salary = input("Please enter your salary")
        if not salary.isdigit():
            raise SalaryError()
        print(salary)
        break
    except SalaryError:
        print("Invalid salary number, try again")
    finally:
        print("This is where we release any resources that were tied up")
