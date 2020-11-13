#                     Automatic Front-End Project Generator

#Created by JR016

#YOU MUST NEITHER TAKE COPYRIGHT FROM THIS SOFTWARE NOR COMMERCIALIZE IT
#THIS IS FREE OPEN-SOURCE SOFTWARE CREATED TO FACILITATE THE CREATION OF FRONT END PROJECTS

#THIS SCRIPT CONTAINS THE CODE REQUIRED FOR THE "AFEPG" APP TO EXECUTE

#I PLUBLISHED THE PROGRAMME WITH THE SOURCE CODE SO YOU CAN CHECK IT AND CREATE YOUR OWN VERSION WITH
#NEW FEATURES AND STUFF
#ENJOY IT AND HAVE FUN
#:)

#IMPORTS
import os, enhancedTk, FileManager
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import font
from PIL import ImageTk, Image #To work with images

#Global Constants
APP_FONTS = ("Arial", "Lucida Grande","Courier New", "Georgia", "Times New Roman")#Fonts for the GUI
PICS_FOLDERNAME = "images" #Name of the folder that contains the images of this programme
ICON_PATH = os.path.join(PICS_FOLDERNAME, "project.png") #Path to the window icon
PICS_PATH = (os.path.join(PICS_FOLDERNAME, "html.png"),
             os.path.join(PICS_FOLDERNAME, "css.png"),
             os.path.join(PICS_FOLDERNAME, "js.jpg")) #Path to programme's images

WIDTH = 650
HEIGHT = 550

def main():
    """Run the programme."""

    #Initialize SuperTk window Object
    window = enhancedTk.Super_Tk(title = "AFEPG",
                                 icon_path = ICON_PATH,
                                 width = WIDTH,
                                 height = HEIGHT,
                                 is_resizable = False)

    #Initialize Main Frame
    main_frame = ProjectGenerator(window,WIDTH,HEIGHT)
    main_frame.place(x = 0, y = 0)

    #Run GUI Mainloop (Always run at the end)
    window.mainloop()

    
