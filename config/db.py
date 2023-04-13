from sqlalchemy import create_engine, MetaData
from urllib.parse import quote_plus

engine = create_engine("mysql+pymysql://root:%s@localhost:3306/job_application_system" %quote_plus("Sanskar@1234"))
meta = MetaData()
conn = engine.connect()