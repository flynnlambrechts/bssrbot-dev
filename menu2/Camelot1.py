#pdf extractor

import camelot


# directory for where menu is
menu = "menu1.pdf"

###tables = camelot.read_pdf(menu, pages='1,2,3,4,5,6,7,8') 
##print(tables)
##
##
##tables.export('menu.csv', f='csv')


for i in range(1,9):
    tables = camelot.read_pdf(menu, pages='%d' %  i)
    try:
        if i % 2: #for even i (pages with dinner)
            

            print(i)
            tables[0].to_csv(str("breakfast_" + str(int(i)-1) + ".csv"))
            tables[1].to_csv(str("lunch_" + str(int(i)-1) + ".csv"))
        else:
            print(i)
            tables[0].to_csv(str("dinner_" + str(int(i)) + ".csv"))
    except IndexError:
        print('NOK')
        
        
        
