from fpdf import FPDF

#part1
# create FPDF object
# Layout ('P','L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
pdf = FPDF('P', 'mm', 'Letter')

# Add a page
pdf.add_page()

# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
pdf.set_font('helvetica', 'BIU', 16)
pdf.set_text_color(220,50,50)
# Add text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)
# border (0 False; 1 True - add border around cell)
pdf.cell(120, 100, 'Hello World!', ln=True, border=True)

pdf.set_font('times', '', 12)
pdf.cell(80, 10, 'Good Bye World!')

pdf.output('pdf_1.pdf')


#part4
title = '20,000 Leagues Under the Sea'

def header():
    # font
    pdf4.set_font('helvetica', 'B', 15)
    # Calculate width of title and position
    title_w = pdf4.get_string_width(title) + 6
    doc_w = pdf4.w
    pdf4.set_x((doc_w - title_w) / 2)
    # colors of frame, background, and text
    pdf4.set_draw_color(0, 80, 180) # border = blue
    pdf4.set_fill_color(230, 230, 0) # background = yellow
    pdf4.set_text_color(220, 50, 50) # text = red
    # Thickness of frame (border)
    pdf4.set_line_width(1)
    # Title
    pdf4.cell(title_w, 10, title, border=1, ln=1, align='C', fill=1)
    # Line break
    pdf4.ln(10)
# Page footer
def footer():
    # Set position of the footer
    pdf4.set_y(-15)
    # set font
    pdf4.set_font('helvetica', 'I', 8)
    # Set font color grey
    pdf4.set_text_color(169,169,169)
    # Page number
    pdf4.cell(0, 10, f'Page {pdf4.page_no()}', align='C')
# Adding chapter title to start of each chapter
def chapter_title(ch_num, ch_title, link):
    # Set link location
    pdf4.set_link(link)
    # set font
    pdf4.set_font('helvetica', '', 12)
    # background color
    pdf4.set_fill_color(200, 220, 255)
    # Chapter title
    chapter_title = f'Chapter {ch_num} : {ch_title}'
    pdf4.cell(0, 5, chapter_title, ln=1, fill=1)
    # line break
    pdf4.ln()
# Chapter content
def chapter_body(name):
    # read text file
    with open(name, 'rb') as fh:
        txt = fh.read().decode('latin-1')
    # set font
    pdf4.set_font('times', '', 12)
    # insert text
    pdf4.multi_cell(0, 5, txt)
    # line break
    pdf4.ln()
    # end each chapter
    pdf4.set_font('times', 'I', 12)
    pdf4.cell(0, 5, 'END OF CHAPTER')
def print_chapter(ch_num, ch_title, name, link):
    pdf4.add_page()
    pdf4.chapter_title(ch_num, ch_title, link)
    pdf4.chapter_body(name)

# Create a PDF object
pdf4 = FPDF('P', 'mm', 'Letter')

# metadata
pdf4.set_title(title)
pdf4.set_author('Jules Verne')

# Create Links
website = 'http://www.gutenberg.org/cache/epub/164/pg164.txt'
ch1_link = pdf4.add_link()
ch2_link = pdf4.add_link()

# Set auto page break
pdf4.set_auto_page_break(auto = True, margin = 15)

# Add Page
pdf4.add_page()
pdf4.image('background_image.png', x = -0.5, w = pdf4.w + 1)

# Attach Links
pdf4.cell(0, 10, 'Text Source', ln = 1, link = website)
pdf4.cell(0, 10, 'Chapter 1', ln = 1, link = ch1_link)
pdf4.cell(0, 10, 'Chapter 2', ln = 1, link = ch2_link)

pdf4.print_chapter(1, 'A RUNAWAY REEF', 'chp1.txt', ch1_link)
pdf4.print_chapter(2, 'THE PROS AND CONS', 'chp2.txt', ch2_link)

pdf4.output('pdf_4.pdf')