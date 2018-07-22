from django.shortcuts import render
from django.shortcuts import redirect
from django import views
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe

def auth(func):
    def inner(request, *args, **kwargs):
        v = request.COOKIES.get('username')
        if not v:
            return redirect('/hostApp/login/')
        return func(request, *args, **kwargs)
    return inner

#CBV:
@method_decorator(auth, name='dispatch')
class Order(views.View):
    # @method_decorator(auth)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(Order,self).dispatch(request, *args, **kwargs)

    # @method_decorator(auth)
    def get(self, reqeust):
        v = reqeust.COOKIES.get('username111')
        return render(reqeust, 'index.html', {'current_user': v})

    def post(self, reqeust):
        v = reqeust.COOKIES.get('username111')
        return render(reqeust, 'index.html', {'current_user': v})