# Import the Tkinter library for GUI
import tkinter as tk

# Import the custom Tkinter library for enhanced widgets
import customtkinter as ctk  

# Import PyTorch for handling tensors and model
import torch  

# Import the Stable Diffusion Pipeline from diffusers library
from diffusers import StableDiffusionPipeline 

# Import PIL for image handling
from PIL import ImageTk 

# Import the authentication token from a file
from authtoken import auth_token  


# Initialize the main Tkinter application window
app = tk.Tk()

# Set the size of the window
app.geometry("532x632") 

# Set the title of the window
app.title("Text-to-Image Generator")  

# Set the appearance mode of customtkinter to dark
ctk.set_appearance_mode("dark")  

# Create an entry widget for the prompt text input
prompt = ctk.CTkEntry(master=app, height=40, width=512, font=("Arial", 20), text_color="black", fg_color="white")

# Place the entry widget at coordinates (10, 10)
prompt.place(x=10, y=10)  

# Create a label widget for displaying the generated image
lmain = ctk.CTkLabel(master=app, height=512, width=512)

# Place the label widget at coordinates (10, 110)
lmain.place(x=10, y=110)  

# Define the model ID for Stable Diffusion
modelid = "CompVis/stable-diffusion-v1-4"  

# Define the device to run the model on
device = "cpu" 

# Load the Stable Diffusion model pipeline
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float32, use_auth_token=auth_token)

# Move the pipeline to the specified device (CPU)
pipe.to(device)  

# Define the function to generate the image from the prompt
def generate():

    # Disable gradient calculation for efficiency
    with torch.no_grad():  
        
        # Generate the image with guidance scale
        output = pipe(prompt.get(), guidance_scale=8.5)

    image = output.images[0]
    # Before converting, check the mode of the image (should be "RGB")
    print(image.mode)  

    # Ensure the image is in RGB format (sometimes PIL converts it to grayscale)
    if image.mode != "RGB":
        image = image.convert("RGB")

    # # Convert the image to a PhotoImage for Tkinter
    # img = ImageTk.PhotoImage(image)
    
    # we are using CTKImage instead of ImageTk.PhotoImage to scaled on HighDPI displays
    # Convert the generated image (PIL Image) to a format compatible with CTkImage    
    img = ctk.CTkImage(light_image=image, size=(512, 512))  # Adjust the size if necessary

    # Keep a reference to the image to prevent garbage collection
    lmain.image = img 

    # Update the label widget with the new image
    lmain.configure(image=img, text="By - Vikas")  

# Create a button widget to trigger the image generation
trigger = ctk.CTkButton(master=app, height=40, width=120, font=("Arial", 20), text_color="white", fg_color="black", command=generate)

# Set the text on the button to "Generate"
trigger.configure(text="Generate")  

# Place the button at coordinates (206, 60)
trigger.place(x=206, y=60)  

# Start the Tkinter main loop
app.mainloop()