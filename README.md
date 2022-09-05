# feature-extraction
Hi, this project is a feature-extraction mechanism used to extract indicator based features.

To you this codes:
```bash
$git clone https://github.com/RezaQavi-git/featuer-extraction.git
$cd feature-extraction
$python3.6 main.py
```
features will extract to this path '/extracts/extracted_{COINNAME}_{DURATION}.csv'
    
For run locally, you should placed input file's in './data/' folder beside main.py, And then edit ./utils/config.py input file pattern.

For run with API call, you should just set coins list in 'main.py' and DURATION in './utils/config.py', then run code and enjoy.


to edit list of coins : ""edit coins list in main.py""

to edit list of functions(indicators) : ""edit functions list in main.py""
