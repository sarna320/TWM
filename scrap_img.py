import urllib.request
import time

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)


urls_to_scrape = []
with open("urls_of_img_to_scrape.txt", "r") as file:
    for line in file:
        urls_to_scrape.append(line)
# print(urls_to_scrape)

count=0
for i, url in enumerate(urls_to_scrape):
    path="images/"
    if count==0:
        path+="patryk"
    elif count==1:
        path+="pawel"
    else:
        path+="piotrek"
    path+="/"
    name = url.split("/")[-2]+".jpg"
    path+=name
    try:
        urllib.request.urlretrieve(url, path)
    except:
        continue
    if count!=2:
        count+=1
    else:
        count=0
    print(str(round(i/len(urls_to_scrape)*100,2))+"%")
    time.sleep(0.2)
        
