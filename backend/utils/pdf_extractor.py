import pdfplumber
import pytesseract
from PIL import Image
import io




def extract_text(file_path: str) -> str:
    text = ""

    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"

        if not text.strip():
            print("No text found, switching to OCR")

            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    image = page.to_image(resolution=300).original

                    if not isinstance(image, Image.Image):
                        image = Image.open(io.BytesIO(image))

                    ocr_text = pytesseract.image_to_string(image)
                    text += ocr_text + "\n"

    except Exception as e:
        print("PDF Extraction Error:", str(e))

    return text.strip()