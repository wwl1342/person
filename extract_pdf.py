import PyPDF2

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error extracting text: {e}")
        return ""

if __name__ == "__main__":
    pdf_path = "我的简历20240625.pdf"
    text = extract_text_from_pdf(pdf_path)
    print("Extracted text:")
    print(text)
