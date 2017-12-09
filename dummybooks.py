from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, BookDB, User
engine = create_engine('sqlite:///BookCatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create user details
User1 = User(name="admin", email="shavgar.haji@gmail.com")
session.add(User1)
session.commit()

# Dummy books catalog
book1 = BookDB(Book_Title="Man's Search for Meaning",
               Author="Viktor E. Frankl	",
               URL="""http://www.fablar.in/yahoo_site_admin/
               assets/docs/Mans_Search_for_Meaning.78114942.pdf""",
               description="talks about men's hope", category="Story", user_id=1)

session.add(book1)
session.commit()

book2 = BookDB(Book_Title="The 48 Laws of Power",
               Author="Robert Greene",
               URL="""https://www.tke.org/files/file/The_48_Laws_of_Power.pdf""",
               description="Great laws to be a leader", category="Self-help", user_id=1)

session.add(book2)
session.commit()

book3 = BookDB(Book_Title="33 War Strategy",
               Author="Robert Greene",
               URL="""https://blackmystory.files.wordpress.com/2014/08/the-33-strategies-of-war.pdf""",
               description="Self and wise Management", category="Self-help", user_id=1)

session.add(book3)
session.commit()

book4 = BookDB(Book_Title="1984",
               Author="George Orwell",
               URL="""http://www.penguin.com/static/pdf/teachersguides/1984.pdf""",
               description="Social Science and Political Fiction", category="Fiction", user_id=1)

session.add(book4)
session.commit()

book5 = BookDB(Book_Title="The Handmaid's Tale",
               Author="Margaret Atwood",
               URL="""http://rockhillib.com/Downloads/eBooks/atwoodthehandmaidstale.pdf""",
               description="Utopian and dystopian fiction", category="Fiction", user_id=1)

session.add(book5)
session.commit()


print ("The Listed Books")
