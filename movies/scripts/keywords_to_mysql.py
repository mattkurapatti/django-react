import json
import xlrd
from movies.models import Movie, Keyword
# Open the workbook and define the worksheet
book = xlrd.open_workbook("keywords.xlsx")
sheet = book.sheet_by_name("keywords")

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
    if r % 5000 == 0:
        print(r)
    mov_id = int(sheet.cell(r, 0).value)
    try:
        movie = Movie.objects.get(movie_id=mov_id)
    except Exception:
        continue
    raw_keywords = str(sheet.cell(r, 1).value)
    # print(raw_keywords)
    try:
        json_keywords = json.loads(raw_keywords)
    except json.JSONDecodeError:
        print(raw_keywords)
        continue
    for keyword in json_keywords:
        # keyword_id = keyword['id']
        wrd = keyword['name']
        if Keyword.objects.filter(word=wrd).exists():
            keyword = Keyword.objects.get(word=wrd)
        else:
            keyword = Keyword(word=wrd)
            keyword.save()
        keyword.movies.add(movie)



    # Assign values from each row

# Print results
print("")
print("All Done! Bye, for now.")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
# print ("I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!")
