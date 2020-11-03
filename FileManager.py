#                            FileManager Object

#Created by JR016

#YOU MUST NEITHER TAKE COPYRIGHT FROM THIS SOFTWARE NOR COMMERCIALIZE IT
#THIS IS FREE OPEN-SOURCE SOFTWARE CREATED TO FACILITATE THE CREATION OF FRONT END PROJECTS

#THIS SCRIPT CONTAINS SOME COMMON GUI POP UP FUNCTIONS USED ACCROSS THE WHOLE
#"AFEPG" PROJECT AND THE FileManager CLASS THAT CREATES A FOLDER WITH THE
#FILES SPECIFIED BY THE USER WHEREVER THE USER WANTS AND AUTOFILLS THEM IF
#THE USER CHOOSES TO DO SO. (MAIN FUNCTIONALITY OF THE "AFEPG" PROJECT LIES HERE)

#I PLUBLISHED THE PROGRAMME WITH THE SOURCE CODE SO YOU CAN CHECK IT AND CREATE YOUR OWN VERSION WITH
#NEW FEATURES AND STUFF
#ENJOY IT AND HAVE FUN
#:)


#IMPORTS

import os
import tkinter
from tkinter import messagebox
import shutil

#COMMONLY USED FUNCTIONS

def show_error(title, error_message):
    """Show a GUI error message."""

    box = tkinter.Tk()
    box.withdraw()
    messagebox.showerror(title, error_message)
    box.destroy()

def show_warning(title, warning_message):
    """Shows a GUI warning message."""
    
    box = tkinter.Tk()
    box.withdraw()
    messagebox.showwarning(title, warning_message)
    box.destroy()

def show_info(title, info_message):
    """Shows info to the user."""

    box = tkinter.Tk()
    box.withdraw()
    messagebox.showinfo(title, info_message)
    box.destroy()

def writelines_infile(filename,lines,mode):
    """Writelines in the specific file"""

    with open(filename,mode) as file:
        file.writelines(lines)



#THE FILE MANAGER CLASS THAT MAKES EVERYTHING WORK
        
