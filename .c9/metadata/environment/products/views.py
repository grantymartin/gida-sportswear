{"filter":false,"title":"views.py","tooltip":"/products/views.py","undoManager":{"mark":51,"position":51,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["from django.shortcuts import render","","# Create your views here.","","def index(request):","    \"\"\" A View to return the index page\"\"\"","    ","    return render(request, 'home/index.html')",""]}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":9},"action":"remove","lines":["index"],"id":3},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["a"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["l"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["l"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["-"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":["p"]},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["r"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["o"]},{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":["d"]},{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["u"]}],[{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["c"],"id":4},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["t"]},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["s"]}],[{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"remove","lines":["-"],"id":5}],[{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["_"],"id":6}],[{"start":{"row":5,"column":29},"end":{"row":5,"column":34},"action":"remove","lines":["index"],"id":7},{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"insert","lines":["a"]},{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"insert","lines":["l"]},{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"insert","lines":["l"]}],[{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"insert","lines":[" "],"id":8},{"start":{"row":5,"column":33},"end":{"row":5,"column":34},"action":"insert","lines":["p"]},{"start":{"row":5,"column":34},"end":{"row":5,"column":35},"action":"insert","lines":["r"]},{"start":{"row":5,"column":35},"end":{"row":5,"column":36},"action":"insert","lines":["o"]},{"start":{"row":5,"column":36},"end":{"row":5,"column":37},"action":"insert","lines":["d"]},{"start":{"row":5,"column":37},"end":{"row":5,"column":38},"action":"insert","lines":["u"]},{"start":{"row":5,"column":38},"end":{"row":5,"column":39},"action":"insert","lines":["c"]}],[{"start":{"row":5,"column":39},"end":{"row":5,"column":40},"action":"insert","lines":["t"],"id":9},{"start":{"row":5,"column":40},"end":{"row":5,"column":41},"action":"insert","lines":["s"]}],[{"start":{"row":5,"column":46},"end":{"row":5,"column":47},"action":"insert","lines":[" "],"id":10},{"start":{"row":5,"column":47},"end":{"row":5,"column":48},"action":"insert","lines":["i"]},{"start":{"row":5,"column":48},"end":{"row":5,"column":49},"action":"insert","lines":["n"]},{"start":{"row":5,"column":49},"end":{"row":5,"column":50},"action":"insert","lines":["c"]},{"start":{"row":5,"column":50},"end":{"row":5,"column":51},"action":"insert","lines":["l"]},{"start":{"row":5,"column":51},"end":{"row":5,"column":52},"action":"insert","lines":["u"]},{"start":{"row":5,"column":52},"end":{"row":5,"column":53},"action":"insert","lines":["d"]},{"start":{"row":5,"column":53},"end":{"row":5,"column":54},"action":"insert","lines":["i"]},{"start":{"row":5,"column":54},"end":{"row":5,"column":55},"action":"insert","lines":["n"]},{"start":{"row":5,"column":55},"end":{"row":5,"column":56},"action":"insert","lines":["g"]}],[{"start":{"row":5,"column":56},"end":{"row":5,"column":57},"action":"insert","lines":[" "],"id":11},{"start":{"row":5,"column":57},"end":{"row":5,"column":58},"action":"insert","lines":["s"]},{"start":{"row":5,"column":58},"end":{"row":5,"column":59},"action":"insert","lines":["o"]}],[{"start":{"row":5,"column":59},"end":{"row":5,"column":60},"action":"insert","lines":["r"],"id":12},{"start":{"row":5,"column":60},"end":{"row":5,"column":61},"action":"insert","lines":["t"]},{"start":{"row":5,"column":61},"end":{"row":5,"column":62},"action":"insert","lines":["i"]},{"start":{"row":5,"column":62},"end":{"row":5,"column":63},"action":"insert","lines":["n"]},{"start":{"row":5,"column":63},"end":{"row":5,"column":64},"action":"insert","lines":["g"]}],[{"start":{"row":5,"column":64},"end":{"row":5,"column":65},"action":"insert","lines":[" "],"id":13},{"start":{"row":5,"column":65},"end":{"row":5,"column":66},"action":"insert","lines":["a"]},{"start":{"row":5,"column":66},"end":{"row":5,"column":67},"action":"insert","lines":["n"]},{"start":{"row":5,"column":67},"end":{"row":5,"column":68},"action":"insert","lines":["d"]}],[{"start":{"row":5,"column":68},"end":{"row":5,"column":69},"action":"insert","lines":[" "],"id":14},{"start":{"row":5,"column":69},"end":{"row":5,"column":70},"action":"insert","lines":["s"]},{"start":{"row":5,"column":70},"end":{"row":5,"column":71},"action":"insert","lines":["e"]},{"start":{"row":5,"column":71},"end":{"row":5,"column":72},"action":"insert","lines":["a"]},{"start":{"row":5,"column":72},"end":{"row":5,"column":73},"action":"insert","lines":["r"]},{"start":{"row":5,"column":73},"end":{"row":5,"column":74},"action":"insert","lines":["c"]},{"start":{"row":5,"column":74},"end":{"row":5,"column":75},"action":"insert","lines":["h"]}],[{"start":{"row":5,"column":75},"end":{"row":5,"column":76},"action":"insert","lines":[" "],"id":15},{"start":{"row":5,"column":76},"end":{"row":5,"column":77},"action":"insert","lines":["q"]},{"start":{"row":5,"column":77},"end":{"row":5,"column":78},"action":"insert","lines":["u"]},{"start":{"row":5,"column":78},"end":{"row":5,"column":79},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":79},"end":{"row":5,"column":80},"action":"insert","lines":["r"],"id":16},{"start":{"row":5,"column":80},"end":{"row":5,"column":81},"action":"insert","lines":["i"]},{"start":{"row":5,"column":81},"end":{"row":5,"column":82},"action":"insert","lines":["e"]},{"start":{"row":5,"column":82},"end":{"row":5,"column":83},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":28},"end":{"row":7,"column":32},"action":"remove","lines":["home"],"id":17},{"start":{"row":7,"column":28},"end":{"row":7,"column":29},"action":"insert","lines":["p"]},{"start":{"row":7,"column":29},"end":{"row":7,"column":30},"action":"insert","lines":["r"]},{"start":{"row":7,"column":30},"end":{"row":7,"column":31},"action":"insert","lines":["o"]},{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":["d"]},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":["u"]},{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["c"]},{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["t"]},{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["s"]}],[{"start":{"row":7,"column":37},"end":{"row":7,"column":42},"action":"remove","lines":["index"],"id":18},{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["p"]},{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["r"]},{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"insert","lines":["o"]},{"start":{"row":7,"column":40},"end":{"row":7,"column":41},"action":"insert","lines":["d"]},{"start":{"row":7,"column":41},"end":{"row":7,"column":42},"action":"insert","lines":["u"]},{"start":{"row":7,"column":42},"end":{"row":7,"column":43},"action":"insert","lines":["c"]},{"start":{"row":7,"column":43},"end":{"row":7,"column":44},"action":"insert","lines":["t"]}],[{"start":{"row":7,"column":44},"end":{"row":7,"column":45},"action":"insert","lines":["s"],"id":19}],[{"start":{"row":7,"column":51},"end":{"row":7,"column":52},"action":"insert","lines":[","],"id":20}],[{"start":{"row":7,"column":52},"end":{"row":7,"column":53},"action":"insert","lines":[" "],"id":21},{"start":{"row":7,"column":53},"end":{"row":7,"column":54},"action":"insert","lines":["c"]},{"start":{"row":7,"column":54},"end":{"row":7,"column":55},"action":"insert","lines":["o"]},{"start":{"row":7,"column":55},"end":{"row":7,"column":56},"action":"insert","lines":["n"]},{"start":{"row":7,"column":56},"end":{"row":7,"column":57},"action":"insert","lines":["t"]},{"start":{"row":7,"column":57},"end":{"row":7,"column":58},"action":"insert","lines":["e"]},{"start":{"row":7,"column":58},"end":{"row":7,"column":59},"action":"insert","lines":["x"]},{"start":{"row":7,"column":59},"end":{"row":7,"column":60},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":35},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":22},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["i"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["m"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["p"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["o"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["r"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":[" "],"id":23},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["."]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["m"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["o"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["d"]},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["e"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["l"]}],[{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["s"],"id":24}],[{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":[" "],"id":25},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["i"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":["m"]},{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"insert","lines":["p"]},{"start":{"row":1,"column":18},"end":{"row":1,"column":19},"action":"insert","lines":["o"]},{"start":{"row":1,"column":19},"end":{"row":1,"column":20},"action":"insert","lines":["r"]}],[{"start":{"row":1,"column":20},"end":{"row":1,"column":21},"action":"insert","lines":["t"],"id":26}],[{"start":{"row":1,"column":21},"end":{"row":1,"column":22},"action":"insert","lines":[" "],"id":27},{"start":{"row":1,"column":22},"end":{"row":1,"column":23},"action":"insert","lines":["P"]},{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["r"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["o"]},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":["d"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"insert","lines":["u"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"insert","lines":["c"]}],[{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"insert","lines":["t"],"id":28},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"insert","lines":["s"]}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":6},"action":"remove","lines":["import"],"id":29},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["f"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["r"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["o"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"remove","lines":["s"],"id":30}],[{"start":{"row":6,"column":86},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":31},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":8,"column":0},"action":"insert","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["p"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["r"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["o"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["d"]}],[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["u"],"id":32},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["c"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["t"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":[" "],"id":33},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["="]}],[{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":[" "],"id":34},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["P"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["r"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["o"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["d"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["u"]}],[{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["c"],"id":35},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["t"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["."]},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["o"]}],[{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"insert","lines":["b"],"id":36},{"start":{"row":8,"column":25},"end":{"row":8,"column":26},"action":"insert","lines":["j"]},{"start":{"row":8,"column":26},"end":{"row":8,"column":27},"action":"insert","lines":["e"]},{"start":{"row":8,"column":27},"end":{"row":8,"column":28},"action":"insert","lines":["c"]},{"start":{"row":8,"column":28},"end":{"row":8,"column":29},"action":"insert","lines":["t"]},{"start":{"row":8,"column":29},"end":{"row":8,"column":30},"action":"insert","lines":["."]}],[{"start":{"row":8,"column":30},"end":{"row":8,"column":31},"action":"insert","lines":["a"],"id":37},{"start":{"row":8,"column":31},"end":{"row":8,"column":32},"action":"insert","lines":["l"]},{"start":{"row":8,"column":32},"end":{"row":8,"column":33},"action":"insert","lines":["l"]}],[{"start":{"row":8,"column":33},"end":{"row":8,"column":35},"action":"insert","lines":["()"],"id":38}],[{"start":{"row":8,"column":35},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]},{"start":{"row":9,"column":4},"end":{"row":10,"column":0},"action":"insert","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]},{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["c"]},{"start":{"row":10,"column":5},"end":{"row":10,"column":6},"action":"insert","lines":["o"]},{"start":{"row":10,"column":6},"end":{"row":10,"column":7},"action":"insert","lines":["n"]},{"start":{"row":10,"column":7},"end":{"row":10,"column":8},"action":"insert","lines":["t"]},{"start":{"row":10,"column":8},"end":{"row":10,"column":9},"action":"insert","lines":["e"]},{"start":{"row":10,"column":9},"end":{"row":10,"column":10},"action":"insert","lines":["x"]},{"start":{"row":10,"column":10},"end":{"row":10,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":10,"column":11},"end":{"row":10,"column":12},"action":"insert","lines":[" "],"id":40},{"start":{"row":10,"column":12},"end":{"row":10,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":10,"column":13},"end":{"row":10,"column":14},"action":"insert","lines":[" "],"id":41},{"start":{"row":10,"column":14},"end":{"row":10,"column":15},"action":"insert","lines":["{"]}],[{"start":{"row":10,"column":15},"end":{"row":12,"column":5},"action":"insert","lines":["","        ","    }"],"id":42}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":10},"action":"insert","lines":["''"],"id":43}],[{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["p"],"id":44},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["r"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["o"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["d"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["u"]},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":["c"]},{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["s"],"id":45}],[{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"insert","lines":[":"],"id":46}],[{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":[" "],"id":47},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":["p"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["r"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"insert","lines":["o"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"insert","lines":["d"]},{"start":{"row":11,"column":24},"end":{"row":11,"column":25},"action":"insert","lines":["u"]}],[{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"insert","lines":["c"],"id":48},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"insert","lines":["t"]},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"insert","lines":["s"]},{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"insert","lines":[","]}],[{"start":{"row":11,"column":29},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":49},{"start":{"row":12,"column":0},"end":{"row":12,"column":8},"action":"insert","lines":["        "]},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"insert","lines":["}"]}],[{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"remove","lines":["}"],"id":50},{"start":{"row":12,"column":4},"end":{"row":12,"column":8},"action":"remove","lines":["    "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "]},{"start":{"row":11,"column":29},"end":{"row":12,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["from django.shortcuts import render","from .models import Product","","# Create your views here.","","def all_products(request):","    \"\"\" A View to return the all products page including sorting and search queries\"\"\"","    ","    products = Product.object.all()","    ","    context = {","        'products': products,","    }","    ","    return render(request, 'products/products.html', context)",""],"id":51}],[{"start":{"row":0,"column":0},"end":{"row":15,"column":61},"action":"insert","lines":["","from django.shortcuts import render","from .models import Product","","# Create your views here.","","def all_products(request):","    \"\"\" A view to show all products, including sorting and search queries \"\"\"","","    products = Product.objects.all()","","    context = {","        'products': products,","    }","","    return render(request, 'products/products.html', context)"],"id":52}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":53}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":0,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1591979532005,"hash":"6f8e4dff92c02358b4725e212d60c5402293c8bb"}