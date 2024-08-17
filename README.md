![historian](output.png)
# historian.py
historian.py is python script that use wayback library to check robots.txt history   
# options
```bash
  -h, --help      show this help message and exit
  -d example.com  Set target domain
  -f 20020501     From date
  -t 20240501     To date
```
## Install requirements 
 ```bash
 pip install -r requirements.txt
 ```
## Usage
 ```bash
 python3 historian.py -d fuzzer.cloud -f 20210610 -t 20240801
 ```
