import yaml
import json


class GetData:

    def get_yamle_data(self, url):
        with open(url, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def get_json_data(self, url):
        with open(url, "r", encoding="utf-8") as f:
            return json.load(f)
