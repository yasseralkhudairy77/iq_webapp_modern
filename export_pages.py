# Export PDF pages to images (PNG)
# pip install pymupdf
import fitz, os

PDF_FILE = "soal.pdf"
OUT_DIR = "pages"
ZOOM = 2

os.makedirs(OUT_DIR, exist_ok=True)
doc = fitz.open(PDF_FILE)
mat = fitz.Matrix(ZOOM, ZOOM)

for i in range(len(doc)):
    pix = doc[i].get_pixmap(matrix=mat, alpha=False)
    pix.save(os.path.join(OUT_DIR, f"page-{i+1}.png"))

print("Done:", len(doc), "pages exported to", OUT_DIR)
