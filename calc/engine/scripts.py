from models import Coefficient, engine, Base
from sqlalchemy.orm import sessionmaker

# Create table 'coefficients'
Base.metadata.create_all(engine)

# Add coefficients
Session = sessionmaker(bind=engine)

session = Session()

coeff1 = Coefficient(name="salary", value=0.01)
coeff2 = Coefficient(name="retirement years", value=1.06)

coeff3 = Coefficient(name="man", value=1.0)
coeff4 = Coefficient(name="woman", value=0.86)

coeff5 = Coefficient(name="default", value=1.0)
coeff6 = Coefficient(name="military", value=2.1)
coeff7 = Coefficient(name="judge", value=1.62)
coeff8 = Coefficient(name="civil_servant", value=1.3)
coeff9 = Coefficient(name="entrepreneur", value=0.52)
coeff10 = Coefficient(name="miner", value=2.6)

coeff11 = Coefficient(name="base retirement years", value=60.0)

coeffs = [coeff1, coeff2, coeff3, coeff4, coeff5, coeff6, coeff7, coeff8, coeff9, coeff10, coeff11]

session.add_all(coeffs)
session.commit()