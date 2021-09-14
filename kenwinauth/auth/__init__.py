from pyramid.config import Configurator

from .security import SecurityPolicy

from sqlalchemy import engine_from_config

from .models import DBSession, Base

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.set_security_policy(
        SecurityPolicy(
            secret=settings['auth.secret'],
        ),
    )
    config.add_route('home', '/')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.scan('.views')
    return config.make_wsgi_app()
