!pip install randomuser
!pip install pandas

from randomuser import RandomUser
import pandas as pd

r = RandomUser()

some_list = r.generate_users(10)
#print(some_list)
some_list
name = r.get_full_name()

for user in some_list:
    print(user.get_full_name()," " , user.get_email())

#**********************************************************888
from randomuser import RandomUser
import pandas as pd

r = RandomUser()

list = r.generate_users(10)
print(list)

for user in list:
 print(user.get_full_name())
# print(user.get_picture())
# print(user.get_email())

#***************************************************
def get_users():
    users = []

    for user in RandomUser.generate_users(20):
        users.append({"Name":user.get_full_name(), "Gender":user.get_gender(), "City":user.get_city()})
    
    return pd.DataFrame(users)

#get_users()

df1 = pd.DataFrame(get_users())
df1
