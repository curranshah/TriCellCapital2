import requests
valueactCIK = '0001418814'
r = requests.get('https://data.sec.gov/submissions/CIK' + valueactCIK + '.json')
print(r.text)