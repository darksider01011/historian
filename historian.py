import argparse                                                                                                                                                                                                                             
from wayback import WaybackClient                                                                                                                                                                                                           
from datetime import date, timedelta  
from colorama import Fore, Back, Style
                                                                                                                                                                                                                                            
client = WaybackClient()                                                                                                                                                                                                                    
                                                                                                                                                                                                                                            
def From(fromm):                                                                                                                                                                                                                            
    date = str(fromm)                                                                                                                                                                                                                       
    datee = len(date)
    if datee > 8 or datee < 8:
        raise argparse.ArgumentTypeError('invalid from date format.   example: 20150510')
    else:
        return date
def To(to):
    date = str(to)
    datee = len(date)
    if datee > 8 or datee < 8:
        raise argparse.ArgumentTypeError('invalid to date format.  example: 20150510')
    else:
        return date

parser = argparse.ArgumentParser(description='historian.py is python script that use wayback library to check robots.txt history', prog= 'historian.py', epilog= 'Example: python3 historian.py  -d amazon.com -f 20050103 -t 20050203')
parser.add_argument('-d', type=str, help='Set target domain', metavar= 'example.com', default=False, required=True)
parser.add_argument('-f', type=From, help='From date', metavar= '20020501', default=False, required=True)
parser.add_argument('-t', type=To, help='To date', metavar= '20240501', default=False, required=True)

args = parser.parse_args()
domain = args.d
fromm = args.f
to = args.t

frommm = str(fromm)
too = str(to)

def daterange(start_date: date, end_date: date):
    days = int((end_date - start_date).days)
    for n in range(days):
        yield start_date + timedelta(n)

start_date = date.fromisoformat(frommm)
end_date = date.fromisoformat(too)

for single_date in daterange(start_date, end_date):
    results = client.search(domain + "/robots.txt",  from_date=single_date)
    record = next(results)
    print(Fore.BLUE + Style.BRIGHT + str(record.timestamp) +" "+ Fore.WHITE + str(record.view_url))
