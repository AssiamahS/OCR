import pytesseract
import pyautogui
from PIL import Image
import time

# Set up pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Path\To\Tesseract\tesseract.exe'

# Function to perform OCR
def read_text_from_screen(region):
    screenshot = pyautogui.screenshot(region=region)
    text = pytesseract.image_to_string(screenshot)
    return text

# Function to click a button
def click_button(x, y):
    pyautogui.click(x, y)

# Coordinates for the buttons and the areas to read
right_button_coords = (1000, 500)
left_button_coords = (200, 500)
edit_filters_button_coords = (500, 500)
ocr_region = (400, 300, 600, 100)  # Adjust these coordinates as needed

# Function to update filters
def update_filters(lat, lon):
    pyautogui.click(edit_filters_button_coords)
    time.sleep(2)
    pyautogui.typewrite(f'{lat},{lon}', interval=0.1)

# Coordinates for the snake-like pattern
coordinates = [
    ('New York', '40.7128', '-74.0060'),
    # Add more coordinates here
]

# Main loop
def main_loop():
    for city, lat, lon in coordinates:
        while True:
            text = read_text_from_screen(ocr_region)
            if "swiped right" in text:
                click_button(*right_button_coords)
            elif "not voted" in text:
                click_button(*left_button_coords)
            elif "you're all caught up!" in text:
                update_filters(lat, lon)
                break
            time.sleep(1)  # Adjust the delay as needed

if __name__ == '__main__':
    main_loop()
