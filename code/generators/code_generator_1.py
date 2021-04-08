import pilgram

a = ['aden', 'brannan', 'brooklyn', 'clarendon', 'css', 'earlybird', 'gingham', 'hudson', 'inkwell', 'kelvin', 'lark', 'lofi', 'maven', 'mayfair',
     'moon', 'nashville', 'perpetua', 'reyes', 'rise', 'slumber', 'stinson', 'toaster', 'util', 'valencia', 'walden', 'willow', 'xpro2']
a2 = []
a3 = []
for i in range(1, len(a)):
    a2.append(f"'{a[i].capitalize()}'")
    if i % 3 == 0:
        a3.append(a2)
        a2 = []
for i in a3:
    print(f"keyboard.row({', '.join(i)})")
print(f"keyboard.row({', '.join(a2)}, 'Aden')")

l = [['brannan', 'brooklyn', 'clarendon'],
     ['css', 'earlybird', 'gingham'],
     ['hudson', 'inkwell', 'kelvin'],
     ['lark', 'lofi', 'maven'],
     ['mayfair', 'moon', 'nashville'],
     ['perpetua', 'reyes', 'rise'],
     ['slumber', 'stinson', 'toaster'],
     ['util', 'valencia', 'walden'],
     ['willow', 'xpro2', 'aden']]


