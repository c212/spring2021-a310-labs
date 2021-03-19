# s1 = "Hello Good afternoon"
#
# s2 = s1[5:]
#
# print(s2)
#
#
# s4 = "Hi there, How are you doing?"
#
# st = s4.split(',')
#
# print(st)
#
# print('asdas' not in s4)
#
# str4 = s1 +" "+ s4
# print(str4)
#
# sl = 'suyash'
#
# print(sl.upper())
#
# print(s4.partition('How'))
#
# String1 = "Brandon"
#
# print(String1.rjust(10))

# Table Printer
'''
tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:
   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose

'''
tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]

print(len(tableData))

def print_table(table):
    col_width = [0] * len(table)
    print(col_width)
    for i in range(0,len(table)):
        for j in table[i]:
            if len(j) > col_width[i]:
                col_width[i] = len(j)
    print(col_width)

    for i in range(0,len(table)):
        for j in range(0, len(table)):
            ans = table[j][i].rjust(col_width[j])
            print(ans, end=' ')
        print()




print_table(tableData)