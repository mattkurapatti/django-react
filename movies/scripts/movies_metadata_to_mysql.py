import xlrd
from movies.models import Movie

# Open the workbook and define the worksheet
book = xlrd.open_workbook("movies_metadata.xlsx")
sheet = book.sheet_by_name("movies_metadata")
Movie.objects.all().delete()

# Establish a MySQL connection
# database = MySQLdb.connect(host="127.0.0.1", user="root", passwd="zvrPri3352", db="movie_project")

# Get the cursor, which is used to traverse the database, line by line
# cursor = database.cursor()


# Create the INSERT INTO sql query
# query = """INSERT INTO movies_movie (title, tagline, overview, vote_average, keywords) VALUES (%s, %s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
    movie_id = sheet.cell(r, 5).value
    title = sheet.cell(r, 20).value
    match_reason = ""
    tagline = sheet.cell(r, 19).value
    overview = sheet.cell(r, 9).value
    vote_average = sheet.cell(r, 22).value
    # Assign values from each row
    try:
        value = Movie(movie_id=movie_id, title=title, match_reason=match_reason,
                      tagline=tagline, overview=overview, vote_average=vote_average)
        value.save()
    except Exception:
        print(str(movie_id) + " " + title)

    # Execute sql Query
    # cursor.execute(query, values)

# Close the cursor
# cursor.close()

# Commit the transaction
# database.commit()

# Close the database connection
# database.close()

# Print results
print("")
print("All Done! Bye, for now.")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
# print ("I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!")
