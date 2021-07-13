#from models import GlobalVar

columns = {"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
values = list(columns.keys())
# print(values)

# test = GlobalVar("test", "test", columns)
# test.update()

print("(" + "".join(["'", "', '".join(values), "'"]) + ")")