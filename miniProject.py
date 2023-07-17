5# Assign the category and subcategory values 
to category and subcategory columns.

crowdfunding_info_df[["category","subcategory"]]  = 
crowdfunding_info_df["category & sub-category"].
str.split('/', n=1, expand=True)

crowdfunding_info_df.head(****)

https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html

#6 # Get the unique categories and subcategories in separate lists.

#7 how do you find how many values there are in a list?

#8 https://numpy.org/doc/stable/reference/routines.array-creation.html
Find info on Numerical ranges.

#9 list comprehension 
https://realpython.com/list-comprehension-python/#using-list-comprehensions
https://www.geeksforgeeks.org/python-list-comprehension/

# Use a list comprehension to add "cat" to each category_id. 
cat_ids = ["******" + str(xxxx) for xxxx in category_ids]

#10 
# Create a category DataFrame with the category_id array as the category_id and categories list as the category name.
category_df = xx.xxxxx({
    "xxxx": cat_ids,
    "category" : xxxxxxxx
})

#13 to_csv function, index=False

#15 .rename
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html


#16 

.astype(float)
https://www.geeksforgeeks.org/python-pandas-dataframe-astype/
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html



#18 
to_datetime
use unit='s' 
and strftime('%Y-%m-%d')

https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

https://docs.python.org/3/library/datetime.html#datetime.datetime.__format__



19
# Merge the campaign_df with the category_df on the "category" column and 
# the subcategory_df on the "subcategory" column.
campaign_merged_df = 
campaign_df.merge(xxxxxx, on='xxxxxx', how='xxxxxx').merge(subcategory_df, on='xxxxxxx', how='xxxxxx')


https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html

#20
# Drop unwanted columns
.drop axis=1


#23

import json
dict_values = []

for i, row in contact_info_df.iterrows():
    data = row['contact_info']
    xxxxxxxx = json.loads(data)
    # Iterate through each dictionary (row) and get the values for each row using list comprehension.
    row_values = [v for k, v in xxxxxx.items()]
    # Append the list of values for each row to a list. 
    dict_values.xxxxxx(xxxxxx)
	
#24
# Create a contact_info DataFrame and add each list of values, i.e., each row 
# to the 'contact_id', 'name', 'email' columns.

contacts_df = pd.DataFrame(xxxxx, columns=['xx', 'xx', 'xx'])	
	
	
#26
# Create a "first"name" and "last_name" column with the first and last names from the "name" column. 
str.split - what is the delimeter?

# Drop the contact_name column
use drop and axis=1


https://docs.python.org/3/howto/regex.html

	
31 
str.extract(r'(\d{4})')	
	
	
	
	
	
	
	
	
	












