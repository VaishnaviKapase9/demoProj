from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 


data = [
    ["Date", ""],
]

pdf = SimpleDocTemplate("receipt.pdf", pagesize = A4)

