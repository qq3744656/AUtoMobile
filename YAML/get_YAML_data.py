import yaml

with open("./yaml.yml", "r", encoding="utf-8") as f:
    # 会返回一个数据字典
    data = yaml.safe_load(f)
    print(data)
    print(type(data))
