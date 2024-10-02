# Text-to-Image Generator using Stable Diffusion and Tkinter GUI

This project demonstrates how to build a simple Text-to-Image Generator GUI application using the Tkinter library in Python. The application leverages the **Stable Diffusion model** (a state-of-the-art deep learning model for generating images from text) and **CustomTkinter** (a custom-styled version of Tkinter that supports modern UI elements and HiDPI scaling).

By entering a text prompt, the user can generate images using the Stable Diffusion model, and the generated image will be displayed in the app.

## Prerequisites

Before running this code, make sure you have the following libraries installed:

- `torch` (PyTorch)
- `diffusers` (for Stable Diffusion)
- `Pillow` (for handling images)
- `customtkinter` (for enhanced GUI elements)

You can install these libraries via pip:

```bash
pip install torch diffusers pillow customtkinter
```

## Project Structure

- **Text-to-Image Generator App**: A GUI that takes a text input (prompt) from the user and generates an image based on that prompt using the Stable Diffusion model.
- **Libraries and Tools Used**:
  - **Tkinter**: Standard Python library for building graphical user interfaces (GUIs).
  - **CustomTkinter**: An extended version of Tkinter that provides better styling and scaling support, especially for HiDPI displays.
  - **PyTorch**: A machine learning library used to handle tensors and deep learning models.
  - **Diffusers (from Hugging Face)**: A library that provides the Stable Diffusion Pipeline to generate images from text.
  - **PIL (Pillow)**: Used for image handling, manipulation, and conversion within Python.

## Code Explanation

### 1. Importing Required Libraries

```python
import tkinter as tk
import customtkinter as ctk
import torch
from diffusers import StableDiffusionPipeline
from PIL import ImageTk
from authtoken import auth_token
```

- `tkinter` and `customtkinter`: Used to create the graphical user interface.
- `torch`: Used to handle tensors and run the deep learning model (Stable Diffusion).
- `diffusers.StableDiffusionPipeline`: A specific pipeline from the `diffusers` library that allows you to input a text prompt and generate an image using the Stable Diffusion model.
- `Pillow (ImageTk)`: Converts the generated images to a format that Tkinter can use for displaying.
- `auth_token`: Imports the authentication token needed to access the Hugging Face model.

### 2. Initializing the Main Application Window

```python
app = tk.Tk()
app.geometry("532x632")
app.title("Text-to-Image Generator")
ctk.set_appearance_mode("dark")
```

- `app = tk.Tk()` initializes the main window for the Tkinter GUI.
- `app.geometry("532x632")` sets the size of the application window.
- `app.title("Text-to-Image Generator")` sets the window title.
- `ctk.set_appearance_mode("dark")` sets the overall theme of the application to a dark mode.

### 3. Creating Input Widgets and Labels

```python
prompt = ctk.CTkEntry(master=app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")
prompt.place(x=10, y=10)

lmain = ctk.CTkLabel(master=app, height=512, width=512)
lmain.place(x=10, y=110)
```

- `prompt`: This is an input field where users can type the text prompt that describes the image they want to generate.
- `lmain`: A label where the generated image will be displayed after it is created.

### 4. Loading the Stable Diffusion Model

```python
modelid = "CompVis/stable-diffusion-v1-4"
device = "cpu"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float32, use_auth_token=auth_token)
pipe.to(device)
```

- `modelid`: Specifies the model to use from Hugging Face. In this case, it's the "CompVis/stable-diffusion-v1-4" model.
- `device = "cpu"`: The application is set to run on the CPU. You can change this to `"cuda"` if you have a GPU available.
- `pipe`: This loads the Stable Diffusion model pipeline using the pre-trained weights and the provided authentication token.

### 5. Defining the Function to Generate Images

```python
def generate():
    with torch.no_grad():
        output = pipe(prompt.get(), guidance_scale=8.5)

    image = output.images[0]

    # Convert to RGB if needed
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Use CTkImage for HiDPI compatibility
    img = ctk.CTkImage(light_image=image, size=(512, 512))

    # Keep a reference to the image to prevent garbage collection
    lmain.image = img

    # Update the label with the new image and a text label
    lmain.configure(image=img, text="By - Vikas")
```

- `generate()`: The function that generates the image based on the user's text prompt.
- `torch.no_grad()`: Disables gradient calculations to save memory and improve efficiency.
- `output = pipe(prompt.get(), guidance_scale=8.5)`: Passes the user’s prompt to the model pipeline and generates an image. The `guidance_scale` controls how much the text influences the generated image (higher values make the image more aligned with the prompt).
- `image = output.images[0]`: Extracts the generated image.
- `image.convert("RGB")`: Ensures that the image is in RGB mode (not grayscale).
- `ctk.CTkImage()`: Converts the image to a format that is compatible with `CustomTkinter` and supports HiDPI scaling.
- `lmain.configure(image=img, text="By - Vikas")`: Updates the label to display the generated image and a label with the creator's name.

### 6. Creating the Generate Button

```python
trigger = ctk.CTkButton(master=app, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="black", command=generate)
trigger.configure(text="Generate")
trigger.place(x=206, y=60)
```

- `trigger`: A button that the user clicks to trigger the image generation. It is styled using `CustomTkinter` and is linked to the `generate()` function.

### 7. Starting the Application

```python
app.mainloop()
```

- This starts the Tkinter main loop, which keeps the application running and responsive to user inputs.

## Usage

1. **Run the Script**: Run the Python script in your terminal or IDE.
2. **Enter Prompt**: Type a descriptive text in the input field.
3. **Generate**: Click the "Generate" button, and the image based on your text prompt will appear in the window.

## Acknowledgments

This project is based on:

- **Stable Diffusion**: A state-of-the-art model for generating images from text, developed by CompVis.
- **Hugging Face Diffusers**: A library that provides easy access to various diffusion models, including Stable Diffusion.
- **CustomTkinter**: An extension of Tkinter that provides modern widget styling and HiDPI support.

Special thanks to [Hamna Khalil](https://www.linkedin.com/in/hamna-khalil/) for her blog, which greatly helped in implementing this project.

### Summary

This README provides step-by-step guidance for understanding the code, detailing each part of the implementation, from loading the model to creating the GUI elements. It is written with a beginner in mind, explaining the purpose and function of each section of the code.
