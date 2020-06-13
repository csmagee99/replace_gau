import re

with open("subs.txt", "r") as a_file:
  for url in a_file:
    if "http://" or "https://" in url:
        new_list = url.replace("https://", "").replace("http://", "").replace("www.", "")
        print(new_list)
