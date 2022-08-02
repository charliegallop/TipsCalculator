import csv
import os
import PIL.Image
from datetime import timedelta
from decimal import Decimal, ROUND_HALF_EVEN
from decimal import *
from tkinter import filedialog
from tkinter import *



# Method for rounding with decimals
def round_decimal(x):
  return x.quantize(Decimal(".01"), rounding=ROUND_HALF_EVEN)


def splashScreen():
    root = Tk()
    image_file = "splash.gif"
    #assert os.path.exists(image_file)
    # use Tkinter's PhotoImage for .gif files
    image = PhotoImage(file=image_file)
    # show no frame
    root.overrideredirect(True)
    width = image.width()
    height = image.height()
    root.geometry('%dx%d+%d+%d' % (width, height, root.winfo_screenwidth()/3.5, root.winfo_screenheight()*0.1))
    # take a .jpg picture you like, add text with a program like PhotoFiltre
    # (free from http://www.photofiltre.com) and save as a .gif image file
    canvas = Canvas(root, height=image.height(), width=image.width(), bg="brown")
    canvas.create_image(image.width()/2, image.height()/2, image=image)
    canvas.pack()
    # show the splash screen for 5000 milliseconds then destroy
    root.after(3000, root.destroy)
    root.mainloop()

# colour pallette
class colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# defining the actual calculator class
def calc_tips(tips):

# with loop to open and read file. filename is defined later on before the calc_tips() is called
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)

# creating a dictionary of employee and hours worked
        hours_worked = {}
        x = []
        for line in csv_reader:
            if line[0] != '':
                time_in = line[1]
                time_out = line[2]

                time_in_split = time_in.split(':')
                time_in_h = int(time_in_split[0])
                time_in_m = int(time_in_split[1])

                time_out_split = time_out.split(':')
                time_out_h = int(time_out_split[0])
                time_out_m = int(time_out_split[1])

                t1 = timedelta(hours=time_in_h, minutes=time_in_m)
                t2 = timedelta(hours=time_out_h, minutes=time_out_m)

                duration1 = str(t2 - t1)

                time = duration1.split(':')

                h1 = int(time[0])
                m1 = int(time[1])

                if line[3] != '':
                    time_in2 = line[3]
                    time_out2 = line[4]

                    time_in2_split = time_in2.split(':')
                    time_in2_h = int(time_in2_split[0])
                    time_in2_m = int(time_in2_split[1])

                    time_out2_split = time_out2.split(':')
                    time_out2_h = int(time_out2_split[0])
                    time_out2_m = int(time_out2_split[1])

                    t3 = timedelta(hours=time_in2_h, minutes=time_in2_m)
                    t4 = timedelta(hours=time_out2_h, minutes=time_out2_m)

                    duration2 = str(t4 - t3)

                    time2 = duration2.split(':')

                    h2 = int(time2[0])
                    m2 = int(time2[1])

                    results = Decimal((h1 + (m1/60)) + (h2 + (m2/60)))
                else:
                    results = Decimal(h1 + (m1/60))

                hours_worked[line[0]] = results
                # name = line[0]
                # print(f'{name} worked: ' + f'{str(hours_worked[name])} hours')
            else:
                next(csv_reader)

        tot_hours = (Decimal(sum(hours_worked.values())))
        print('Total hours worked is: ' + colour.PURPLE + f' {round_decimal(tot_hours)} hrs' + colour.END)

        hourly_wage = round_decimal(tips / tot_hours)
        print('The hourly rate is: ' + colour.PURPLE + str(hourly_wage) + ' £/hr' + colour.END)

        for key, value in hours_worked.items():
            tips_due = round_decimal(Decimal(value) * hourly_wage)
            print(colour.GREEN + f' {key} ' + colour.END + 'worked ' + colour.RED + f'{str(round_decimal(Decimal(value)))} hrs ' + colour.END + 'and gets: ' + colour.BLUE + f'£{tips_due}' + colour.END)
            x.append(tips_due)


run = True
start = True
x = 0

os.system('cls')
splScr = splashScreen()

# if __name__ == "__main__":
#     #If you don't do this, the splash screen will show, but wont render it's contents
#     while gtk.events_pending():
#         gtk.main_iteration()
#     #Here you can do all that nasty things that take some time.
#     sleep(3)
#     #We don't need splScr anymore.
#     splScr.window.destroy()
#     gtk.main()

while run:
    if start == True:
        print(colour.YELLOW + 'WELCOME TO THE TIPS CALCULATOR' + colour.END)
        greeting = ('Create an Excel sheet in the ' + colour.DARKCYAN + 'SAME LAYOUT ' + colour.END + 'as the sign-in sheet with a header for ' + colour.DARKCYAN + '"Name", "Time in", "Time out".' + colour.END + '\nFor ' + colour.DARKCYAN + 'SPLIT SHIFTS' + colour.END + ', simply add another set of "Time in" "Time Out" coloumns'
                     + '\nAll times must be in the ' + colour.DARKCYAN + '24HR FORMAT ' + colour.END + 'seperated by a ":" e.g 21:30. \nSave the Excel sheet as a ' + colour.DARKCYAN + 'CSV ' + colour.END + 'file')
        print(greeting)
        start = False
        x = 0
    else:
        #print('Would you like to calculate tips?')
        x = x+1
        if x <= 1:
            retry = input(colour.BLUE + "Read instructions above then type 'y' to start or 'help' to see an example spreadsheet" + colour.END + "> ").lower()
            x = x+1
        elif retry == 'help':
            imge = PIL.Image.open('example.jpg')
            imge.show()
            retry = 'y'
        else:
            retry = input(colour.BLUE + "Type 'y' to start again or 'help' to see an example spreadsheet" + colour.END + "> ").lower()

        if retry == 'y':
            print('Select your CSV file from the pop-up window')
            filename = filedialog.askopenfilename(initialdir= "/", title = 'Select CSV file', filetypes = (("CSV files", "*.csv"),))
            print('Selected file: ' + colour.PURPLE + filename + colour.END)
            tips = Decimal(input("How many tips were made? £"))
            calc_tips(tips)
        elif retry == 'help':
            imge = PIL.Image.open('example.jpg')
            imge.show()
            retry = 'y'
        else:
            break
