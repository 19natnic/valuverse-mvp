from datetime import datetime, date
from sqlalchemy import (
    Column, String, Integer, Float, DateTime, Date, ForeignKey, Text
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Property(Base):
    __tablename__ = "properties"
    id = Column(String, primary_key=True)
    property_type = Column(String, nullable=False)   # condo | house | land
    address_line = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)
    land_rai = Column(Integer, default=0)
    land_ngan = Column(Integer, default=0)
    land_wah = Column(Integer, default=0)
    built_area_sqm = Column(Float, default=0)
    year_built = Column(Integer)

class Valuation(Base):
    __tablename__ = "valuations"
    id = Column(String, primary_key=True)
    property_id = Column(String, ForeignKey("properties.id"))
    valuation_type = Column(String, nullable=False)  # quick | verified | full
    est_value = Column(Float)
    low_value = Column(Float)
    high_value = Column(Float)
    confidence = Column(String)                      # Low | Medium | High
    status = Column(String, default="awaiting_valuer")  # awaiting_valuer | approved | rejected
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    approved_by = Column(String)
    approved_at = Column(DateTime)

class Comparable(Base):
    __tablename__ = "comparables"
    id = Column(String, primary_key=True)
    property_type = Column(String, nullable=False)
    address = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)
    area_sqm = Column(Float)
    land_sqm = Column(Float)
    price = Column(Float)
    transaction_date = Column(Date)
    source = Column(String)   # portal | internal | transaction

class ValuationComp(Base):
    __tablename__ = "valuation_comps"
    valuation_id = Column(String, primary_key=True)
    comp_id = Column(String, primary_key=True)
    distance_m = Column(Float)
    adj_percent = Column(Float)
    weight = Column(Float)
