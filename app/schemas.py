from typing import List, Optional
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from decimal import Decimal

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    SSN: Optional[str] = None
    phone: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[str] = None

    class Config:
        orm_mode = True
    
class UserUpdate(BaseModel):
    SSN: Optional[str] = None
    phone: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[str] = None

    class Config:
        orm_mode = True

class taxCalcBase(BaseModel):
    title: str
    description: str

class taxCalcCreate(taxCalcBase):
    pass

class taxCalc(taxCalcBase):
    id: int
    owner_id: int
    owner: User #User or UserOut?(gottta create)
    created_at: datetime
    
    class Config:
        orm_mode = True

class taxCalcUpdate(BaseModel):

    self_employment_income: Decimal = Field(0, alias="selfEmploymentIncome")
    equipment_depreciation: Decimal = Field(0, alias="equipmentDepreciation")
    partnership_income: Decimal = Field(0, alias="partnershipIncome")
    se_tax_deduction: Decimal = Field(0, alias="seTaxDeduction")
    se_deduction: Decimal = Field(0, alias="seDeduction")
    federal_itemized_deduction: Decimal = Field(0, alias="federalItemizedDeduction")
    state_itemized_deduction: Decimal = Field(0, alias="stateItemizedDeduction")
    w2_income: Decimal = Field(0, alias="w2Income")
    other_income: Decimal = Field(0, alias="otherIncome")

    class Config:
        orm_mode = True
        
class FederalTaxCalculation(BaseModel):
    fed_ord_inc: Decimal = Field(0, alias="Fed_Ord_Inc")
    fed_cap_inc: Decimal = Field(0, alias="Fed_Cap_Inc")
    fed_adj: Decimal = Field(0, alias="Fed_Adj")
    fed_agi: Decimal = Field(0, alias="Fed_AGI")
    fed_ded: Decimal = Field(0, alias="Fed_Ded")
    fed_qbi_ded: Decimal = Field(0, alias="Fed_QBI_Ded")
    fed_tax_inc: Decimal = Field(0, alias="Fed_Tax_Inc")
    fed_tax: Decimal = Field(0, alias="Fed_Tax")
    fed_add_tax: Decimal = Field(0, alias="Fed_Add_Tax")
    fed_nonref_credit: Decimal = Field(0, alias="Fed_nonref_Credit")
    fed_other_tax: Decimal = Field(0, alias="Fed_other_tax")
    fed_tot_tax: Decimal = Field(0, alias="Fed_tot_Tax")
    fed_wh: Decimal = Field(0, alias="Fed_WH")
    fed_ref_credit: Decimal = Field(0, alias="Fed_ref_Credit")
    fed_owed_bal: Decimal = Field(0, alias="Fed_Owed_Bal")


    class Config:
        orm_mode = True
        allow_population_by_field_name = True  

class StateTaxCalculation(BaseModel):
    state_fed_inc: Decimal = Field(0, alias="State_Fed_Inc")
    state_adj_sub: Decimal = Field(0, alias="State_Adj_Sub")
    state_adj_add: Decimal = Field(0, alias="State_Adj_Add")
    state_adj_inc: Decimal = Field(0, alias="State_Adj_Inc")
    state_ded: Decimal = Field(0, alias="State_Ded")
    state_tax_inc: Decimal = Field(0, alias="State_Tax_Inc")
    state_tax: Decimal = Field(0, alias="State_Tax")
    state_exmpt: Decimal = Field(0, alias="State_Exmpt")
    state_wh: Decimal = Field(0, alias="State_WH")
    state_owed_bal: Decimal = Field(0, alias="State_Owed_Bal")
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
