import random
from sqlalchemy import create_engine
engine = create_engine('sqlite:///base2.sqlite', echo=False)


from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
metadata = MetaData()
users_table = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
    Column('User_Text', String),
    Column('Chat_Id', String)
)
metadata.create_all(engine)

class User(object):
    def __init__(self,name, fullname, user_text, chat_id):
        self.name = name
        self.fullname = fullname
        self.user_text = user_text
        self.chat_id = chat_id

    def __repr__(self):
        return "!User({0}, {1}, {2}, {3})!".format(self.name, self.fullname,self.user_text,self.chat_id)

def add_user(*args):
   user = User(*args)
   session.add(user)
   session.commit()


from sqlalchemy.orm import mapper
mapper(User, users_table)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# user = User ('Vasya', 'Pupkin', '123')
# session.add(user)
# session.commit()
# user = User ('Valya', 'Pupkina', '124')
# session.add(user)
# session.commit()
# user = User ('Sergey', 'Arhipov', '143')
# session.add(user)
# session.commit()


# for i in range (11,20):
#     user1 = User("petya"+str(i), "Pupkin", "ppp"+str(random.randit(100,200)))
#     session.add(user1)
#session.commit



# vasiaUser = User("vasia2", "Vasiliy Pypkin", "vasia2000")
# session.add(vasiaUser)
# session.commit()
#print(vasiaUser.password)
#&&&&&&&&&&&&&
# res = session.query(User).filter(User.name.in_(["Pupkina", "Arhipov"])).all()
# res2 = session.query(User).filter(User.fullname=="Pupkina", "Arhipov").all()
# print(res)
# print(res2)
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# res = session.query(User).filter(User.fullname.like('%3')).all()
# res = session.query(User).get(1)
# res = session.query(User).filter(User.id==1).first()
# res = session.query(User).get(3)
#res = session.query(Usr).all()
#for user in res^
#   if user.name == 'petya17':
#        user.fullname = "ivanov"
#session.commit
#
# for i in res:
#     i.name += "-"
#
#     if i.fullname.endswith('4'):
#         session.delete(i)
#     session.commit()
# print(res)
# # print(res.password)
# # res.password = '34551'
# res.fullname = "Федя1"
# print(res)
# res.name = "Федя2"
# print(res)
# session.rollback()
# res = session.query(User).get(1)
# print(res)