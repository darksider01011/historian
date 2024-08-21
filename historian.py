import argparse
import requests
from wayback import WaybackClient
from datetime import date, timedelta
from colorama import Fore, Style

# wayback socket
client = WaybackClient()

# add parser object
parser = argparse.ArgumentParser(description='historian.py is python script that use wayback library to check robots.txt and sitemap.xml history', prog='historian.py', epilog='Example: python3 historian.py sitemap -d example.com -f 20050103 -t 20050203')

# add subparser object
subparser = parser.add_subparsers(dest='command')

def fromm(from_date):
    date = str(from_date)
    datee = len(date)
    if datee > 8 or datee < 8:
        raise argparse.ArgumentTypeError('invalid from date format.   example: 20150510')
    else:
        return date
def to(to_date):
    date = str(to_date)
    datee = len(date)
    if datee > 8 or datee < 8:
        raise argparse.ArgumentTypeError('invalid to date format.  example: 20150510')
    else:
        return date

# add robots subparser
robots = subparser.add_parser("robots", help='robots subcommand')
robots.add_argument('-d', type=str, help='Set target domain', metavar='example.com', default=False, required=True)
robots.add_argument('-f', type=fromm, help='From date', metavar='20020501', default=False, required=True)
robots.add_argument('-t', type=to, help='To date', metavar='20240501', default=False, required=True)
robots.add_argument('-r', help='Show response body', action='store_true')

# add sitemap subparser
sitemap = subparser.add_parser("sitemap", help='sitemap subcommand')
sitemap.add_argument('-d', type=str, help='Set target domain', metavar='example.com', default=False, required=True)
sitemap.add_argument('-f', type=fromm, help='From date', metavar='20020501', default=False, required=True)
sitemap.add_argument('-t', type=to, help='To date', metavar='20240501', default=False, required=True)
sitemap.add_argument('-r', help='Show response body', action='store_true')

# parse argument
args = parser.parse_args()

if args.command == "robots":

    # store variable
    domain = args.d
    from_date = args.f
    to_date = args.t
    response = args.r

    # to string variable
    fd = str(from_date)
    td = str(to_date)

    def daterange(start_date: date, end_date: date):
        days = int((end_date - start_date).days)
        for n in range(days):
            yield start_date + timedelta(n)

    start_date = date.fromisoformat(fd)
    end_date = date.fromisoformat(td)

    for single_date in daterange(start_date, end_date):
        results = client.search(domain + "/robots.txt", from_date=single_date)
        record = next(results)
        print(Fore.BLUE + Style.BRIGHT + str(record.timestamp) + " " + Fore.WHITE + str(record.view_url))

        # show response
        if response:
            request = requests.get(record.url)
            print(request.text)
            print("")

if args.command == "sitemap":

    # store variable
    domain = args.d
    from_date = args.f
    to_date = args.t
    response = args.r

    # to string variable
    fd = str(from_date)
    td = str(to_date)

    def daterange(start_date: date, end_date: date):
        days = int((end_date - start_date).days)
        for n in range(days):
            yield start_date + timedelta(n)

    start_date = date.fromisoformat(fd)
    end_date = date.fromisoformat(td)

    for single_date in daterange(start_date, end_date):
        results = client.search(domain + "/sitemap.xml", from_date=single_date)
        record = next(results)
        print(Fore.BLUE + Style.BRIGHT + str(record.timestamp) + " " + Fore.WHITE + str(record.view_url))

        # show response
        if response:
            request = requests.get(record.url)
            print(request.text)
            print("")
