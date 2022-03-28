from sqlalchemy.orm import scoped_session
from flask import _app_ctx_stack


def register_database(app):
    from app.database import LocalSession, engine
    from app.models.User import User

    User.metadata.create_all(bind=engine)

    app.session = scoped_session(LocalSession, scopefunc=_app_ctx_stack.__ident_func__)
