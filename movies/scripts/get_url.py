import urllib.request, json

key = "nLuRdJU7ilmshomzNmLM800CKr4jp1NnF9pjsnz4Jvx28fyBHA"
search = 'frozen' + ' movie poster'
search_url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI?pageNumber=1" \
             "&pageSize=1&q=" + search + "&rapidapi-key=" + "nLuRdJU7ilmshomzNmLM800CKr4jp1NnF9pjsnz4Jvx28fyBHA"
search_url = search_url.replace(' ', '%20')
print(search_url)
with urllib.request.urlopen(search_url) as url:
    data = json.loads(url.read().decode())
    pic_url = data['value'][0]['url']

print(pic_url)
