from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    SSN = Column(Integer)
    phone = Column(String)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    last_updated = Column(DateTime)
    date_of_birth = Column(DateTime)




class TaxCalculation(Base):    
    __tablename__ = "tax_calculation"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    title = Column(String)
    description = Column(String)    # May or may not need
    ordinary_income = Column(DECIMAL(12, 2))
    capital_income = Column(DECIMAL(12, 2))
    federal_deduction = Column(DECIMAL(12, 2))
    taxable_income = Column(DECIMAL(12, 2))
    federal_tax_owed = Column(DECIMAL(12, 2))
    penalty = Column(DECIMAL(12, 2))
    se_tax = Column(DECIMAL(12, 2))
    federal_withholding = Column(DECIMAL(12, 2))
    federal_tax_credit = Column(DECIMAL(12, 2))
    federal_tax_liability = Column(DECIMAL(12, 2))
    total_tax_owed = Column(DECIMAL(12, 2))
    federal_income = Column(DECIMAL(12, 2))
    depreciation_adjustment = Column(DECIMAL(12, 2))
    HSA_adjustment = Column(DECIMAL(12, 2))
    ca_adj_income = Column(DECIMAL(12, 2))
    ca_itemized_deduction = Column(DECIMAL(12, 2))
    ca_taxable_income = Column(DECIMAL(12, 2))
    ca_ira_penalty = Column(DECIMAL(12, 2))
    state_tax_owed = Column(DECIMAL(12, 2))
    state_withholding = Column(DECIMAL(12, 2))
    state_exemption = Column(DECIMAL(12, 2))
    ca_tax_liability = Column(DECIMAL(12, 2))
    self_employment_income = Column(DECIMAL(12, 2))
    equipment_depreciation = Column(DECIMAL(12, 2))
    partnership_income = Column(DECIMAL(12, 2))
    se_tax_deduction = Column(DECIMAL(12, 2))
    se_deduction = Column(DECIMAL(12, 2))
    federal_itemized_deduction = Column(DECIMAL(12, 2))
    state_itemized_deduction = Column(DECIMAL(12, 2))
    w2_income = Column(DECIMAL(12, 2))
    other_income = Column(DECIMAL(12, 2))

    # Define relatipnship
    # user = relationship("User", back_populates="tax_calculation")
    owner = relationship("User")

class TaxForm(Base):
    __tablename__ = "tax_form"
    id = Column(Integer, primary_key=True, index=True)
    formName = Column(Integer, nullable=False)
    formData = Column(String)
    year = Column(Integer, nullable=False)

class Bank(Base):
    __tablename__ = "bank"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    account_number = Column(Integer)
    routing_number = Column(Integer)

class DriverLicense(Base):
    __tablename__ = "driver_license"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    driver_license_expiration = Column(DateTime)
    issue_date = Column(DateTime)

class Payment(Base):
    __tablename__ = "payment"
    id = Column(Integer,primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    amount = Column(Float)
    payment_date=Column(DateTime)    
    payment_status=Column(String)   # Tbh not sure
    description=Column(String)

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    street = Column(String)
    street_number = Column(String)
    unit = Column(String)
    city = Column(String)
    state = Column(String)
    zipcode = Column(Integer)
    address_type = Column(String)


