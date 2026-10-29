import re
import pdfplumber

def extract_text(file):
    """Read all text from a PDF (works with a path or an uploaded file)."""
    with pdfplumber.open(file) as pdf:
        return "\n".join(page.extract_text() or "" for page in pdf.pages)

def find(pattern, text):
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else None

def parse_invoice(text):
    lines = [l for l in text.split("\n") if l.strip()]
    data = {
        "vendor": lines[0] if lines else None,
        "invoice_number": find(r"Invoice\s*(?:Number|No\.?|#)\s*[:\-]?\s*([A-Za-z0-9\-]+)", text),
        "date": find(r"\bDate\s*[:\-]?\s*(\d{4}-\d{2}-\d{2}|\d{1,2}[/-]\d{1,2}[/-]\d{2,4})", text),
        "total": find(r"\bTotal\s*[:\-]?\s*[$€£]?\s*([\d,]+\.\d{2})", text),
    }
    missing = [k for k, v in data.items() if not v]
    data["status"] = "OK" if not missing else "Needs review: " + ", ".join(missing)
    return data
if __name__ == "__main__":
    text = extract_text("sample_invoices/invoice_1.pdf")
    print(parse_invoice(text))