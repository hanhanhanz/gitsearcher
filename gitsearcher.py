import requests
import time
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

wordlist = "alldorksv3"
seeds = "seeds"

headers = {
    'Host': 'api.github.com',
    'User-Agent': 'python-requests/2.25.1',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Authorization': 'token YOURGITHUBTOKEN',
}


with open(wordlist) as w:
        n = 1
        for line in w:
                with open(seeds) as s:
                        for seed in s:
                                print("trial " + str(n) + " " + line.strip())
         

                                params = {
                                    'q': seed + ' ' + line,
                                }
                                response = requests.get('https://api.github.com/search/code', params=params, headers=headers, verify=False)
                                #print(response.status_code)
                                jres = response.json()
                                if response.status_code == 200 and (jres["total_count"] != 0):
                                        res = "Hit=" + str(n) + " seed=" + seed.strip()  + " payload=" + line.strip() + " res=" + str(len(response.content))
                                        with open("res2", 'a') as f:
                                                f.write(res + "\n")
                                elif response.status_code == 403:
                                        time.sleep(10)
                                else:
                                        pass
                                time.sleep(35)
                                n += 1

