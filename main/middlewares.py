from . import models
from django.shortcuts import get_object_or_404

def basket_middleware(get_response):
    def middleware(request):
        if "basket_id" in request.session:
            basket_id = request.session["basket_id"]
            basket = get_object_or_404(models.Basket,id=basket_id)
            request.basket = basket
        else:
            request.basket = None

        response = get_response(request)
        return response

    return middleware
