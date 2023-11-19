import os
from PyPDF3 import PdfFileWriter, PdfFileReader
from dateutil.parser import parse

class Transaction:
  def __init__(self, vendor, price, currency):
    self.vendor = vendor
    self.price = price
    self.currency = currency

STATEMENT_PAGE = 2
files = os.listdir(".")

def is_a_date(line):
  if ("/" in line):
    try:
      parse(line, fuzzy=False)
      return True
    except ValueError:
      pass
  return False

def line_payment_thx(line):
  return line == "Payment Thank You-Mobile"

for file in files:
  if (".pdf" in file and file[:8].isdigit()):
    f = PdfFileReader(open(file, "rb"))
    print(f"{file} has {f.getNumPages()} pages")

    parse_start = False
    lines = f.getPage(STATEMENT_PAGE).extractText().splitlines()

    i = 0
    line_was_date = False

    while i < len(lines):
      if (parse_start):
        # Seems like it's usually a date followed by "payment thanks"
        if (is_a_date(lines[i])):
          i += 1
          if (line_payment_thx(lines[i])):
            i += 1
          else:
            line_was_date = True
        
        if (line_was_date):
          Transaction()
          price
          print(f"line: {lines[i]}")

      if ("$ Amount" == lines[i]):
        parse_start = True

      i+= 1

    lines = f.getPage(STATEMENT_PAGE + 1).extractText().splitlines()
    # print("\n")
    # print(lines)
    exit()
