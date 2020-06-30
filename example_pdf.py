from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

from datetime import datetime 

current_date = str(datetime.date(datetime.now()))

w, h = A4
c = canvas.Canvas("hello_world.pdf", pagesize=A4)
text = c.beginText(50, h - 50)
text.setFont("Times-Bold", 12)
text.textLine("Processed Update on "+current_date)
text.setFont("Times-Roman", 12)
text.textLines("")
text.textLines("\n\n\nHello, world!\nUsing ReportLab and Python!")
c.drawText(text)
c.showPage()
c.save()
