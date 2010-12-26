from werkzeug.routing import Map, Rule

url_map = Map([
    Rule('/', endpoint =  'index'),
    Rule('/p<int:page_id>', endpoint =  'index'),
    Rule('/add/', endpoint =  'add'),
    Rule('/comment/', endpoint =  'comment'),
    Rule('/comments/', endpoint =  'comments')
])