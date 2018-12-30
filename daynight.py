import ephem, openpyxl
wb = openpyxl.load_workbook('day.xlsx')
sheet = wb.active
bird = ephem.Observer()
sun = ophem.Sun()
sheet.cell(row=1, column=5).value = "longitude"
sheet.cell(row=1, column=6).value = "latitude"
sheet.cell(row=1, column=7).value = "sunrise"
sheet.cell(row=1, column=8).value = "sunset"
sun.compute(bird)
bird.date = "2000/07/31 23:00" 
for t in range(2,xxxx,1):
  bird.date += ephem.hour * 1
