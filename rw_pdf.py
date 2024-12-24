import PyPDF2

# C:\\Users\\asinha37\\AviRepo\\Python\\python-exercises\\python-exercies\\resources\\Working_Business_Proposal.pdf

with open('C:\\Users\\asinha37\\AviRepo\\Python\\python-exercises\\python-exercies\\resources\\Working_Business_Proposal.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[0] # reading the first page
    print(page.extract_text())
    with open('C:\\Users\\asinha37\\AviRepo\\Python\\python-exercises\\python-exercies\\resources\\Working_Business_Proposal_Page1.pdf', 'ab') as pdf_file:
        writer = PyPDF2.PdfWriter()
        writer.add_page(page)
        writer.write(pdf_file)
        # pdf_file.close()
        # file.close()