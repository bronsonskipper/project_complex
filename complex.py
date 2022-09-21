"""
    -- project_complex -- 
        Author: Bronson Skipper
    visualisation of the cartesian co-ordinates 
    information generation of both polar and rectangular form.

    This program is fundementally built to help me with my up
    coming calculus exams understanding important concepts behind
    complex numbers. 

    An import module used in this program is matplotlib as it provides
    the ability to easily impelement a polar graph.
    installation 
    pip3 install matplotlib
"""

import cmath
import math
import random
import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class complex_interface:
    def __init__(self, master):
        # GUI main window setup
        self.master = master
        master.title("Complex Polar Coordinates")
        master.resizable(0, 0)

        # ---------- ClASS variables ----------
        self.all_complex_equations = []
        self.complex_equation = tk.StringVar()

        # String variables displayed in description
        # Rectangular description variables
        self.current_equation = tk.StringVar()
        self.rectangle_description_text = tk.StringVar()
        self.real_part = tk.StringVar()
        self.complex_part = tk.StringVar()

        self.polar_form = tk.StringVar()
        self.mod = tk.StringVar()
        self.angle = tk.StringVar()

        # standard configuration
        self.rectangle_description_text.set("format: a + bi")
        self.real_part.set("Real part: ")
        self.complex_part.set("Complex part: ")

        self.mod.set("magnitude: ")
        self.angle.set("angle: ")

        # -------------------- FRAMES --------------------
        # Polar coordinates frame
        self.polar_graph_frame = tk.Frame(master)
        self.polar_graph_frame.pack(side=tk.RIGHT)

        # Coordinate graph created and placed in polar_graph_frame
        self.create_polar_coordinate()

        # User input frame
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(side=tk.LEFT)

        # -------------------- All attributes in user input frame --------------------
        # Input Label this is the overall heading for the input frame
        self.complex_title = tk.Label(
            self.input_frame,
            font=("arial", 16, "bold"),
            text="Graphing Polar Coordinates",
            width=44,
            height=2,
            bg="CadetBlue2",
            anchor=tk.CENTER,
            justify=tk.RIGHT,
        )
        self.complex_title.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)

        # ========== All attributes in rectangle form input frame ===========
        self.single_rectangle_input_frame = tk.Frame(
            self.input_frame, bg="white smoke", highlightthickness=1
        )
        self.single_rectangle_input_frame.grid(
            row=1, column=0, columnspan=2, pady=2, sticky=tk.NSEW
        )

        # Label to display singular rectangle form input and discription label
        self.single_rectangle_label = tk.Label(
            self.single_rectangle_input_frame,
            font=("arial", 15, "italic"),
            text="Rectangular form notation",
            bg="white smoke",
        )
        self.single_rectangle_label.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)

        self.rectangle_label_description = tk.Label(
            self.single_rectangle_input_frame,
            textvariable=self.rectangle_description_text,
            bg="white smoke",
        )
        self.rectangle_label_description.grid(row=1, column=0, columnspan=2)

        # Entry field for complex equation in rectangular form
        self.complex_equation_input = tk.Entry(
            self.single_rectangle_input_frame,
            width=20,
            textvariable=self.complex_equation,
        )
        self.complex_equation_input.grid(row=2, column=0, padx=5, pady=2)

        # Button to graph the real, complex relationship on the
        # cartesian plane.
        self.graph_button = tk.Button(
            self.single_rectangle_input_frame,
            width=20,
            height=2,
            text="Visualise Equation",
            command=self.visualise_equation,
        )
        self.graph_button.grid(row=2, column=1, sticky=tk.NSEW, padx=0, pady=5)
        # ===================================================================

        # ========== All attributes in complex description frame ===========
        self.complex_description_frame = tk.Frame(
            self.input_frame, bg="white smoke", highlightthickness=1
        )
        self.complex_description_frame.grid(
            row=2, column=0, columnspan=2, pady=2, sticky=tk.NSEW
        )

        # Label to display complex description
        self.equation_description_label = tk.Label(
            self.complex_description_frame,
            font=("arial", 15, "italic"),
            text="Complex description",
            bg="white smoke",
        )
        self.equation_description_label.grid(
            row=0, column=0, columnspan=2, sticky=tk.NSEW
        )

        # ----- complex descriptions -----
        # Rectangular from
        self.rectangular_from_label = tk.Label(
            self.complex_description_frame, text="Rectangular from: ", bg="white smoke"
        )
        self.rectangular_from_label.grid(row=1, column=0, sticky=tk.NSEW)

        # Current rectangular equation
        self.current_rectangular_from = tk.Label(
            self.complex_description_frame,
            width=28,
            height=2,
            textvariable=self.current_equation,
            bg="White smoke",
        )
        self.current_rectangular_from.grid(row=1, column=1, sticky=tk.NSEW)

        # Real and imaginary components labels
        self.real_component_label = tk.Label(
            self.complex_description_frame,
            width=20,
            height=2,
            textvariable=self.real_part,
            bg="white smoke",
        )
        self.real_component_label.grid(row=2, column=0)

        self.complex_component_label = tk.Label(
            self.complex_description_frame,
            width=20,
            height=2,
            textvariable=self.complex_part,
            bg="white smoke",
        )
        self.complex_component_label.grid(row=2, column=1)

        # Polar form and magnitude, angle
        # Polar form label and equation label
        self.polar_form_label = tk.Label(
            self.complex_description_frame, text="Polar from: ", bg="white smoke"
        )
        self.polar_form_label.grid(row=3, column=0, sticky=tk.NSEW)

        self.polar_form_equation = tk.Label(
            self.complex_description_frame,
            width=28,
            height=2,
            textvariable=self.polar_form,
            bg="White smoke",
        )
        self.polar_form_equation.grid(row=3, column=1, sticky=tk.NSEW)

        # Polar magnitude and angle
        self.magnitude_label = tk.Label(
            self.complex_description_frame,
            width=20,
            height=2,
            textvariable=self.mod,
            bg="white smoke",
        )
        self.magnitude_label.grid(row=4, column=0)

        self.angle_label = tk.Label(
            self.complex_description_frame,
            width=20,
            height=2,
            textvariable=self.angle,
            bg="white smoke",
        )
        self.angle_label.grid(row=4, column=1)

        # ===================================================================

        # Clears the graph
        self.clear_graph_button = tk.Button(
            self.input_frame,
            width=20,
            height=3,
            text="Clear Graph",
            command=self.clear_graph,
        )
        self.clear_graph_button.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW)

    def create_polar_coordinate(self):
        """Create polar graph with motplotlib"""
        self.figure = plt.Figure(figsize=(5, 5), dpi=78)
        self.ax = self.figure.add_subplot(111, projection="polar")

        self.polar = FigureCanvasTkAgg(self.figure, self.polar_graph_frame)
        self.polar.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        self.ax.set_title("Polar Coordinates")

    def coordinate_graph(self):
        """Clear and plot the polar graph"""
        self.ax.clear()
        self.ax.set_title("Polar Coordinates")
        for x in self.all_complex_equations:
            self.ax.plot([0, cmath.phase(x)], [0, abs(x)], marker="o")
        self.polar.draw()

    def visualise_equation(self):
        """Identifies if the given equation is valid with the method 
        complex_part_identification, calls methods to graph and display
        the complex equation as well as complex_description_generation
        or display error notification
        """
        self.equation = self.complex_part_identification(self.complex_equation.get())

        if self.equation:
            # If the returned identification is a real complex equation
            self.rectangle_description_text.set("format: a + bi")
            self.all_complex_equations.append(self.equation)
            self.coordinate_graph()

            # Updates equation variables, and description frame
            # Operator to display the if imag part is positive or negative
            operator = "+" if self.equation.imag > 0 else ""
            self.current_equation.set(
                f"{self.equation.real:2.4}{operator}{self.equation.imag:2.4}i"
            )
            self.complex_description_generation()

            self.complex_equation.set("")
        else:
            # Incorrect complex equation notification
            rand_real, rand_imag = random.randint(-50, 50), random.randint(-50, 50)
            operator = "+" if rand_imag > 0 else ""
            self.rectangle_description_text.set(
                f"Invalid rectangular form. example: {rand_real}{operator}{rand_imag}i"
            )

        print(self.all_complex_equations)

    def clear_graph(self):
        """Clears all current variables and StringVariables"""
        # Clears list of equations and displayed StrVariables
        self.all_complex_equations = []
        self.coordinate_graph()

        self.complex_equation.set("")
        self.current_equation.set("")
        self.polar_form.set("")

        self.rectangle_description_text.set("format: a + bi")
        self.real_part.set("Real part: ")
        self.complex_part.set("Complex part: ")

        self.mod.set("magnitude: ")
        self.angle.set("angle: ")

        # Notifying the terminal
        print(self.all_complex_equations)

    def complex_description_generation(self):
        """A function to assign the correct variables in the complex 
        description frame
        """
        self.real_part.set(f"Real part: {self.equation.real:2.4}")
        self.complex_part.set(f"Complex part: {self.equation.imag:2.4}")

        self.polar_form.set(
            f"{abs(self.equation):2.4} ∠ {math.degrees(cmath.phase(self.equation)):2.4}˚"
        )
        self.mod.set(f"magnitude: {abs(self.equation):2.4}")
        self.angle.set(f"angle: {math.degrees(cmath.phase(self.equation)):2.4}˚")

    def complex_part_identification(self, equation):
        """To evaluate a complex equation"""
        # Formating the string with no white space and complex notation
        # of "j" instead of "i" for complex implementation with cmath
        equation = equation.lower()
        equation = equation.replace(" ", "")
        equation = equation.replace("i", "j")

        try:
            return complex(equation)
        except:
            # Any error Attribute, Value
            # The equation is not a valid complex number
            return False


if __name__ == "__main__":
    root = tk.Tk()
    complex_interface(root)
    root.mainloop()
