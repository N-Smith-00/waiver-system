from fpdf import FPDF

spc = 6

def create_confirmation_adult(data):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    pdf.set_font("Arial", "B", 18)
    pdf.cell(200, spc*2, "Participant Info")
    pdf.ln()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, spc, f'Name: {data["fname"]} {data["lname"]}')
    pdf.ln()
    pdf.cell(200, spc, f'Date of Birth: {data["dob"]}')
    pdf.ln()
    pdf.cell(200, spc, f'Email: {data["email"]}')
    pdf.ln()
    pdf.cell(200, spc, f'Phone Number: {data["phone_num"]}')
    pdf.ln(spc*2)

    pdf.set_font("Arial", "B", 18)
    pdf.cell(200, spc*2, "Emergency Contact")
    pdf.ln()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, spc, f'Name: {data["ec_fname"]} {data["ec_lname"]}')
    pdf.ln()
    pdf.cell(200, spc, f'Phone Number: {data["ec_phone_num"]}')
    pdf.ln()
    pdf.cell(200, spc, f'Emergency Contact Relationship: {data["ec_relation"]}')

    pdf.output("confirmation.pdf")