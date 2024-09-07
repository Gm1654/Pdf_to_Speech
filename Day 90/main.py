from PyPDF2 import PdfReader
from gtts import gTTS

def get_text_from_pdf(pdf_path):
    full_text = ''
    pdf_file = open(pdf_path, 'rb')
    read_pdf = PdfReader(pdf_file)
    no_of_pages = len(read_pdf.pages)
    print(no_of_pages)
    for i in range(0,no_of_pages):
        page = read_pdf.pages[i]
        page_content = page.extract_text()
        full_text += page_content
    print(full_text)
    return full_text

def get_audio_from_text(text):
    tts = gTTS(text=text, lang='en', tld='co.in')
    tts.save("audio.mp3")

if __name__ == "__main__":
    pdf_path = '9 proposal hooks.pdf'
    text = get_text_from_pdf(pdf_path)
    get_audio_from_text(text)
