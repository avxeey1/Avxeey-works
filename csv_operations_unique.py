print('let\'s start new project test')

import math
def parse_header(header):
    return header.strip().split(',')

def parse_values(values):
    result = []
    for value in values.strip().split(','):
        if value == '':
            result.append(0.0)
        else:
            result.append(float(value))
    return result

def dict_values(header, values):
    result = {}
    for head, value in zip(header, values):
        result[head] = value
    return result
    
def read_csv(path):
    result = []
    with open(path, 'r') as f:
        lines = f.readlines()
        header = parse_header(lines[0])
        for value in lines[1:]:
            lists_values = parse_values(value)
            dict_items = dict_values(header, lists_values)
            result.append(dict_items)  
    return result

csv = read_csv('loan1.csv')
print(csv)

def loan_emi(amount, duration, rate, down_payment=0):
    loan_amount = amount - down_payment
    try:
        emi = loan_amount * rate * ((1 + rate)**duration) / (((1 + rate)**duration)-1)
    except ZeroDivisionError:
        emi = loan_amount / duration
    emi = math.ceil(emi)
    return emi
    

def compute_emi(loan1):
    for loan in loan1:
        loan['Emi\'s'] = loan_emi(amount=loan['Loan'], duration=loan[' Duration'], down_payment=loan['Down_payment'], rate=loan['Rate'] / 12)
    return loan1

file=compute_emi(csv)

def write_csv(items, path):
    with open(path, 'w') as f:
        if len(items) == 0:
            return 
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')
        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, '')))
            f.write(','.join(values) + '\n')
        
        

write_csv(file, 'loan_emi\'s3.csv')

with open('loan_emi\'s3.csv', 'r') as f:
    print(f.read())