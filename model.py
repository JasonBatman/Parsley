from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref


ENGINE = None
Session = None

engine = create_engine("sqlite:///paprika.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                      autocommit = False,
                                      autoflush = False))

Base = declarative_base()
Base.query = session.query_property()


ENGINE= None
Session= None
Base = declarative_base()

class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True)
    age = Column(String(64), nullable=True)
    gender = Column(String(64), nullable=True)
    occupation =  Column(String(64), nullable=True)
    zip = Column(String(64), nullable=True)
    email = Column(String(64), nullable=True)
    password = Column(String(256), nullable=True)
    timestamp = Column(Integer, nullable=True)

    # make a quick form to get additional user demo info for machine learning
    age = Column(Integer, nullable=True)
    zipcode =  Column(String(15), nullable= True) 

    # rest = models.Restaurant()
    # rest.name = "Bob's"

    # factual_to_rest():
    #     for key (fact_resp):
    #         if key == ""
    #         switch statement

class Restaurant(Base):
    __tablename__="restaurants"

    id = Column(Integer, primary_key=True) #autoincrement
    name = Column(String(64), nullable=True)
    address = Column(String(64), nullable=True) 
    address_extended =  Column(String(128), nullable=True) 
    attire = Column(String(64), nullable=True) 
    attire = Column(String(64), nullable=True) 
    attire_prohibited = Column(String(64), nullable=True) 
    attire_required = Column(String(64), nullable=True) 
    chain_id = Column(String(64), nullable=True) 
    chain_name = Column(String(64), nullable=True) 
    country = Column(String(64), nullable=True) 
    email = Column(String(64), nullable=True) 
    factual_id = Column(String(128), nullable=True) 
    fax = Column(Integer, nullable=True)
    founded = Column(String(64), nullable=True)
    hours = Column(String(64), nullable=True) 
    hours_display = Column(String(64), nullable=True) 
    latitude =  Column(Float(Precision=64), nullable=True)
    locality = Column(String(64), nullable=True) 
    longitude = Column(Float(Precision=64), nullable=True)
    owner  = Column(String(64), nullable=True)
    po_box = Column(Integer, nullable=True)
    postcode = Column(Integer, nullable=True)
    price = Column(Integer, nullable=True)
    rating = Column(Float(Precision=64), nullable=True)
    region =  Column(String(64), nullable=True)  
    tel = Column(String(64), nullable=True)  
    website = Column(String(64), nullable=True)  
    timestamp = Column(Integer, nullable=True)
    #look at notes for list of strings to deal with
 
