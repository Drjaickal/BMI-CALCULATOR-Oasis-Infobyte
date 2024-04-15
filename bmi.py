# Import libraries
from tkinter import Tk, Label, Entry, Button

# Function to calculate BMI
def calculate_bmi():
  """
  This function calculates the Body Mass Index (BMI) based on the user's weight and height.

  It retrieves the weight and height values from the entry fields, converts them to numerical values,
  and calculates the BMI using the formula: BMI = weight (kg) / height (m)^2.

  The function then displays the calculated BMI along with a corresponding message based on the BMI range.
  """
  try:
    # Get weight and height from entry fields
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100  # Convert height from cm to meters

    # Calculate BMI
    bmi = weight / (height * height)

    # Display BMI and message based on range
    bmi_label.config(text=f"Your BMI is: {bmi:.2f}")  # Format BMI to two decimal places
    if bmi < 18.5:
      message_label.config(text="You are underweight.")
    elif bmi < 25:
      message_label.config(text="You are healthy weight.")
    elif bmi < 30:
      message_label.config(text="You are overweight.")
    else:
      message_label.config(text="You are obese.")
  except ValueError:
    # Handle invalid input (non-numeric values)
    bmi_label.config(text="Error: Please enter valid numbers for weight and height.")
    message_label.config(text="")

# Create the main window
window = Tk()
window.title("BMI Calculator")

# Create labels for weight and height
weight_label = Label(window, text="Enter your weight (kg):")
weight_label.pack()

height_label = Label(window, text="Enter your height (cm):")
height_label.pack()

# Create entry fields for weight and height
weight_entry = Entry(window)
weight_entry.pack()

height_entry = Entry(window)
height_entry.pack()

# Create a button to trigger the calculation
calculate_button = Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Create labels to display BMI and message
bmi_label = Label(window, text="Your BMI will be displayed here.")
bmi_label.pack()

message_label = Label(window, text="")
message_label.pack()

# Run the main loop to display the window
window.mainloop()
