{"filter":false,"title":"admin.py","tooltip":"/products/admin.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.contrib import admin","","# Register your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":5,"column":29},"action":"insert","lines":["from django.contrib import admin","from .models import Product, Category","","# Register your models here.","admin.site.register(Product)","admin.site.register(Category)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":29},"end":{"row":5,"column":29},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1591911988577,"hash":"0486a63665ebd74a6eedf3bde04b766633c1128d"}