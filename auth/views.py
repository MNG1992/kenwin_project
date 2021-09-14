from pyramid.httpexceptions import HTTPFound
from pyramid.security import (
    remember,
    forget,
)

from pyramid.view import (
    view_config,
    view_defaults,
)

from .models import User, DBSession
from .security import check_password


@view_defaults(renderer='templates/home.jinja2')
class TutorialViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config(route_name='home')
    def home(self):
        return {'name': 'Home View'}

    @view_config(route_name='login', renderer='templates/login.jinja2')
    def login(self):
        request = self.request
        login_url = request.route_url('login')
        referrer = request.url
        if referrer == login_url:
            referrer = '/'
        came_from = request.params.get('came_from', referrer)
        message = ''
        login = ''
        password = ''
        if 'form.submitted' in request.params:
            login = request.params['login']
            password = request.params['password']
            user = DBSession.query(User).filter_by(username=login).first()
            if user and check_password(password, user.password):
                headers = remember(request, login)
                return HTTPFound(location=came_from, headers=headers)
            message = 'Username or password incorrect'

        return dict(
            name='Login',
            message=message,
            url=request.application_url + '/login',
            came_from=came_from,
            login=login,
            password=password,
        )

    @view_config(route_name='logout')
    def logout(self):
        request = self.request
        headers = forget(request)
        url = request.route_url('home')
        return HTTPFound(location=url, headers=headers)
