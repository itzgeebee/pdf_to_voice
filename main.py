import pdfplumber  # pip install pdfplumber first
from gtts import gTTS

# get file location
file_path = input("Enter correct file pdf file path(make sure you add the extension i.e .pdf)\n")
audio_file_name = input("enter audio file name\n")

with pdfplumber.open(f"{file_path}") as pdf_file:
    pages = pdf_file.pages
    pg = 1
    for page in pages:
        text = page.extract_text()
        print(text)
        print(page)

        language = "en"
        voice = gTTS(text=text, lang=language, slow=False)
        voice.save(f"{audio_file_name}{pg}.mp3")

        pg += 1