class ProjectGenerator(Frame):
    """Main frame of the Front End Project Generator Programme."""

    def __init__(self,master, width, height):
        """Initialize the frame with all required attributes """

        #Call parent's constructor method       
        super(ProjectGenerator, self).__init__(master,
                                               width = width,
                                               height = height)

        #Methods to call right away
        self.add_stuff()

        #Attributes to handle GUI operations
        self.times_asked_folder = 0 #Times user asked for folder locations

    def add_stuff(self):
        """Add GUI widgets to the Frame"""

        #Create Main Title Label
        self.titleFont = font.Font(family = APP_FONTS[0], size = 25)
        self.title = ttk.Label(self,
                               text = "Automatic Front End Project Generator",
                               font = self.titleFont)
        
        self.title.place(x = 50, y = 60) #Place the widget on the GUI screen

        #Label to get Project Name
        self.questionsFont = font.Font(family = APP_FONTS[2], size = 12) #Font for label questions
        self.answersFont = font.Font(family = APP_FONTS[4], size = 12) #Font for user answers
        self.project_name = ttk.Label(self,
                                      text = "Project Name:",
                                      font = self.questionsFont)

        self.project_name.place(x = 120 , y = 150)

        #Entry Widget to get Project Name
        self.enter_name = ttk.Entry(self,font = self.answersFont)
        self.enter_name.place(x = 320, y = 150, width = 200)

        #Label to get Project Location
        self.project_location = ttk.Label(self,
                                          text = "Project Location:",
                                          font = self.questionsFont)
        self.project_location.place(x = 120, y = 200)

        #Entry Widget to get Project Location
        self.enter_location = ttk.Entry(self,
                                        font = self.answersFont)
        self.enter_location.place(x = 320, y = 200, width = 200)

        #Create Button to open filedialog to browse project location
        self.button_location = ttk.Button(self,
                                          text = "Browse",
                                          command = self.ask_folder)
        self.button_location.place(x = 550, y = 200)

        #Create a Label for Project Files
        self.project_files = ttk.Label(self,
                                       text = "Files",
                                       font = self.questionsFont)
        self.project_files.place(x = 303, y = 270)

        #Add Image for HTML
        self.html_pic = ImageTk.PhotoImage(file = PICS_PATH[0])
        self.html_label = ttk.Label(self)
        self.html_label.config(image = self.html_pic)
        self.html_label.place(x = 120, y = 350)

        #Add CSS Image
        self.css_pic = ImageTk.PhotoImage(file = PICS_PATH[1])
        self.css_label = ttk.Label(self)
        self.css_label.config(image = self.css_pic)
        self.css_label.place(x = 295, y = 350)

        #Add Js Image
        self.js_img = Image.open(PICS_PATH[2]).resize((64,64), Image.ANTIALIAS)
        self.js_pic = ImageTk.PhotoImage(self.js_img)
        self.js_label = ttk.Label(self)
        self.js_label.configure(image = self.js_pic)
        self.js_label.place(x = 480, y = 350)

        #Add Text Labels for Files
        self.html_text = ttk.Label(self,text = "HTML")
        self.html_text.place(x = 135, y = 310)

        self.css_text = ttk.Label(self, text = "CSS")
        self.css_text.place(x = 315, y = 310)

        self.js_text = ttk.Label(self, text = "JS")
        self.js_text.place(x = 505, y = 310)

        #Create File Checkboxes
        self.add_html = BooleanVar(self)
        self.add_css = BooleanVar(self)
        self.add_js = BooleanVar(self)

        self.html_cb = Checkbutton(self, variable = self.add_html, offvalue = False,
                                   onvalue = True)
        self.html_cb.select() #Select By Default
        self.html_cb.config(state = "disabled") #Don't Let User to Change it
        
        self.css_cb = Checkbutton(self, variable = self.add_css,
                                  offvalue = False, onvalue = True,
                                  command = self.show_CSS_autofill)
        
        self.js_cb = Checkbutton(self, variable = self.add_js,
                                 offvalue = False, onvalue = True,
                                 command = self.head_or_body)

        self.html_cb.place(x = 143, y = 440)
        self.css_cb.place(x = 320, y = 440)
        self.js_cb.place(x = 505, y = 440)

        #Create Optional Autofill CheckButtons
        self.auto_html = BooleanVar(self)
        self.auto_css = BooleanVar(self)

        self.auto_html_cb = Checkbutton(self, variable = self.auto_html,
                                        offvalue = False, onvalue = True,
                                        command = self.head_or_body)
        
        self.auto_css_cb = Checkbutton(self, variable = self.auto_css,
                                       offvalue = False, onvalue = True)

        self.auto_html_cb.place(x = 143, y = 470)

        #Autofill labels
        self.auto1 = ttk.Label(self, text = "Autofill HTML")
        self.auto1.place(x = 50, y = 473)

        self.auto2 = ttk.Label(self, text = "Autofill CSS")

        #Ask user if it's desired to add JS in the head or the body
        self.js_position = StringVar(self)
        self.js_position.set("body")
        
        self.js_head = Radiobutton(self, text = "Head", variable = self.js_position,
                                   value = "head")
        
        self.js_body = Radiobutton(self, text = "Body", variable = self.js_position,
                                   value = "body")

        #Create a Final Submit Button
        self.final_button = ttk.Button(self, text = "Create Project",
                                       width = 20, command = self.info_for_manager)
        self.final_button.place(x = 500, y = 515)    

    def ask_folder(self):
        """Opens a file dialog for a directory."""

        #Ask for a directory folder
        self.location = filedialog.askdirectory()
        
        #Increase the times the user pressed the button
        self.times_asked_folder += 1

        #Delete previous content if it exists
        if self.times_asked_folder > 1:
            self.enter_location.delete(0, END)

        #Add folder path to entry widget when selected
        self.enter_location.insert(0, self.location)

    def show_CSS_autofill(self):
        """Show the user the option to autofill CSS files."""

        if self.add_css.get():
            self.auto2.place(x = 230, y = 473)
            self.auto_css_cb.place(x = 320, y = 470)

        else:
            self.auto2.place_forget()
            self.auto_css_cb.place_forget()
            self.auto_css_cb.deselect()

    def head_or_body(self):
        """Ask users if they want their JS script on the head or the body."""

        if self.add_js.get() and self.auto_html.get():  #Don't show buttons if HTML is not autofilled   
            self.js_head.place(x = 450, y = 473)
            self.js_body.place(x = 530, y = 473)

        else:
            self.js_head.place_forget()
            self.js_body.place_forget()

    def info_for_manager(self):
        """Sets the information that will be passed to the FileManager."""

        #Only run manager if project name is not empty

        if len(self.enter_name.get()) > 0:  

            #Create a File Manager object that handles all the stuff (as a local variable)

            my_manager = FileManager.FileManager(
                self.enter_name.get(), #Project's Name
                self.enter_location.get(), #Project's Location
                {"html" : self.add_html.get(), "css" : self.add_css.get(), "js" : self.add_js.get()}, #Files to be created by the manager.
                {"html" : self.auto_html.get(), "css" : self.auto_css.get()}, #Files to be autofilled by the manager
                self.js_position.get() #Position of the JS file in HTML file if autofilled
                )

        else:
            FileManager.show_warning("Empty Name", "Cannot create project whose name is empty.")
        

#Run if script is called directly (not imported)
if __name__ == "__main__":
    main()
