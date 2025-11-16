import json


def load_data(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return data

def save_data(path, data: list):
    with open(path, 'w') as f:
        json.dump(data, f)


def save_stats(url, method, time):
    path = "data/endpoints_data.json"
    list_stats = load_data(path)

    for endpoint in list_stats:
        if endpoint["url"] == url and endpoint["method"] == method:
            endpoint["stats"]["total_requests_received"] += 1
            endpoint["stats"]["avg_handling_time"] = (endpoint["stats"]["avg_handling_time"]  + time) / endpoint["stats"]["total_requests_received"]
            save_data(path, list_stats)
            return
    
    new_ep =  {"url": url,
                "method": method,
                "stats": {
                "total_requests_received": 1,
                "avg_handling_time": time
                }
            }
    
    list_stats.append(new_ep)
    save_data(path, list_stats)
        



# [
# {
# "url": "/atbash",
# "method": "POST",
# "stats": {
# "total_requests_received": 12,
# "avg_handling_time": 10.4
# }
# }
# ]
