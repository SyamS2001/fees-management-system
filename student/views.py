from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas 
from .models import receipt
from io import BytesIO
from django.conf import settings
import os

# Create your views here.
def view_pdf(request):
    # Create a file-like buffer to receive PDF data
    buffer = BytesIO()

    # Create the PDF object, using the buffer as its "file"
    # width, height = 5 * inch, 3 * inch
    # p = canvas.Canvas(buffer, pagesize=(width, height))
    p = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Draw things on the PDF. Here's where ReportLab goes to work
    # Fetch data from the database
    receipts = receipt.objects.all()

    y = height - 80
    for r in receipts:
        if r.logo:
            logo_path = os.path.join(settings.MEDIA_ROOT, r.logo.name)
            p.drawImage(logo_path, 30, y - 60, width=500, height=80)  # Adjust dimensions as necessary
            y -= 80  # Adjust for the height of the logo

        p.drawString(30, y, f"Receipt No: {r.receiptno}")
        y -= 20
        p.drawString(30, y, f"Student Name: {r.studentname.studentname}")
        y -= 20
        p.drawString(30, y, f"Amount : {r.amount}")
        y -= 20
        # p.drawString(30, y, f"Course Duration: {course.courseduration}")
        # y -= 20

        if y < 80:  # Simple pagination
            p.showPage()
            y = height - 80

    # Close the PDF object cleanly, and we're done
    p.showPage()
    p.save()

    # Get the value of the BytesIO buffer and write it to the response
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')


def index_page(request):
	return render(request, 'index.html')