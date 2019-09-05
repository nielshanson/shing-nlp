import requests
import json

doi_html="http://api.springernature.com/meta/v2/json?q=doi:"

api_key = "205ddb8c0eec0fa8bf11d10233717273"

def get_abstract(my_obj):
    return my_obj["records"][0]["abstract"]

def download_doi_obj(doi, api_key):
    this_url = doi_html + doi + "&api_key=" + api_key
    print(this_url)
    req = requests.get(this_url)
    my_obj = json.loads(req.text)
    return my_obj
    #print(json.dumps(my_obj, indent=4))

def download_and_extract_abstract(doi, api_key):
    my_obj = download_doi_obj(doi, api_key)
    abstract_text = get_abstract(my_obj)
    return abstract_text

test_doi = "10.1186/1471-2105-14-202"
test_abstract = download_and_extract_abstract(test_doi, api_key)
# print(test_abstract)

doi_list = [
    "10.1186/1741-7007-9-34",
    "10.1186/1471-2105-14-202"
]

for doi in doi_list:
    print("-----")
    print(download_and_extract_abstract(doi, api_key))
    print("-----")
