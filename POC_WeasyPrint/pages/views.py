from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML

def generate_pdf(request):
    # Render the HTML template
    template = get_template('my_template.html')
    html = template.render()

    # Create a PDF object using WeasyPrint
    pdf_file = HTML(string=html).write_pdf()

    # Create an HttpResponse object with the PDF file
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="my_pdf_file.pdf"'
    return response