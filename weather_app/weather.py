from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root = Tk()
root.title('a title')
root.iconbitmap("C:/Users/User/Desktop/gui/photos/python_logo.ico")
root.geometry("600x100")


# Create Zipcode lookup function
def zipLookUp():
    # zip.get()
    # zipLabel = Label(root, text=zip.get())
    # # zipLabel.pack()
    # zipLabel.grid(row=1, column=0, columnspan=2)
    try:
        # api_requests = requests.get()
        api_requests = requests.get()
        api = json.loads(api_requests.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#00e400"
        elif category == "Moderate":
            weather_color = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff7e00"
        elif category == "Unhealthy":
            weather_color = "ff0000"
        elif category == "Very Unhealthy":
            weather_color = "#99004c"
        elif category == "Hazardous":
            weather_color = "#7e0023"

        root.configure(background=weather_color)
        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20),
                    background=weather_color)
        # myLabel.pack()
        myLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
            api = "Error..."



zip = Entry(root)
# zip.pack()
zip.grid(row=0, column=0, sticky=W+E+N+S)

zipButton = Button(root, text="Lookup Zipcode", command=zipLookUp)
# zipButton.pack()
zipButton.grid(row=0, column=1, sticky=W+E+N+S)


root.mainloop()
