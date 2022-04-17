# Job Hunting app
# Job includes job title, company, multiple contacts (date, person, description)
# todo: external storage of data
# todo: read data from spreadsheet
# todo: search on company or person
# todo: display all jobs
# todo: display job by status
# todo: time-out job if have not heard back after two weeks? Should have checkbox to prevent this for specific jobs

# todo: JTG: descriptions can contain newlines and I'm not sure how that will work with reading this CSV

from tkinter import Tk, Label, Entry, Text, Button
from tkinter import messagebox
# import pandas as pd
import csv


def on_ok():
    job = {
        "position": position.get(),
        "company": company.get(),
        "location": location.get(),
        "description": description.get('1.0', 'end'),
    }
    if not job["company"]:
        messagebox.showwarning("Empty Field", "Company field may not be empty")
    else:
        # open the file in the write mode
        with open('files/csv_file', 'w') as f:
            w = csv.DictWriter(f, job.keys())
            w.writeheader()
            w.writerow(job)


# position, company, location, description, to-do list, contact list
root = Tk()
root.config(padx=5, pady=5)
position_label = Label(text="Position: ")
position_label.grid(row=0, column=0)
position = Entry()
position.grid(row=0, column=1)
company_label = Label(text="Company: ")
company_label.grid(row=1, column=0)
company = Entry()
company.grid(row=1, column=1)
location_label = Label(text="Location")
location_label.grid(row=2, column=0)

# ToDo: location -> own table with ids to cx so this should become a dropdown listbox
location = Entry()
location.grid(row=2, column=1)

description_label = Label(text="Description: ")
description_label.grid(row=3, column=0)
description = Text(width=40, height=10)
description.grid(row=3, column=1)

ok_button = Button(text="OK", command=on_ok)
ok_button.grid(row=9, column=0)
cancel_button = Button(text="Cancel", command=root.destroy)
cancel_button.grid(row=9, column=1)

root.mainloop()
