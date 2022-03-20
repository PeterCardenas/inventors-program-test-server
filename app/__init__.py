from flask import Flask, request
import random
import time

app = Flask(__name__)

@app.route("/")
def root():
  arr_len = request.args.get("arrlen", default=2500, type=int)
  num_itrs = request.args.get("itrs", default=1000, type=int)
  start = time.time()
  arr = list(range(arr_len))
  for _ in range(num_itrs):
    random.shuffle(arr)
    arr.sort()
  duration = time.time() - start
  return f"<p>Shuffled a %d length array for %d iterations. Took %s seconds</p>" % (arr_len, num_itrs, duration)
