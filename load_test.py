import urllib.request
import time
import threading

results = []

def make_request():
    start = time.time()
    try:
        urllib.request.urlopen("http://localhost:5000/")
        results.append(time.time() - start)
    except Exception as e:
        print(f"Erreur: {e}")

# 100 requêtes, 10 en simultané
threads = []
start_total = time.time()
for i in range(100):
    t = threading.Thread(target=make_request)
    threads.append(t)
    t.start()
    if len(threads) % 10 == 0:
        for t in threads:
            t.join()
        threads = []

total_time = time.time() - start_total
print(f"Requests/sec: {100/total_time:.2f}")
print(f"Average: {sum(results)/len(results):.4f} secs")
print(f"Fastest: {min(results):.4f} secs")
print(f"Slowest: {max(results):.4f} secs")
