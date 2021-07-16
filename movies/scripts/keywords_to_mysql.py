import json
import xlrd

from movies.models import Movie, Keyword
# Open the workbook and define the worksheet
book = xlrd.open_workbook("keywords.xlsx")
sheet = book.sheet_by_name("keywords")

# Create a For loop to iterate through each row in the XLS file
for r in range(1, sheet.nrows):
    if r % 5000 == 0:
        print(r)
    mov_id = int(sheet.cell(r, 0).value)
    # check if movie exists
    try:
        movie = Movie.objects.get(movie_id=mov_id)
    except Exception:
        continue
    raw_keywords = str(sheet.cell(r, 1).value)
    # try to load into json
    try:
        json_keywords = json.loads(raw_keywords)
    except json.JSONDecodeError:
        print(raw_keywords)
        continue
    for keyword in json_keywords:
        wrd = keyword['name']
        # get keyword if it already exists, otherwise create new keyword
        if Keyword.objects.filter(word=wrd).exists():
            keyword = Keyword.objects.get(word=wrd)
        else:
            keyword = Keyword(word=wrd)
            keyword.save()
        # add movie-keyword relationship
        keyword.movies.add(movie)

print("All Done!")

