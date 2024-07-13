#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import time
from PIL import ImageTk, Image
from tkinter import ttk, messagebox
from playsound import playsound
import multiprocessing
from datetime import datetime


# Hours List.
hours_list = ['00', '01', '02', '03', '04', '05', '06', '07',
              '08', '09', '10', '11', '12', '13', '14', '15',
              '16', '17', '18', '19', '20', '21', '22', '23', '24']

# Minutes List.
minutes_list = ['00', '01', '02', '03', '04', '05', '06', '07',
                '08', '09', '10', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22', '23',
                '24', '25', '26', '27', '28', '29', '30', '31',
                '32', '33', '34', '35', '36', '37', '38', '39',
                '40', '41', '42', '43', '44', '45', '46', '47',
                '48', '49', '50', '51', '52', '53', '54', '55',
                '56', '57', '58', '59']

# Ringtones list.
ringtones_list = ['Tune_1', 'Tune_2', 'Tune_3',
                  'Tune_4', 'Tune_5']

# Ringtone Paths.
ringtones_path = {
    'Tune_1': 'D:/PROGRAMS/dabotics india/alarm clock/Ringtones/Tune_1.mp3',
    'Tune_2': 'D:/PROGRAMS/dabotics india/alarm clock/Ringtones/Tune_2.mp3',
    'Tune_3': 'D:/PROGRAMS/dabotics india/alarm clock/Ringtones/Tune_3.mp3',
    'Tune_4': 'D:/PROGRAMS/dabotics india/alarm clock/Ringtones/Tune_4.mp3',
    'Tune_5': 'D:/PROGRAMS/dabotics india/alarm clock/Ringtones/Tune_5.mp3'
}


class Alarm_Clock:
    def __init__(self, root):
        self.window = root
        self.window.geometry("580x580+0+0")
        self.window.title("PyClock")

        # Update the path to your image file here
        image_path = "D:/PROGRAMS/dabotics india/alarm clock/Images/image_1.jpg"
        try:
            self.bg_image = ImageTk.PhotoImage(Image.open(image_path))
        except FileNotFoundError:
            messagebox.showerror("Error", f"Image file '{image_path}' not found.")
            self.bg_image = None

        if self.bg_image:
            self.background = Label(self.window, image=self.bg_image)
            self.background.place(x=0, y=0, relwidth=1, relheight=1)
            
        # Display Label that shows the current time in the
        # first window
        self.display = Label(self.window, font=('Helvetica', 40),
                             bg='#d9d9d9', fg='#BD8334')
        self.display.place(x=40, y=130)

        # Calling the function.
        self.show_time()


        # Hour Label.
        hours_label = Label(self.window, text="Hours",
                            font=("times new roman", 20), bg='#d9d9d9', fg='black')
        hours_label.place(x=100, y=230)

        # Minute Label.
        minute_label = Label(self.window, text="Minutes",
                             font=("times new roman", 20), bg='#d9d9d9', fg='black')
        minute_label.place(x=360, y=230)

        # Hour Combobox.
        self.hours = StringVar()
        self.hours_combobox = ttk.Combobox(self.window,
                                           width=8, height=10, textvariable=self.hours,
                                           font=("times new roman", 15), background="#d9d9d9")
        self.hours_combobox['values'] = hours_list
        self.hours_combobox.current(0)
        self.hours_combobox.place(x=100, y=270)

        # Minute Combobox.
        self.minutes = StringVar()
        self.minutes_combobox = ttk.Combobox(self.window,
                                             width=8, height=10, textvariable=self.minutes,
                                             font=("times new roman", 15))
        self.minutes_combobox['values'] = minutes_list
        self.minutes_combobox.current(0)
        self.minutes_combobox.place(x=360, y=270)

        # Ringtone Label.
        ringtone_label = Label(self.window, text="Ringtones",
                               font=("times new roman", 20), bg='#d9d9d9', fg='black')
        ringtone_label.place(x=100, y=330)

        # Ringtone Combobox (Choose the ringtone).
        self.ringtones = StringVar()
        self.ringtones_combobox = ttk.Combobox(self.window,
                                               width=19, height=10, textvariable=self.ringtones,
                                               font=("times new roman", 17),background="#d9d9d9")
        self.ringtones_combobox['values'] = ringtones_list
        self.ringtones_combobox.current(0)
        self.ringtones_combobox.place(x=230, y=335)

        # Title or Message Label.
        message_label = Label(self.window, text="Message",
                              font=("times new roman", 20), bg='#d9d9d9', fg='black')
        message_label.place(x=100, y=380)

        # Message Entry box: This Message will show when
        # the alarm rings.
        self.message = StringVar()
        self.message_entry = Entry(self.window,
                                   textvariable=self.message, font=("times new roman", 17), width=21)
        self.message_entry.insert(0, 'Wake Up')
        self.message_entry.place(x=230, y=385)

        # Placing the set alarm button.
        # Font Type: relief solid font Helvetica.
        set_button = Button(self.window, text="Set Alarm",
                            font=('Helvetica', 15), bg="#BD8334", fg="black",
                            command=self.set_alarm_time)
        set_button.place(x=230, y=480)

    def set_alarm_time(self):
        alarm_time = f"{self.hours_combobox.get()}:{self.minutes_combobox.get()}"
        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
        try:
            while True:
                # The current time is in 24-hour format
                current_time = datetime.now()
                # Converting the current time into hours and minutes
                current_time_format = current_time.strftime("%H:%M")
                if current_time_format == alarm_time:
                    process = multiprocessing.Process(target=playsound,
                                                      args=(ringtones_path[self.ringtones_combobox.get()],))
                    process.start()
                    # Messagebox: This message box will show when the
                    # alarm rings.
                    messagebox.showinfo("Alarm", f"{self.message_entry.get()}, It's {alarm_time}")
                    process.terminate()
                    break
        except Exception as es:
            messagebox.showerror("Error!", f"Error due to {es}")    
        
    # This function shows the current time in the first window.
    def show_time(self):
        current_time = time.strftime('%H:%M:%S %p, %A')
        # Placing the time format level.
        self.display.config(text=current_time)
        self.display.after(100, self.show_time)


if __name__ == "__main__":
    root = Tk()
    # Object of Alarm_Clock class.
    obj = Alarm_Clock(root)
    root.mainloop()