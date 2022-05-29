import json
with open('prueba2.json') as prueba:
   data=json.load(prueba)
   print(str(data['name']))
   print(str(data['id']))
   print(str(data['id_bycicle']))
   print((data['identification']))
   if(data['status'] ==False):
       print("una cariloca, yo me transformo")
       
data['name']="Ana Milena"
print(str(data['name']))

       