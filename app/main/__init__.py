from flask import Blueprint

#initializing blueprint .It takes two arguements 
#the name of the blueprint "Main" and  __name__ variable to find the location of the blueprint.

main=Blueprint('main',__name__)

from . import views,errors,forms
