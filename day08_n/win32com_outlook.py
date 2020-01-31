import win32com.client as win32
import pandas as pd
from pathlib import Path
from datetime import date


to_email = """
Lincoln, Abraham <honest_abe@example.com>; chris@example.com
"""

cc_email = """
Franklin, Benjamin <benny@example.com>
"""

# Read in the remote data file
df = pd.read_csv("https://github.com/johnny/data/sample-sales-tax.csv?raw=True")

# Define the full path for the output file
out_file = Path.cwd() / "tax_summary.xlsx"

# Do some summary calcs
# In the real world, this would likely be much more involved
df_summary = df.groupby('category')['ext price', 'Tax amount'].sum()

# Save the file as Excel
df_summary.to_excel(out_file)

# Open up an outlook email
outlook = win32.gencache.EnsureDispatch('Outlook.Application')
new_mail = outlook.CreateItem(0)

# Label the subject
new_mail.Subject = "{:%m/%d} Report Update".format(date.today())

# Add the to and cc list
new_mail.To = to_email
new_mail.CC = cc_email

# Attach the file
attachment1 = out_file

# The file needs to be a string not a path object
new_mail.Attachments.Add(Source=str(attachment1))

# Display the email
new_mail.Display(True)