"Imprimir la fecha y hora actuales."
import datetime 
from time import localtime
from time import timezone
from time import tzname
local = datetime.date.today()
ahora_0 = timezone
ahora = tzname
ahora_2 = datetime.datetime.utcnow()
print(ahora_2)
#print(local)
fecha = localtime()
#print (fecha)
year = fecha.tm_year
month = fecha.tm_mon
day = fecha.tm_mday
fe=(year, month,day)
#hora = datetime.date.ctime()
dia_del_anio = fecha.tm_yday
#print("la fecha es ", day,"-", month,"-", year, " y el dia del año es ", dia_del_anio)