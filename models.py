from sqlalchemy import Column, TIMESTAMP, Integer, text, DECIMAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PerformanceData(Base):
    __tablename__ = "performance_data"

    ymdh = Column("ymdh", TIMESTAMP, primary_key=True, nullable=False)
    campaign_id = Column("campaign_id", Integer, primary_key=True, nullable=False)
    creative_id = Column("creative_id", Integer, primary_key=True, nullable=False)
    imps = Column("imps", Integer)
    clicks = Column("clicks", Integer)
    last_modified = Column("last_modified", TIMESTAMP,
                           server_default=text("CURRENT_TIMESTAMP"))

class CreativeWeights(Base):
    __tablename__ = "creative_weights"

    campaign_id = Column("campaign_id", Integer, primary_key=True, nullable=False)
    creative_id = Column("creative_id", Integer, primary_key=True, nullable=False)
    weight = Column("weight", DECIMAL(9, 6, asdecimal=False), nullable=False,
                    default=0)
    last_modified = Column("last_modified", TIMESTAMP,
                           server_default=text("CURRENT_TIMESTAMP"))

    def __init__(self, campaign_id, creative_id, weight):
        self.campaign_id = campaign_id
        self.creative_id = creative_id
        self.weight = weight