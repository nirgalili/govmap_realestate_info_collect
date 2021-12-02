from bs4 import BeautifulSoup
import pandas as pd

'''
go to govmap site
create polygon on area of interest real estate
after table with info of latest deals open press F12
copy the class "realsestate-items-wrapper table-mode scrollWrapper"
create txt file with the copied text
put the file in the directory

after running open the file with open in exel 
'''

with open('mozkin_1.txt', encoding="utf8") as file:
    print(type(file))
    # print(file.read())
    site_text = file.read()
# print(site_text)

soup = BeautifulSoup(site_text, "lxml")


def create_list_for_column(class_name: str, key:str):
    temp_list_not_in_text = soup.find_all(class_=class_name)
    new_list = []
    for item in temp_list_not_in_text:
        if class_name == "price-deal cell":
            new_list.append(item.get_text().split()[0])
        elif key == "gush":
            gush_helka_list = item.get_text().split("-")[0]
            new_list.append(gush_helka_list)
        elif key == "helka":
            gush_helka_list = item.get_text().split("-")[1]
            new_list.append(gush_helka_list)
        else:
            new_list.append(item.get_text())
    return new_list


column_classes_dict = {
    "sale date": "first sale-date cell",
    "address": "address-text",
    "neighborhood": "neighborhood-text",
    "gush": "gush-helka cell",
    "helka": "gush-helka cell",
    "asset-type": "asset-type cell",
    "rooms": "rooms cell",
    "floor": "floor cell ellipsis-text",
    "area": "mr cell",
    "price": "price-deal cell",
}


new_dict = {}
for key, value in column_classes_dict.items():
    new_list = create_list_for_column(value, key)
    new_dict[key] = new_list
# print(new_dict)

df = pd.DataFrame.from_dict(new_dict, orient='index')
df = df.transpose()
df.to_csv("new_tsv_file_1.tsv", sep="\t")

print(df.head())
# print(df.head().loc[:, "address"])
# print(df.head().loc[:, "gush"])
# print(df.head().loc[:, "helka"])