class FileManager(object):
    """Creates a Folder and Files within it and Autofills those Files."""

    def __init__(self, folder_name, folder_path,
                 files_to_create, files_to_autofill, js_position):
        
        """Initializes the FileManager with all the required
        information to work well."""

        self.folder_name = folder_name
        self.folder_location = folder_path
        self.complete_foldername = os.path.join(self.folder_location, self.folder_name)
        self.common_filenames = os.path.join(self.complete_foldername, self.folder_name)
        self.created_files = files_to_create
        self.autofilled_files = files_to_autofill
        self.js_position = js_position

        #Status attributes that track the success of this object operations
        self.folder_created = True
        self.files_created = True
        self.autofilled = True

        #Call this object methods
        self.create_folder()

        if self.folder_created:
            self.create_files()

            if self.files_created:
                self.autofill_files()

        #If there was an error creating files or autofilling them, delete everything.
        if not self.files_created or not self.autofilled:
            self.destroy_all()

        else:
            #All operations were successful
            show_info("Success Pop-Up", "All operations were successful.")

    def create_folder(self):
        """Create folder that will contain the files."""

        try:
            os.mkdir(self.complete_foldername)

        except FileNotFoundError as creation_error:
            self.folder_created = False
            show_error("Path Not Found", creation_error)
           

        except FileExistsError as exists_error:
            self.folder_created = False
            show_error("Folder Exists Error", exists_error)

    def create_files(self):
        """Create the required files within the created folder."""

        try:

            if self.created_files["html"]:
                open(self.common_filenames + ".htm","x").close()

            if self.created_files["css"]:
                open(self.common_filenames + ".css","x").close()

            if self.created_files["js"]:
                open(self.common_filenames + ".js", "x").close()

        except KeyError as not_in_dict:
            self.files_created = False
            show_error("KeyError", f"'{not_in_dict}' does not exist in {self.created_files}.")

    def autofill_files(self):
        """Autofill selected files by the user."""

        #File Names
        self.html_filename = self.folder_name + ".htm"
        self.css_filename = self.folder_name + ".css" 
        self.js_filename = self.folder_name + ".js"

        #Content that will be automatically written in HTML and CSS files if possible
        self.html_autocontent = None
        self.css_autocontent = None

        #Check if user wants to autofill the html file (Do some error handling)
        try:

            #Create a list that sequences all possible outcomes
            self.outcomes = [
                self.autofilled_files["html"],
                self.autofilled_files["css"],
                self.created_files["js"],
                self.js_position
                ]

            #All options to autofill HTML files
            if self.outcomes[0] and self.outcomes[1] and self.outcomes[2] and self.js_position == "head":
                #This option autofills HTML, CSS, JS is created and it puts it in the head

                self.html_autocontent = ["<!DOCTYPE html> \n\n",
                                "<html> \n\n",
                                "    <head> \n\n"
                                "        <meta charset=\"UTF-8\"> \n\n",
                                "        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <!--For Responsive Behaviour--> \n\n",
                                "        <title>Default Title</title> \n\n",
                                f"       <link rel=\"stylesheet\" href=\"{self.css_filename}\"> <!--CSS File Reference--> \n",
                                f"       <script src=\"{self.js_filename}\"></script> <!--JS File Reference--> \n\n",
                                "    </head> \n\n",
                                "    <body> \n",
                                "    </body> \n\n",
                                "</html>"]

                self.css_autocontent = ["/*Base Styling*/\n\n",
                                        "* \n",
                                        "{ \n",
                                        "    box-sizing: border-box; \n",
                                        "} \n\n\n\n",
                                        "/*Mobile Devices Styling*/\n\n",
                                        "@media (min-width: 320px) and (max-width: 479px) \n",
                                        "{} \n\n\n\n",
                                        "/*Tablet Devices Styling*/\n\n",
                                        "@media (min-width: 480px) and (max-width: 959px) \n",
                                        "{} \n\n\n\n",
                                        "/*Desktop Devices Styling*/\n\n",
                                        "@media (min-width: 960px) \n",
                                        "{}"]

                #Write content in files
                writelines_infile(self.common_filenames + ".htm",self.html_autocontent,"w")
                writelines_infile(self.common_filenames + ".css", self.css_autocontent,"w")

            elif self.outcomes[0] and self.outcomes[1] and self.outcomes[2] and self.js_position == "body":
                #This option autofills HTML, CSS,JS is created and it puts it in the body

                self.html_autocontent = ["<!DOCTYPE html> \n\n",
                                "<html> \n\n",
                                "    <head> \n\n"
                                "        <meta charset=\"UTF-8\"> \n\n",
                                "        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <!--For Responsive Behaviour--> \n\n",
                                "        <title>Default Title</title> \n\n",
                                f"       <link rel=\"stylesheet\" href=\"{self.css_filename}\"> <!--CSS File Reference--> \n\n",
                                "    </head> \n\n",
                                "    <body> \n",
                                f"       <script src=\"{self.js_filename}\"></script> <!--JS File Reference--> \n",
                                "    </body> \n\n",
                                "</html>"]

                self.css_autocontent = ["/*Base Styling*/\n\n",
                                        "* \n",
                                        "{ \n",
                                        "    box-sizing: border-box; \n",
                                        "} \n\n\n\n",
                                        "/*Mobile Devices Styling*/\n\n",
                                        "@media (min-width: 320px) and (max-width: 479px) \n",
                                        "{} \n\n\n\n",
                                        "/*Tablet Devices Styling*/\n\n",
                                        "@media (min-width: 480px) and (max-width: 959px) \n",
                                        "{} \n\n\n\n",
                                        "/*Desktop Devices Styling*/\n\n",
                                        "@media (min-width: 960px) \n",
                                        "{}"]

                #Write content in files
                writelines_infile(self.common_filenames + ".htm",self.html_autocontent,"w")
                writelines_infile(self.common_filenames + ".css", self.css_autocontent,"w")

            elif self.outcomes[0] and self.outcomes[1] and not self.outcomes[2]:
                #This option autofills HTML, CSS and JS is not created

                self.html_autocontent = ["<!DOCTYPE html> \n\n",
                                "<html> \n\n",
                                "    <head> \n\n"
                                "        <meta charset=\"UTF-8\"> \n\n",
                                "        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <!--For Responsive Behaviour--> \n\n",
                                "        <title>Default Title</title> \n\n",
                                f"       <link rel=\"stylesheet\" href=\"{self.css_filename}\"> <!--CSS File Reference--> \n\n",
                                "    </head> \n\n",
                                "    <body> \n",
                                "    </body> \n\n",
                                "</html>"]

                self.css_autocontent = ["/*Base Styling*/\n\n",
                                        "* \n",
                                        "{ \n",
                                        "    box-sizing: border-box; \n",
                                        "} \n\n\n\n",
                                        "/*Mobile Devices Styling*/\n\n",
                                        "@media (min-width: 320px) and (max-width: 479px) \n",
                                        "{} \n\n\n\n",
                                        "/*Tablet Devices Styling*/\n\n",
                                        "@media (min-width: 480px) and (max-width: 959px) \n",
                                        "{} \n\n\n\n",
                                        "/*Desktop Devices Styling*/\n\n",
                                        "@media (min-width: 960px) \n",
                                        "{}"]

                #Write content in files
                writelines_infile(self.common_filenames + ".htm",self.html_autocontent,"w")
                writelines_infile(self.common_filenames + ".css", self.css_autocontent,"w")

            elif self.outcomes[0] and not self.outcomes[1] and self.outcomes[2] and self.js_position == "head":
                #This option autofills HTML, not CSS and JS is created and referenced in the head.

                self.html_autocontent = ["<!DOCTYPE html> \n\n",
                                "<html> \n\n",
                                "    <head> \n\n"
                                "        <meta charset=\"UTF-8\"> \n\n",
                                "        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <!--For Responsive Behaviour--> \n\n",
                                "        <title>Default Title</title> \n\n",
                                f"       <script src=\"{self.js_filename}\"></script> <!--JS File Reference--> \n\n",
                                "    </head> \n\n",
                                "    <body> \n",
                                "    </body> \n\n",
                                "</html>"]

                #Write content in files
                writelines_infile(self.common_filenames + ".htm",self.html_autocontent,"w")

            elif self.outcomes[0] and not self.outcomes[1] and self.outcomes[2] and self.js_position == "body":
                #This option autofills HTML, not CSS and JS is created and referenced in the body

                self.html_autocontent = ["<!DOCTYPE html> \n\n",
                                "<html> \n\n",
                                "    <head> \n\n"
                                "        <meta charset=\"UTF-8\"> \n\n",
                                "        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <!--For Responsive Behaviour--> \n\n",
                                "        <title>Default Title</title> \n\n",
                                "    </head> \n\n",
                                "    <body> \n",
                                f"       <script src=\"{self.js_filename}\"></script> <!--JS File Reference--> \n",
                                "    </body> \n\n",
                                "</html>"]

                #Write content in files
                writelines_infile(self.common_filenames + ".htm",self.html_autocontent,"w")

            elif self.outcomes[0] and not self.outcomes[1] and not self.outcomes[2]:
                #This option autofills HTML, but not CSS neither creates JS

                self.html_autocontent = ["<!DOCTYPE html> \n\n",
                                "<html> \n\n",
                                "    <head> \n\n"
                                "        <meta charset=\"UTF-8\"> \n\n",
                                "        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> <!--For Responsive Behaviour--> \n\n",
                                "        <title>Default Title</title> \n\n",
                                "    </head> \n\n",
                                "    <body> \n",
                                "    </body> \n\n",
                                "</html>"]

                #Write content in files
                writelines_infile(self.common_filenames + ".htm",self.html_autocontent,"w")

            elif not self.outcomes[0] and self.outcomes[1]:
                #This option does not autofills HTML, but it autofills CSS

                self.css_autocontent = ["/*Base Styling*/\n\n",
                                        "* \n",
                                        "{ \n",
                                        "    box-sizing: border-box; \n",
                                        "} \n\n\n\n",
                                        "/*Mobile Devices Styling*/\n\n",
                                        "@media (min-width: 320px) and (max-width: 479px) \n",
                                        "{} \n\n\n\n",
                                        "/*Tablet Devices Styling*/\n\n",
                                        "@media (min-width: 480px) and (max-width: 959px) \n",
                                        "{} \n\n\n\n",
                                        "/*Desktop Devices Styling*/\n\n",
                                        "@media (min-width: 960px) \n",
                                        "{}"]

                writelines_infile(self.common_filenames + ".css", self.css_autocontent,"w")

            elif not self.outcomes[0] and not self.outcomes[1]:
                #This option does not autofill neither html nor css
                pass
                
            else:
                #If the user chooses an undefined choice (It it exists)
                show_warning("Invalid Choice", "Your pattern of selections is not defined " \
                             + "by this programme, try another one later.")
                self.autofilled = False
            

        except KeyError as auto_error:
            self.autofilled = False
            show_error("KeyError", f"'{auto_error}' key does not exist in {self.autofilled_files}.")

        except AttributeError as atrie:
            self.autofilled = False
            show_error("Developer Error", f"{atrie}.\n\nIt's the developer's fault, they make mistakes too.")
                

    def destroy_all(self):
        """Destroy folder and files if some
        error happened while creating files or autofilling them."""

        shutil.rmtree(self.complete_foldername)
            
        
if __name__ == "__main__": 

    #Tell User this programme is not meant to be run directly
    show_warning("Import Warning",
                 "This script contains a Project Manager Class for the\n" \
                 + "\"Automatic Front End Project Generator\" programme." \
                 + "\n\nThis script IS NOT MEANT TO BE RUN DIRECTLY." \
                 + "\nPlease, IMPORT IT IN ANOTHER SCRIPT.")
    

