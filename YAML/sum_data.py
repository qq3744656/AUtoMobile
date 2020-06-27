import yaml
import os

from Base.get_data import GetData
from utils import URL

url = URL + os.sep + "YAML" + os.sep + "sum_data.yml"


# def get_data(url=url):
#     data_info = []
#     with open(url, "r", encoding="utf-8") as f:
#         data = yaml.safe_load(f)
#         # print(data.get("sum_001").values())
#         for i in data.values():
#             info = []
#             info.append([i.get("a"),i.get("b"),i.get("c")])
#             # info.append(i.get("a"))
#             # info.append(i.get("b"))
#             # info.append(i.get("c"))
#             data_info.append(info)
#         print(data_info)
#     return data_info
def get_my_data(url=url):
    data_info = []
    data = GetData().get_yamle_data(url)
    for i in data.values():
        info = []
        info.append([i.get("a"), i.get("b"), i.get("c")])
        data_info.append(info)
    print(data_info)
    return data_info


if __name__ == '__main__':
    get_my_data(url)
