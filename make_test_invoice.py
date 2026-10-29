from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

c = canvas.Canvas("sample_invoices/invoice_test_no55.pdf", pagesize=A4)
c.setFont("Helvetica-Bold", 18)
c.drawString(50, 800, "Test Vendor Co")
c.setFont("Helvetica", 11)
c.drawString(50, 770, "Invoice No: 55")
c.drawString(50, 755, "Date: 2026-10-27")
c.drawString(50, 740, "Bill To: Sample Customer Co.")
c.drawString(50, 700, "Stapler  2 x 8.75  =  17.50")
c.drawString(50, 660, "Subtotal: 17.50")
c.drawString(50, 642, "Tax: 1.75")
c.drawString(50, 624, "Total: 19.25")
c.save()
print("Created invoice_test_no55.pdf")