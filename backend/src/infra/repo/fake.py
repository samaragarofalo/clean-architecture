from backend.src.infra.config import DBConnectionHandler
from backend.src.infra.entities.users import Users


class FakeRepo:
    """A simple repository"""

    @classmethod
    def insert_user(cls):
        """something"""

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Programador", password="Gigi")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
