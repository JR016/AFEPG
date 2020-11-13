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

import os, tkinter, shutil, copy
from tkinter import messagebox

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

def writelines_infile(filename,lines):
    """Writelines in the specific file"""

    with open(filename,"w") as file:
        file.writelines(lines)

#THE FILE MANAGER CLASS THAT MAKES EVERYTHING WORK
        
class FileManager(object):
    """Creates a Folder and Files within it and Autofills those Files."""

    #Dictionary that defines file and it's autocontent

    FILE_N_CONTENT = {
        "html" : [
            "<!DOCTYPE html> \n\n",
             "<html> \n\n",
             "    <head> \n\n",
             "        <meta charset=\"UTF-8\"> \n\n",
             "        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n\n",
             "        <title>Default Title</title> \n\n",
             "    </head> \n\n",
             "    <body> \n",
             "    </body> \n\n",
             "</html>"
            ],
        
        "css"  : [
            "             /*Base Styling*/ \n\n\n\n",
            "* \n",
            "{ \n",
            "    -webkit-box-sizing:border-box; \n",
            "    -moz-box-sizing:border-box; \n",
            "    box-sizing:border-box; \n",
            "} \n\n\n\n",
            "             /*Mobile Devices Styling*/ \n\n\n\n",
            "@media screen and (min-width: 320px) and (max-width: 479px) \n",
            "{} \n\n\n\n",
            "             /*Tablet Devices Styling*/ \n\n\n\n",
            "@media screen and (min-width: 480px) and (max-width: 959px) \n",
            "{} \n\n\n\n",
            "             /*Desktop Devices Styling*/ \n\n\n\n",
            "@media screen and (min-width: 960px) \n",
            "{}"]
        }

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
        if not self.folder_created or not self.files_created or not self.autofilled:
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
                open(self.common_filenames + ".html","x").close()

            if self.created_files["css"]:
                open(self.common_filenames + ".css","x").close()

            if self.created_files["js"]:
                open(self.common_filenames + ".js", "x").close()

        except KeyError as not_in_dict:
            self.files_created = False
            show_error("KeyError", f"'{not_in_dict}' does not exist in {self.created_files}.")

    def autofill_files(self):
        """Autofill selected files by the user."""

        #File Names for references
        self.css_filename = self.folder_name + ".css" 
        self.js_filename = self.folder_name + ".js"

        #Content that will be automatically written in HTML and CSS files if possible
        self.html_autocontent = None
        self.css_autocontent = None

        try:
           
            #Css is autofilled
            if self.autofilled_files["css"]:
                writelines_infile(self.common_filenames + ".css",
                                  FileManager.FILE_N_CONTENT["css"])

            #If Html is autofilled
            if self.autofilled_files["html"]: #Autofill HTML
                        
                #Dictionary for css and js references to use in html files

                references = {
                    "css_reference" : f"        <link rel=\"stylesheet\" href=\"{self.css_filename}\"> <!--CSS Reference--> \n\n",
                    "js_reference"  : f"        <script src=\"{self.js_filename}\"></script> <!--JS Reference--> \n"
                    }

                #Deep copy of the html content
                html_copy_content = copy.deepcopy(FileManager.FILE_N_CONTENT["html"])

                #Indexes of key elements of html content used to attach dynamic content
                title_index = html_copy_content.index(html_copy_content[5]) #Values is 5
                body_index = html_copy_content.index(html_copy_content[7]) #Value is 7


                if self.created_files["css"]: #Autofill HTML and CSS

                    #Add CSS Reference to HTML autocontent copy
                    html_copy_content.insert(title_index + 1, references["css_reference"])

                    if self.created_files["js"]: #Autofill HTML, CSS and include JS

                        if self.js_position == "head": #Include JS in head

                            #Add JS Reference to HTML autocontent copy in the head
                            html_copy_content.insert(title_index + 2, references["js_reference"] + "\n")

                            #Autofill HTML file
                            writelines_infile(self.common_filenames + ".html",
                                              html_copy_content)

                        else: #Include JS in body

                            #Add JS Reference to HTML autocontent copy in the body
                            html_copy_content.insert(body_index + 2, references["js_reference"])

                            #Autofill HTML file
                            writelines_infile(self.common_filenames + ".html",
                                              html_copy_content)

                    else: #Just write the CSS Reference in HTML File

                            writelines_infile(self.common_filenames + ".html",
                                              html_copy_content)

                else: #Autofill HTML but not CSS

                    if self.created_files["js"]: #Autofill HTML and include JS

                        if self.js_position == "head": #Include JS in head
                            html_copy_content.insert(title_index + 1, references["js_reference"] + "\n")

                            #Autofill HTML file
                            writelines_infile(self.common_filenames + ".html",
                                              html_copy_content)

                        else: #Include JS in body
                            html_copy_content.insert(body_index + 1, references["js_reference"])

                            #Autofill HTML file
                            writelines_infile(self.common_filenames + ".html",
                                              html_copy_content)

                    else: #Only autofill HTML without CSS and JS
                        writelines_infile(self.common_filenames + ".html",
                                          html_copy_content)
            

        except KeyError as auto_error:
            self.autofilled = False
            show_error("KeyError", f"'{auto_error}' key does not exist in {self.autofilled_files}.")

        except AttributeError as atrie:
            self.autofilled = False
            show_error("Developer Error", f"{atrie}.\n\nIt's the developer's fault, they make mistakes too.")
                

    def destroy_all(self):
        """Destroy folder and files if some
        error happened while creating files or autofilling them."""

        if not self.files_created or not self.autofilled:
            shutil.rmtree(self.complete_foldername)
            
        
if __name__ == "__main__": 

    #Tell User this programme is not meant to be run directly
    show_warning("Import Warning",
                 "This script contains a Project Manager Class for the\n" \
                 + "\"Automatic Front End Project Generator\" programme." \
                 + "\n\nThis script IS NOT MEANT TO BE RUN DIRECTLY." \
                 + "\nPlease, IMPORT IT IN ANOTHER SCRIPT.")
    

