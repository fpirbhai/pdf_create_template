from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)

    pdf.set_text_color(0,110,0)
    pdf.cell(w=0, h=24, txt= row['Topic'], border=0, ln=1)

    pdf.set_draw_color(0,110,0)
    pdf.line(x1=10, y1=27, x2= 200, y2=27)

    pdf.set_draw_color(0,0,0)
    pdf.ln(5)

    for line in range(16):
        pdf.cell(w=0, h=15, txt= '', border='T', ln=1)

    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(110,110,110)
    pdf.cell(w=0, h=10, txt= row['Topic'], border=0, ln=1, align='R')

    for pg in range(row['Pages']):
        pdf.add_page()    

        for line in range(18):
            pdf.cell(w=0, h=15, txt= '', border='T', ln=1)

        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(110,110,110)
        pdf.cell(w=0, h=10, txt= row['Topic'], border=0, ln=1, align='R')

    # pdf.cell(w=0, h=24, txt= row['Topic'], border=1, ln=1)



pdf.output("output.pdf")    