from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('sqlite:///granjasys.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class TbOvos(Base):
    __tablename__ = 'tb_ovos'
    id_regovos = Column(Integer, primary_key=True, autoincrement=True)
    dt_ovos = Column(DateTime, default=datetime.utcnow)
    qt_ovos = Column(String)

    def __repr__(self):
        return f'<TbOvos(id_regovos={self.id_regovos}, dt_ovos={self.dt_ovos}, qt_ovos={self.qt_ovos})>'
    
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    @staticmethod
    def get_all():
        with engine.connect() as conn:
            query = "SELECT * FROM tb_ovos"
            result = conn.execute(query)
            return result.fetchall()

class TbGastos(Base):
    __tablename__ = 'tb_gastos'
    id_gastos = Column(Integer, primary_key=True, autoincrement=True)
    dt_gastos = Column(DateTime, default=datetime.utcnow)
    qt_gastos = Column(Float)
    tp_gastos = Column(String)

    def __repr__(self):
        return f'<TbGastos(id_gastos={self.id_gastos}, dt_gastos={self.dt_gastos}, qt_gastos={self.qt_gastos}, tp_gastos={self.tp_gastos})>'
    
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    @staticmethod
    def get_all():
        with engine.connect() as conn:
            query = "SELECT * FROM tb_gastos"
            result = conn.execute(query)
            return result.fetchall()

class TbVendas(Base):
    __tablename__ = 'tb_vendas'
    id_vendas = Column(Integer, primary_key=True, autoincrement=True)
    dt_vendas = Column(DateTime, default=datetime.utcnow)
    vl_vendas = Column(Float)

    def __repr__(self):
        return f'<TbVendas(id_vendas={self.id_vendas}, dt_vendas={self.dt_vendas}, vl_vendas={self.vl_vendas})>'
    
    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    @staticmethod
    def get_all():
        with engine.connect() as conn:
            query = "SELECT * FROM tb_vendas"
            result = conn.execute(query)
            return result.fetchall()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()