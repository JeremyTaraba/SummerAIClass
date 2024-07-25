import cv2
import pytesseract
from gtts import gTTS
from mtranslate import translate
from PIL import Image


# text = "hola"
# translated_text = translate(text, "en")
# print(translated_text)

# speech = gTTS(text = translated_text, lang = "en", slow = False, tld="com.au")
# speech.save("translated.mp3")


# Load the image using OpenCV
image = cv2.imread("hello.png")

# Perform text detection
text = pytesseract.image_to_string(image)

# Print the detected text
print(text)

# Translate text
translated_text = translate(text, "en")

# Print the translated text
print(translated_text)

# # Convert translated text to audio
# speech = gTTS(text = translated_text, lang = "en", slow = False)
# speech.save("ImageText.mp3")