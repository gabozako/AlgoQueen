import json
import requests


def getPhoneNumbers(country, phoneNumber):
    # Write your code here
    res = requests.get(url="https://jsonmock.hackerrank.com/api/countries?name=" + country).text
    res = json.loads(res)

    if not res["total"]:
        return -1

    calling_codes = list(map(int, res['data'][0]["callingCodes"]))
    calling_codes.sort(reverse=True)

    return "+" + str(calling_codes[0]) + " " + str(phoneNumber)