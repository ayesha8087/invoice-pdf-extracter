import os
import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

os.makedirs("sample_invoices", exist_ok=True)

vendors = ["Alpha Supplies Ltd", "BrightTech Solutions",
           "Green Valley Traders", "Nova Office Mart"]
items = [("Paper A4 Pack", 5.00), ("Printer Ink", 22.50),
         ("Stapler", 8.75), ("Office Chair", 95.00), ("USB Cable", 6.20)]

def make_invoice(n):
    c = canvas.Canvas(f"sample_invoices/invoice_{n}.pdf", pagesize=A4)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 800, random.choice(vendors))
    c.setFont("Helvetica", 11)
    c.drawString(50, 770, f"Invoice Number: INV-{1000 + n}")
    c.drawString(50, 755, f"Date: 2026-{random.randint(1, 9):02d}-{random.randint(10, 28)}")
    c.drawString(50, 740, "Bill To: Sample Customer Co.")

    y = 700
    subtotal = 0
    for name, price in random.sample(items, 3):
        qty = random.randint(1, 5)
        amount = qty * price
        subtotal += amount
        c.drawString(50, y, f"{name}  {qty} x {price:.2f}  =  {amount:.2f}")
        y -= 18

    tax = subtotal * 0.10
    c.drawString(50, y - 20, f"Subtotal: {subtotal:.2f}")
    c.drawString(50, y - 38, f"Tax: {tax:.2f}")
    c.drawString(50, y - 56, f"Total: {subtotal + tax:.2f}")
    c.save()

for i in range(1, 6):
    make_invoice(i)
print("Created 5 sample invoices")