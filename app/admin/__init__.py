# so that we can import anything from admin folder
# without the extra admin syntax
from admin import *
from flask.views import MethodView
from .models import Banner

class CRUDView(MethodView):
    list_template = 'admin/list_view.html'

    def __init__(self, model, endpoint, list_template=None):
        self.model = model
        self.endpoint = endpoint
        # so we can generate a url relevant to this
        # endpoint, for example if we utilize this CRUD object
        # to enpoint comments the path generated will be
        # /admin/comments/

        self.path = url_for('.{}'.format(self.endpoint))
        if list_template:
            self.list_template = list_template

    def get():
        obj = self.model.query.all()
        return render_template(list_template, obj=obj, path=self.path)


# this turns the class to a function that flask can use for requests
# the argument it takes is the endpoint that you can call in url_for()
# since we are using a blueprint called admin the endpoint becomes
# in this case 'admin.banner' or simply '.banner'
# the '.' links to the current app(which is 'admin')
view = CRUDView.as_view('banner')

admin.add_url_rule('/banner/', view_func=view, methods=['GET', 'POST'])
