import requests

signature = "s0Ju9AAgEBCwzpufd4dd9bNCb-AAO0V"
#signature= "s0Ju9AAgEBAq1O-Bd4dd9bNCZ-AAO0V"

referer = "https://www.tiktok.com/@ondymikula/video/6757762109670477061"

url = "https://m.tiktok.com/share/item/list?secUid=&id=&type=5&count=30&minCursor=0&maxCursor=0&shareUid=" + \
    "&_signature=" + signature
request = requests.get(url, headers={"method": "GET",
                                "accept-encoding": "gzip, deflate, br",
                                "Referer": referer,
                                "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
                                })

data = request.json()

print(data)
