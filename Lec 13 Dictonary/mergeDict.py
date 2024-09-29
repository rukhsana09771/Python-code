d1 = {100:'Sama', 200:'Parveen'}
d2 = {300:'Rukhsana', 400:'Anjum'}
d3 = {500:'Rani', 600:'Yamin'}

# 1st method
d4 = {}
d4.update(d1)
d4.update(d2)
d4.update(d3)
print(d4)

# 2nd method= {**d1, **d2, **d3}
print(d4)