import requests
from pprint import pprint

import numpy as np

def get(url: str):
  r_get = requests.get(url)
  if r_get.status_code == 200:
    # pprint(r_get.json())
    return r_get.json()

def post(url: str, items):
  # items = {
  #   'users': [
  #     {
  #       "id": "10",
  #       "rank": [ "CONTENT_11mlakf", "CONTENT_2", "CONTENT_3" ]
  #     },
  #     {
  #       "id": "754742998550712320",
  #       "rank": [ "CONTENT_1", "CONTENT_2", "CONTENT_3" ]
  #     }
  #   ]
  # }

  r_post = requests.post(url+"/register", json=items)
  if r_post.status_code == 200:
    pprint(r_post.json())


if __name__ == '__main__':
  url = "https://techfusion-studio.com/Oma-Ben/recommend"
  
  # get(url)

  # items = {
  #   'users': [
  #     {
  #       "id": "10",
  #       "rank": [ "CONTENT_11mlakf", "CONTENT_2", "CONTENT_3" ]
  #     },
  #     {
  #       "id": "754742998550712320",
  #       "rank": [ "CONTENT_1", "CONTENT_2", "CONTENT_3" ]
  #     }
  #   ]
  # }
  # post(url, items)

  # items = get(url)
  # pprint(items)
  # for k, v in items.items():
  #   id = k
  #   rank = ["", "", ""]
  #   print(v["own"] + v["other"])
  #   print(len(v["own"]))
  #   print(len(v["other"]))

  ar = np.array([[0.99999976, 0.96970403, 0.7450729 , 0.6458974 , 0.6031469 ],
           [0.96970403, 1.0000002 , 0.7233708 , 0.6374834 , 0.59641033],
           [0.7450729 , 0.7233708 , 1.0000002 , 0.6782884 , 0.62431043],
           [0.6458974 , 0.6374834 , 0.67828834, 1.0000001 , 0.8846145 ],
           [0.603147  , 0.5964103 , 0.62431043, 0.8846146 , 1.0000002 ]])
  print(ar)
  print(ar.ravel())
  print(np.argsort(ar.ravel()))
  print(np.argsort(ar.ravel()) % 5)
  print((np.argsort(ar.ravel()) % 5)[:3])
  
