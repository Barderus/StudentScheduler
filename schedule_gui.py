'''
Author: Gabriel dos Reis
Date: 12/4/2023
Description: This program creates a GUI to schedule students and courses.

        ** Struggling with adding multiple data from the file to the listbox. **
    
'''
import tkinter as tk
import student as stu
import course as crs
import tkinter.messagebox
import tkinter.filedialog
import tkinter.font

class ScheduleGUI:
    ''' This class creates a GUI to schedule students and courses.'''
    
    # Class level variables
    COURIER_FONT = "Courier"
    TIMES_FONT = "Times New Roman"
    BOLD_FONT = 1
    SIZE12_FONT = 12
    SIZE14_FONT = 14
    SIZE16_FONT = 16
    
    def __init__(self):
        
        ''' Initialize the GUI '''
       
        # Create a list of students and courses
        self.__student_list = []
        self.__course_list = []
        self.__student_dict = {}
        self.__selected_student_id = None

         
        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.title("Scheduler GUI")
        
        # Size of the window
        self.main_window.geometry("750x400+250+150")
        
        # Create frame to hold student widgets
        self.studentFrame = tk.Frame(self.main_window)
        self.studentFrame.grid(row=0, column=0, rowspan=3, columnspan=3)

        
        # Create some labels and entry for placement
        # Student name
        self.lblName = tk.Label(self.studentFrame, text= "Student Name: ")
        self.entryName = tk.Entry(self.studentFrame, width= 20)
        # Student ID
        self.lblID = tk.Label(self.studentFrame, text= "Student ID: ")
        self.entryID = tk.Entry(self.studentFrame, width= 20)
        # Student GPA
        self.lblGPA = tk.Label(self.studentFrame, text= "GPA: ")
        self.entryGPA = tk.Entry(self.studentFrame, width= 20)
        
        # Place widgets using grid on the student frame
        self.lblName.grid(row=0, column=0, padx=5, pady=3)
        self.entryName.grid(row=0, column=1, padx=5, pady=3)
        
        self.lblID.grid(row=1, column=0, padx=5, pady=3)
        self.entryID.grid(row=1, column=1, padx=5, pady=3)
        
        self.lblGPA.grid(row=2, column=0, padx=5, pady=3)
        self.entryGPA.grid(row=2, column=1, padx=5, pady=3)
        
        # Create frame to hold course widgets
        self.courseFrame = tk.Frame(self.main_window)
        self.courseFrame.grid(row=3, column=6, rowspan=3, columnspan=6,padx=50)

        # Crate some labels and entry for placement
        # Course ID
        self.lblCourseID = tk.Label(self.courseFrame, text= "Course ID: ")
        self.entryCourseID = tk.Entry(self.courseFrame, width= 20)
        # Course name
        self.courseName = tk.Label(self.courseFrame, text= "Course Name: ")
        self.entryCourseName = tk.Entry(self.courseFrame, width= 20)
        # Credit hours
        self.crHours = tk.Label(self.courseFrame, text= "Credit Hours: ")
        self.entryCrHours = tk.Entry(self.courseFrame, width= 20)
        
        # Places widgets using grid on the course frame
        self.lblCourseID.grid(row=0, column=6, padx=5, pady=3)
        self.entryCourseID.grid(row=0, column=7, padx=5, pady=3)
        
        self.courseName.grid(row=1, column=6, padx=5, pady=3)
        self.entryCourseName.grid(row=1, column=7, padx=5, pady=3)
        
        self.crHours.grid(row=2, column=6, padx=5, pady=3)
        self.entryCrHours.grid(row=2, column=7, padx=5, pady=3)
        
        # Create frames to hold buttons
        self.buttonStuFrame = tk.Frame(self.main_window)
        self.buttonCrsFrame = tk.Frame(self.main_window)

        # Create buttons
        # For the student frame
        self.addStu_button = tk.Button(self.buttonStuFrame, text="Add Student",
                                         command=self.add_student)
        self.showStu_button = tk.Button(self.buttonStuFrame, text="Display Students",
                                          command=self.display_students)
        # For the course frame
        self.addCourse_button = tk.Button(self.buttonCrsFrame, text="Add Course",
                                           command=self.add_course)        
        
        # Pack buttons in the frame
        self.addStu_button.pack(side= "left", padx = 5)
        self.showStu_button.pack(side= "left", padx = 5)
        self.addCourse_button.pack(side= "left", padx = 5)
        
        # Place the frames using grid
        self.buttonStuFrame.grid(row=5, column=0, columnspan=3, pady=5)
        self.buttonCrsFrame.grid(row=5, column=3, columnspan=6, pady=5)

        
        # Create a frame to hold list boxes and scrollbars
        self.displayStu_Frame = tkinter.Frame(self.main_window)   
             
        # Scrollbar and listbox to hold the student data
        self.stuscrollbar = tkinter.Scrollbar(self.displayStu_Frame, orient = tkinter.VERTICAL)
        self.stulistbox = tkinter.Listbox(self.displayStu_Frame,
                                        yscrollcommand = self.stuscrollbar.set, width= 50)
        self.stuscrollbar.config(command = self.stulistbox.yview)
        
        self.stuscrollbar.pack(side = "right", fill = tkinter.Y)
        self.stulistbox.pack(side = "left", fill = tkinter.BOTH, expand = 1)
        
        # Create frame to hold buttons and radio buttons
        self.control_frame = tk.Frame(self.main_window) 
        
        # Radio button for font family
        self.font_fam = tk.StringVar()
        self.font_fam.set(ScheduleGUI.COURIER_FONT)
        self.create_button = tk.Button(self.control_frame, text="Create schedule", width=15,
                                         command=self.create_schedule)
        self.font_label = tk.Label(self.control_frame, text = "Font Family")
        self.courier_button = tk.Radiobutton(self.control_frame, 
                                                  text = "Courier",
                                                  variable = self.font_fam,
                                                  value = ScheduleGUI.COURIER_FONT)
        
        self.times_button = tk.Radiobutton(self.control_frame, 
                                                text = "Times",
                                                variable = self.font_fam,
                                                value = ScheduleGUI.BOLD_FONT)
    
        # Radio button for font size
        self.font_size = tk.IntVar()
        self.font_size.set(self.SIZE12_FONT)
        self.data_check = tk.IntVar()
        self.data_check.set(0)
        
        self.size_label = tk.Label(self.control_frame, text = "Font Size")
        self.size12_button = tk.Radiobutton(self.control_frame,
                                                 text="12",
                                                 variable=self.font_size,
                                                 value=ScheduleGUI.SIZE12_FONT)
        self.size14_button = tk.Radiobutton(self.control_frame,
                                                 text="14",
                                                 variable=self.font_size,
                                                 value=ScheduleGUI.SIZE14_FONT)
        self.size16_button = tk.Radiobutton(self.control_frame,
                                                 text="16",
                                                 variable=self.font_size,
                                                 value=ScheduleGUI.SIZE16_FONT)

        # Check button for font weight
        self.font_weight = tkinter.IntVar()
        self.font_weight.set(ScheduleGUI.BOLD_FONT)   
        self.bold_check = tkinter.Checkbutton(self.control_frame, text = "Bold",
                                              variable = self.font_weight)              

        
        # Grid layout for the widgets in the control frame
        self.create_button.grid(row=1, column=4, pady=5, padx=5, sticky="w")
        self.font_label.grid(row=0, column=1, pady=5, padx=10, sticky="w")
        self.size_label.grid(row=0, column=2, pady=5, padx=10, sticky="w")

        self.courier_button.grid(row=1, column=1, pady=5, padx=10, sticky="w")
        self.times_button.grid(row=2, column=1, pady=5, padx=10, sticky="w")

        self.size12_button.grid(row=1, column=2, pady=5, padx=10, sticky="w")
        self.size14_button.grid(row=2, column=2, pady=5, padx=10, sticky="w")
        self.size16_button.grid(row=3, column=2, pady=5, padx=10, sticky="w")
        
        self.bold_check.grid(row=0, column=4, pady=5, padx=10, sticky="w")
        
        self.save_button = tk.Button(self.control_frame, text="Save to file", command=self.save_file)
        self.save_button.grid(row=3, column=0, pady=5, padx=10, sticky="w")
        
        self.load_button = tk.Button(self.control_frame, text="Load from file", command=self.load_data)
        self.load_button.grid(row=4, column=0, pady=5, padx=10, sticky="w")

        # Place frames into the window
        self.studentFrame.grid(row=0, column=0, rowspan=3, columnspan=3)
        self.courseFrame.grid(row=0, column=3, rowspan=3, columnspan=6)
        self.displayStu_Frame.grid(row=7, column=0, rowspan=3, columnspan=3, padx=10)
        self.control_frame.grid(row=9, column=3, rowspan=3, columnspan=3, padx = 20)
        
        # Create a menu bar at top of windw
        self.menubar = tkinter.Menu(self.main_window)
        self.main_window.config(menu = self.menubar)
        
        # Add file menu options
        self.file_menu = tkinter.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "File", menu = self.file_menu)
        self.file_menu.add_command(label = "Save file...", command = self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit", command = self.exit_app)
        
        # Help menu option
        self.help_menu = tk.Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = "Help", menu = self.help_menu)
        self.help_menu.add_command(label = "About",
                                   command = self.show_about)
       
        # Start with the window event loop
        self.main_window.mainloop()
        
    def add_student(self):
        
        ''' This method adds a student to the list '''
        # Get text from entry fields
        stu_id = self.entryID.get()
        stu_name = self.entryName.get()
        stu_gpa = self.entryGPA.get()

        # Check for empty string
        if not stu_id or not stu_name or not stu_gpa:
            # Display error message box
            tkinter.messagebox.showerror("ERROR", "All fields must be filled.")
            self.entryID.focus()
            return

        try:
            # Try to convert gpa to a float
            stu_gpa = float(stu_gpa)
        except ValueError:
            # Display an error if the conversion fails
            tkinter.messagebox.showerror("ERROR", "Student GPA must be a float.")
            self.entryGPA.focus()
            return

        # Check if the student ID already exists
        for student_obj in self.__student_list:
            if student_obj.id_num == stu_id:
                # Display an error if the ID is already in use
                tkinter.messagebox.showerror("ERROR", "Student ID already exists.")
                self.entryID.focus()
                return

        # Create a student object and add it to the list
        new_student = stu.Student(name=stu_name, id_num=stu_id, gpa=stu_gpa)
        self.__student_list.append(new_student)

        # Display confirmation message box
        tkinter.messagebox.showinfo("Information", "Student added to the list")

        # Clear the entry fields
        self.clear_stuentry()
  
    def add_student_from_file(self, stu_id, stu_name, stu_gpa, stu_courses=None):
        ''' This method adds a student to the list from a file '''
        
        # Check if the student ID already exists
        for student_obj in self.__student_list:
            if student_obj.id_num == stu_id:
                # Display an error if the ID is already in use
                tkinter.messagebox.showerror("ERROR", "Student ID already exists.")
                return

        # Validate stu_courses
        if stu_courses is None:
            tkinter.messagebox.showerror("ERROR", "Invalid course data.")
            return

        stu_courses = ",".join(stu_courses)
        
        # Create a student object and add it to the list
        new_student = stu.Student(name=stu_name, id_num=stu_id, gpa=float(stu_gpa))
        self.stulistbox.insert(tk.END, new_student)


        # Split courses by comma and then extract course details
        for course_str in stu_courses.split(','):
            # Split course details by colon
            course_parts = course_str.strip().split(':')

            # Check if the course has the expected format
            if len(course_parts) == 2:
                course_num, course_info = course_parts
                # Extract course name and credit hours
                course_name, credit_hours = course_info.strip().split('(')
                credit_hours = credit_hours.rstrip(')').strip()

                # Create a Course object and add it to the student
                new_course = crs.Course(num=course_num, name=course_name, crHours=int(credit_hours))
                new_student.addCourse(new_course)
            else:
                tkinter.messagebox.showerror("ERROR", "Invalid course data.")

        # Add the new student to the list
        self.__student_list.append(new_student)

        # Display confirmation message box
        tkinter.messagebox.showinfo("Information", "Student added to the list")

    def add_course(self):
        ''' This method adds a course to the selected student'''
        # Check if a student is selected
        if self.__selected_student_id is None:
            tkinter.messagebox.showerror("Error", "Please select a student first.")
            return

        # Get text from entry fields
        crs_ID = self.entryCourseID.get()
        crs_name = self.entryCourseName.get()
        crs_crdHours = self.entryCrHours.get()

        # Check for empty string
        if not crs_ID or not crs_name or not crs_crdHours:
            tkinter.messagebox.showerror("ERROR", "All fields must be filled.")
            return

        try:
            # Try to convert credit hours to an integer
            crs_crdHours = int(crs_crdHours)
        except ValueError:
            tkinter.messagebox.showerror("ERROR", "Credit hours must be an integer.")
            self.entryCrHours.focus()
            return

        # Create a Course object
        new_course = crs.Course(num=crs_ID, name=crs_name, crHours=crs_crdHours)

        # Find the selected student in the list
        selected_student = None
        for student_obj in self.__student_list:
            if student_obj.id_num == self.__selected_student_id:
                selected_student = student_obj
                break

        if selected_student:
            # Add the course to the selected student's list of courses
            selected_student.courses.add(new_course)
            tkinter.messagebox.showinfo("Information", "Course added to the selected student.")

        # Clear the entry fields
        self.clear_crsentry()
        # PRINT FOR TESTING
        print(f"Selected Student ID: {self.__selected_student_id}")
        print(f"Selected Student Data: {selected_student}")

    def display_students(self):
        ''' This method displays the students in the listbox '''
        # Clear the listbox before adding new items
        self.stulistbox.delete(0, tkinter.END)

        # Add students items to listbox
        for student_obj in self.__student_list:
            # Check if the item is an instance of Student class
            if isinstance(student_obj, stu.Student):
                # Extract necessary information from the student object
                item_string = f"Name:{student_obj.name} ID:{student_obj.id_num} GPA:{student_obj.gpa}"
                # PRINT FOR TESTING
                print(self.__student_list)

                self.stulistbox.insert(tkinter.END, item_string)

        # Bind the select_student method to the listbox
        self.stulistbox.bind('<<ListboxSelect>>', self.select_student)

    def select_student(self, event):
        # Get the selected index
        selected_index = self.stulistbox.curselection()

        if selected_index:
            # Get the selected item from the listbox
            selected_item = self.stulistbox.get(selected_index)
            
            # Extract the student ID from the selected item
            parts = selected_item.split(" ")
            student_id_index = parts.index("ID:") + 1
            self.__selected_student_id = parts[student_id_index]
    
    def load_data(self):
        ''' This method loads data from a file given by the user'''
        # Clear the listbox before adding new data
        self.stulistbox.delete(0, tk.END)
        
        # Ask the user to select a file
        file_path = tkinter.filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", ".*")])
            
        # Check if the user selected a file
        if file_path:
            # Read data from the file
            with open(file_path, "r") as file:
                for line in file:
                    fields = line.strip().split(":")

                    # Check if there are enough fields in the line
                    if len(fields) >= 3:
                        
                        # Extract the necessary information
                        id_num = fields[0]
                        name = fields[1]
                        gpa = fields[2]
                        last_field = fields[-1].split(",")
                        
                        self.add_student_from_file(id_num, name, gpa, last_field)
                    else:
                        # Display an error message
                        tkinter.messagebox.showerror("Error", "Invalid data.")
                        return
                    
    def create_schedule(self):
        ''' This method creates a schedule for the selected student in the listbox in studentSchedule.txt'''
        # Use a specific filename
        file_name = "studentSchedule.txt"
        

        ''' NEEDS TESTING '''
        # Check user selection for font type and set listbox font
        if self.font_weight.get() == ScheduleGUI.BOLD_FONT:
            fontUse = tkinter.font.Font(family = self.font_fam.get(),
                                     weight = "bold")
        else:
            fontUse = tkinter.font.Font(family = self.font_fam.get(),
                                     weight = "normal")
        
        self.stulistbox.config(font = fontUse)


        # Open file
        with open(file_name, "w") as file_var:
            # Write student information to file
            for student_obj in self.__student_list:
                file_var.write(f"Student ID: {student_obj.id_num}      Student Name: {student_obj.name}    Student GPA: {student_obj.gpa}\n")

                # Write each course for the student
                for course in student_obj.courses:
                    file_var.write(f"Course[{course.num}] - {course.name} Credit Hours: {course.crHours}]\n")
                    
        tkinter.messagebox.showinfo("Information", "Schedule written to the file studentSchedule.txt.")
    
    def clear_stuentry(self):
        ''' This method clears the entry fields'''
        # Remove all text from entry fields
        self.entryID.delete(0, tkinter.END)
        self.entryName.delete(0, tkinter.END)
        self.entryGPA.delete(0, tkinter.END)

        # Set the focus to description
        self.entryID.focus()

    def clear_crsentry(self):
        ''' This method clears the entry fields for courses'''
        # Remove all text from entry fields
        self.entryCourseID.delete(0, tkinter.END)
        self.entryCourseName.delete(0, tkinter.END)
        self.entryCrHours.delete(0, tkinter.END)

        # Set the focus to description
        self.entryCourseID.focus()
    
    def save_file(self):
        ''' This method saves the data to a file'''
        # Get filename
        file_name = tkinter.filedialog.asksaveasfilename(initialdir="/",
                                                        filetypes=[("Text files", "*.txt"),
                                                                    ("All files", ".*")],
                                                        title="Select file",
                                                        defaultextension=".txt")
        # Check for empty string
        if len(file_name) != 0:
            # Open file
            with open(file_name, "w") as file_var:
                # Write to file
                for student_obj in self.__student_list:
                    # Extract necessary information from the student object
                    item_string = f"{student_obj.id_num}:{student_obj.name}:{student_obj.gpa}:{','.join(map(str, student_obj.courses))}"

                    file_var.write(item_string + "\n")

            tkinter.messagebox.showinfo("Information", "File saved successfully.")

    def show_about(self):
        tk.messagebox.showinfo("Help", "This is a GUI application designed to create schedule of students.\n\nWritten by: Gabriel dos Reis\n\nDate: 2023")
        
    def exit_app(self):
        ''' This method allows the user to exit the program'''
        response = tkinter.messagebox.askyesno("Confirmation",
                                               "Are you sure you want to exit?")
        if response == True:
            self.main_window.destroy()
    
if __name__ == '__main__':
    ''' Launch the application '''
    launch = ScheduleGUI()