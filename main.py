from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    flag = 0

    for pg in range(row['Pages']):
        pdf.add_page()

        if flag==0:
            pdf.set_font(family='Times', style="B", size = 24)
            pdf.set_text_color(100,0,100)
            pdf.cell(w=0, h=24, txt= row['Topic'], align='L', border=0, ln=1)

            pdf.set_draw_color(100,0,100)
            pdf.line(x1=10,y1=28,x2=200,y2=28)
            flag = flag + 1  

            pdf.ln(250)
            pdf.set_font(family='Times', style="I", size = 8)
            pdf.set_text_color(100,0,100)
            pdf.cell(w=0, h=8, txt= row['Topic'], align='R', border=0, ln=1)

        
        pdf.ln(272)
        pdf.set_font(family='Times', style="I", size = 8)
        pdf.set_text_color(100,0,100)
        pdf.cell(w=0, h=8, txt= row['Topic'], align='R', border=0, ln=1)



pdf.output("output.pdf")    