class Restaurant_Features(Base):
    __tablename__="restaurant_features"   
    #name and factual_id to join 
    id = Column (Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id')) #because each should be unique
    factual_id = Column(String(128), nullable=True) 
    #these are all booleans
    accessible_wheelchair= Column(Boolean, unique=False, default=False)
    alcohol_byob = Column(Boolean, unique=False, default=False)
    alcohol_bar = Column(Boolean, unique=False, default=False)
    alcohol_beer_wine = Column(Boolean, unique=False, default=False)
    alcohol = Column(Boolean, unique=False, default=False)
    groups_goodfor=  Column(Boolean, unique=False, default=False)
    kids_goodfor=  Column(Boolean, unique=False, default=False)
    kids_menu =  Column(Boolean, unique=False, default=False)
    meal_breakfast=  Column(Boolean, unique=False, default=False)
    meal_cater=  Column(Boolean, unique=False, default=False)
    meal_deliver=  Column(Boolean, unique=False, default=False)
    meal_dinner=  Column(Boolean, unique=False, default=False)
    meal_lunch =  Column(Boolean, unique=False, default=False)
    meal_takeout=  Column(Boolean, unique=False, default=False)
    open_24hrs=  Column(Boolean, unique=False, default=False)
    options_glutenfree  =  Column(Boolean, unique=False, default=False)
    options_lowfat  =  Column(Boolean, unique=False, default=False)
    options_organic =  Column(Boolean, unique=False, default=False)
    options_healthy=  Column(Boolean, unique=False, default=False)
    options_vegan=  Column(Boolean, unique=False, default=False)
    options_vegetarian=  Column(Boolean, unique=False, default=False)
    parking = Column(Boolean, unique=False, default=False)
    parking_free =  Column(Boolean, unique=False, default=False)
    parking_garage =  Column(Boolean, unique=False, default=False)
    parking_lot=  Column(Boolean, unique=False, default=False)
    parking_street=  Column(Boolean, unique=False, default=False)
    parking_valet=  Column(Boolean, unique=False, default=False)
    parking_validated =  Column(Boolean, unique=False, default=False)
    payment_cashonly=  Column(Boolean, unique=False, default=False)
    reservations =   Column(Boolean, unique=False, default=False)
    room_private=  Column(Boolean, unique=False, default=False)
    seating_outdoor=  Column(Boolean, unique=False, default=False)
    smoking=  Column(Boolean, unique=False, default=False)
    wifi= Column(Boolean, unique=False, default=False)
    reservations = Column(Boolean, unique=False, default=False)
    timestamp = Column(Integer, nullable=True)

    restaurant = relationship("Restaurant", backref=backref("restaurant_features", order_by=restaurant_id))
    #the point of this table is to start storing values to figure out how often a user wants these 


class Restaurant_Category(Base):
    __tablename__="restaurant_categories"
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    category = Column(String(128), nullable=True)

class Restaurant_Neighborhood(Base):
    __tablename__="restaurant_neighborhoods"
    id = Column(Integer, primary_key=True)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    neighborhood = Column(String(128), nullable=True)
    
    
class User_Preference(Base):
    __tablename__="user_preferences"

    id = Column (Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id')) #because each should be unique
    accessible_wheelchair= Column(String(64), nullable=True)
    alcohol_byob = Column(String(64), nullable=True)
    alcohol_bar = Column(String(64), nullable=True)
    alcohol_beer_wine = Column(String(64), nullable=True)
    alcohol= Column(String(64), nullable=True) 
    groups_goodfor= Column(String(64), nullable=True) 
    kids_goodfor= Column(String(64), nullable=True) 
    kids_menu = Column(String(64), nullable=True) 
    meal_breakfast= Column(String(64), nullable=True)    
    meal_cater= Column(String(64), nullable=True) 
    meal_deliver= Column(String(64), nullable=True) 
    meal_dinner= Column(String(64), nullable=True) 
    meal_lunch = Column(String(64), nullable=True)
    meal_takeout= Column(String(64), nullable=True)
    open_24hrs= Column(String(64), nullable=True)
    options_glutenfree  = Column(String(64), nullable=True)
    options_lowfat  = Column(String(64), nullable=True)
    options_organic = Column(String(64), nullable=True)
    options_healthy= Column(String(64), nullable=True) 
    options_vegan= Column(String(64), nullable=True) 
    options_vegetarian= Column(String(64), nullable=True)
    parking = Column(String(64), nullable=True)
    parking_free = Column(String(64), nullable=True)
    parking_garage = Column(String(64), nullable=True)
    parking_lot= Column(String(64), nullable=True) 
    parking_street= Column(String(64), nullable=True)
    parking_valet= Column(String(64), nullable=True) 
    parking_validated = Column(String(64), nullable=True) 
    payment_cashonly= Column(String(64), nullable=True)
    reservations =  Column(String(64), nullable=True)
    room_private= Column(String(64), nullable=True) 
    seating_outdoor= Column(String(64), nullable=True) 
    smoking= Column(String(64), nullable=True) 
    wifi= Column(String(64), nullable=True)
    reservations = Column(String(64), nullable=True)
    timestamp = Column(Integer, nullable=True)

    user = relationship("User", backref=backref("user_preferences", order_by=user_id))

class User_Restaurant_Rating(Base):
    __tablename__="user_restaurant_ratings"
    # this table will basically say users like the first three restaurants they type in
    #it will also store feedback on suggested restaurants for each user
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id')) 
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    rating = Column(Float(Precision=64), nullable=True)

    user = relationship("User", backref=backref("user_restaurant_ratings", order_by=user_id))
    restaurant = relationship("Restaurant", backref=backref("user_restaurant_ratings", order_by=restaurant_id))
    # user_preference = relationship("User_Preference", backref=backref("user_restaurant_ratings", order_by=user_id))


#for Yelp reviews
class Yelp_Review(Base):
    __tablename__="yelp_reviews"
    id = Column(Integer, primary_key=True)
    business_id = Column(String(128), nullable = True)
    stars = Column(Integer, nullable = True)
    user_id = Column(String(128), nullable = True)
    date = Column(String(128), nullable = True)
    votes_funny = Column(String(128), nullable=True)
    votes_useful = Column(String(128), nullable=True)
    votes_cool = Column(String(128), nullable=True)
    timestamp = Column(Integer, nullable=True)
    text = Column(String(3000), nullable = True)


#for Yelp users
class Yelp_User(Base):
    __tablename__="yelp_users"
    id = Column(Integer, primary_key=True)
    user_id = Column(String(128), nullable = True)
    name = Column(String(128), nullable = True)
    review_count = Column(Integer, nullable=True)
    user_id = Column(String(128), nullable = True)
    average_stars = Column(Float(Precision=64), nullable=True)
    votes_funny = Column(Integer, nullable=True)
    votes_useful = Column(Integer, nullable=True)
    votes_cool = Column(Integer, nullable=True)
    friends = Column(String(128), nullable = True)
    elite = Column(String(128), nullable = True)
    yelping_since = Column(String(128), nullable = True)
    compliments = Column(Integer, nullable=True)
    compliment_type = Column(Integer, nullable=True)
    fans = Column(Integer, nullable=True)
    timestamp = Column(Integer, nullable=True)

class Yelp_Business(Base):
    __tablename__="yelp_businesses"
    id = Column(Integer, primary_key=True) #autoincrement
    name = Column(String(64), nullable=True)
    business_id =  Column(String(128), nullable=True) 
    full_address = Column(String(128), nullable=True) 
    city =  Column(String(128), nullable=True) 
    state = Column(String(128), nullable=True) 
    latitude =  Column(Float(Precision=64), nullable=True)
    longitude = Column(Float(Precision=64), nullable=True)
    stars = Column(Float(Precision=64), nullable=True)
    review_count =  Column(Integer, nullable=True)
    is_still_open = Column(Boolean, unique=False, default=False)
    #these are likely to be lists and a problem unless unpacked
    timestamp = Column(Integer, nullable=True)


class Yelp_Business_Category(Base):
    __tablename__="yelp_business_categories"
    id = Column(Integer, primary_key=True)
    yelp_business_id = Column(Integer, ForeignKey('yelp_businesses.business_id'))
    restaurant = Column(String(128), nullable=True)
    food = Column(Boolean, unique=False, default=False)
    restaurant = Column(Boolean, unique=False, default=False)
    nightlife = Column(Boolean, unique=False, default=False)

class Yelp_Restaurant_Category(Base):
    __tablename__="yelp_restaurant_categories"
    id = Column(Integer, primary_key=True)
    yelp_business_id = Column(Integer, ForeignKey('yelp_businesses.business_id'))
    afghan = Column(Boolean, unique=False, default=False)
    african = Column(Boolean, unique=False, default=False)
    american_new = Column(Boolean, unique=False, default=False)
    american_trad = Column(Boolean, unique=False, default=False)
    arabian= Column(Boolean, unique=False, default=False)
    argentine = Column(Boolean, unique=False, default=False)
    armenian = Column(Boolean, unique=False, default=False)
    asian_fusion= Column(Boolean, unique=False, default=False)
    bangladeshi= Column(Boolean, unique=False, default=False)
    barbeque= Column(Boolean, unique=False, default=False)
    basque= Column(Boolean, unique=False, default=False)
    belgian= Column(Boolean, unique=False, default=False)
    brasseries= Column(Boolean, unique=False, default=False)
    brazilian= Column(Boolean, unique=False, default=False)
    breakfast_brunch= Column(Boolean, unique=False, default=False)
    british= Column(Boolean, unique=False, default=False)
    buffet= Column(Boolean, unique=False, default=False)
    burgers= Column(Boolean, unique=False, default=False)
    burmese= Column(Boolean, unique=False, default=False)
    cafe= Column(Boolean, unique=False, default=False)
    cafeteria= Column(Boolean, unique=False, default=False)
    cajun_creole= Column(Boolean, unique=False, default=False)
    cambodian= Column(Boolean, unique=False, default=False)
    caribbean= Column(Boolean, unique=False, default=False)
    catalan= Column(Boolean, unique=False, default=False)
    cheesesteaks= Column(Boolean, unique=False, default=False)
    chicken_wings= Column(Boolean, unique=False, default=False)
    chinese= Column(Boolean, unique=False, default=False)
    comfort_food= Column(Boolean, unique=False, default=False)
    creperies= Column(Boolean, unique=False, default=False)
    cuban= Column(Boolean, unique=False, default=False)
    czech= Column(Boolean, unique=False, default=False)
    delis = Column(Boolean, unique=False, default=False)
    diners= Column(Boolean, unique=False, default=False)
    ethiopian= Column(Boolean, unique=False, default=False)
    fast_food= Column(Boolean, unique=False, default=False)
    filipino= Column(Boolean, unique=False, default=False)
    fish_chips= Column(Boolean, unique=False, default=False)
    food_court= Column(Boolean, unique=False, default=False)
    food_stands= Column(Boolean, unique=False, default=False)
    french= Column(Boolean, unique=False, default=False)
    gastropubs= Column(Boolean, unique=False, default=False)
    german= Column(Boolean, unique=False, default=False)
    gluten_free= Column(Boolean, unique=False, default=False)
    greek= Column(Boolean, unique=False, default=False)
    halal= Column(Boolean, unique=False, default=False)
    hawaiian= Column(Boolean, unique=False, default=False)
    himalayan_nepa= Column(Boolean, unique=False, default=False)
    hot_dogs= Column(Boolean, unique=False, default=False)
    hot_pot= Column(Boolean, unique=False, default=False)
    hungarian= Column(Boolean, unique=False, default=False)
    iberian= Column(Boolean, unique=False, default=False)
    indian= Column(Boolean, unique=False, default=False)
    indonesian= Column(Boolean, unique=False, default=False)
    irish= Column(Boolean, unique=False, default=False)
    italian= Column(Boolean, unique=False, default=False)
    japanese= Column(Boolean, unique=False, default=False)
    korean= Column(Boolean, unique=False, default=False)
    kosher= Column(Boolean, unique=False, default=False)
    laotian= Column(Boolean, unique=False, default=False)
    lat_am= Column(Boolean, unique=False, default=False)
    live_raw= Column(Boolean, unique=False, default=False)
    malaysian= Column(Boolean, unique=False, default=False)
    mediterranean= Column(Boolean, unique=False, default=False)
    mexican= Column(Boolean, unique=False, default=False)
    middle_eastern= Column(Boolean, unique=False, default=False)
    modern_euro= Column(Boolean, unique=False, default=False)
    mongolian= Column(Boolean, unique=False, default=False)
    pakistani= Column(Boolean, unique=False, default=False)
    persian= Column(Boolean, unique=False, default=False)
    peruvian= Column(Boolean, unique=False, default=False)
    pizza= Column(Boolean, unique=False, default=False)
    polish= Column(Boolean, unique=False, default=False)
    portuguese= Column(Boolean, unique=False, default=False)
    russian= Column(Boolean, unique=False, default=False)
    salad= Column(Boolean, unique=False, default=False)
    sandwiches= Column(Boolean, unique=False, default=False)
    scandinavian= Column(Boolean, unique=False, default=False)
    scottish= Column(Boolean, unique=False, default=False)
    seafood= Column(Boolean, unique=False, default=False)
    singaporean= Column(Boolean, unique=False, default=False)
    slovakian= Column(Boolean, unique=False, default=False)
    soul_food= Column(Boolean, unique=False, default=False)
    soup= Column(Boolean, unique=False, default=False)
    southern= Column(Boolean, unique=False, default=False)
    spanish= Column(Boolean, unique=False, default=False)
    steakhouses= Column(Boolean, unique=False, default=False)
    sushi_bars= Column(Boolean, unique=False, default=False)
    taiwanese= Column(Boolean, unique=False, default=False)
    tapas_bars= Column(Boolean, unique=False, default=False)
    tapas_small= Column(Boolean, unique=False, default=False)
    texmex= Column(Boolean, unique=False, default=False)
    thai= Column(Boolean, unique=False, default=False)
    turkish= Column(Boolean, unique=False, default=False)
    ukranian= Column(Boolean, unique=False, default=False)
    vegan = Column(Boolean, unique=False, default=False)
    vegetarian = Column(Boolean, unique=False, default=False)
    vietnamese = Column(Boolean, unique=False, default=False)


class Yelp_Food_Category(Base):
    __tablename__="yelp_food_categories"
    id = Column(Integer, primary_key=True)

        #FOODs
      #Bagels
      # Bakeries
      # Beer, Wine & Spirits
      # Breweries
      # Bubble Tea
      # Butcher
      # CSA
      # Coffee & Tea
      # Convenience Stores
      # Desserts
      # Do-It-Yourself Food
      # Donuts
      # Farmers Market
      # Food Delivery Services
      # Food Trucks
      # Gelato
      # Grocery
      # Ice Cream & Frozen Yogust
      # Internet Cafes
      # Juice Bars & Smoothies
      # Pretzels
      # Shaved Ice
      # Specialty Food
      # Street Vendors
      # Tea Rooms
      # Wineries

class Yelp_Bar_Category(Base):
    __tablename__="yelp_bar_categories"
    id = Column(Integer, primary_key=True)
      # Bars
      # Comedy Clubs
      # Country Dance Halls
      # Dance Clubs
      # Jazz& Blues
      # Karaoke
      # Music Venues
      # Piano Bars
      # Pool Halls
      # tertiary: 
        # Champagne Bars
        # Cocktail Bars
        # Dive Bars
        # Gay Bars
        # Hookah Bars
        # Lounges
        # Pubs
        # Sports Bars
        # Wine Bars
   
class Yelp_Business_Neighborhood(Base):
    __tablename__="yelp_business_neighborhoods"
    id = Column(Integer, primary_key=True)
    yelp_business_id = Column(Integer, ForeignKey('yelp_businesses.business_id'))
    neighborhood = Column(String(128), nullable=True)

    

def connect():
    global ENGINE
    global Session

    ENGINE = create_engine("sqlite:///paprika.db", echo=True)
    Session = sessionmaker(bind=ENGINE)

    return Session()
 

def main():
    Base.metadata.create_all(ENGINE)

if __name__ == "__main__":
    session = connect() 
    main()
