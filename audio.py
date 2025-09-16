import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# Open file dialog to select PDF
book = askopenfilename(title="Select PDF File", filetypes=[("PDF files", "*.pdf")])

# Open the PDF
pdfreader = PyPDF2.PdfReader(book)
pages = len(pdfreader.pages)

# Initialize TTS engine once
player = pyttsx3.init()

# Read each page
for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    if text:  # Avoid empty pages
        player.say(text)
        player.runAndWait()
