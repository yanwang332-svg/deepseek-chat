
import my_fun as mf
print(mf.PI)
print(mf.NAME)
mf.log_separator1()
mf.log_separator2()
mf.log_separator3()

from my_fun import log_separator1,PI, NAME, log_separator2
log_separator1()
log_separator2()
print(PI)
print(NAME)