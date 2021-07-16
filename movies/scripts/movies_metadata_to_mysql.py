import xlrd
from movies.models import Movie

# Open the workbook and define the worksheet
book = xlrd.open_workbook("movies_metadata.xlsx")
sheet = book.sheet_by_name("movies_metadata")
Movie.objects.all().delete()

# Create a For loop to iterate through each row in the XLS file
for r in range(1, sheet.nrows):
    # populate fields with appropiate column indeces at row r
    movie_id = sheet.cell(r, 5).value
    title = sheet.cell(r, 20).value
    match_reason = ""
    tagline = sheet.cell(r, 19).value
    overview = sheet.cell(r, 9).value
    vote_average = sheet.cell(r, 22).value
    try:
        value = Movie(movie_id=movie_id, title=title, match_reason=match_reason,
                      tagline=tagline, overview=overview, vote_average=vote_average)
        value.save()
    except Exception:
        print("Error adding " + str(movie_id) + " " + title)

print("All Done!")
