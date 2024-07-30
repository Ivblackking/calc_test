from .models import Coefficient, engine
from sqlalchemy.orm import sessionmaker 

Session = sessionmaker(bind=engine)

session = Session()


async def calculate_pension(data: dict) -> int:
    salary_coeff = session.query(Coefficient).filter_by(name='salary').one()
    retirement_years_coeff = session.query(Coefficient).filter_by(name='retirement years').one()
    base_retirement_years = session.query(Coefficient).filter_by(name='base retirement years').one()
    gender_coef = session.query(Coefficient).filter_by(name=data['gender']).one()
    category_coef = session.query(Coefficient).filter_by(name=data['category']).one()

    if int(data['retirement_years']) < base_retirement_years.value:
        return 0

    pension = int(
        int(data['salary'])*
        int(data['experience'])*
        salary_coeff.value*
        retirement_years_coeff.value**(int(data['retirement_years'])-base_retirement_years.value)*
        gender_coef.value*
        category_coef.value
    )

    return pension