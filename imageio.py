from PIL import Image

def read_image(path):
    try:
        with Image.open(path) as img:
            img = img.convert("L") # convert to grayscale
            pixels = list(img.getdata())
            width, height = img.size
            pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
            return pixels
    except Exception as e:
        print(f"Error reading image: {e}")
        return None

def write_image(path, pixels):
    try:
        width = len(pixels[0])
        height = len(pixels)
        img = Image.new("L", (width, height))
        # Flatten the 2D list into 1D
        flat_pixels = [pixel for row in pixels for pixel in row]
        img.putdata(flat_pixels)
        img.save(path)
    except Exception as e:
        print(f"Error writing image: {e}")
