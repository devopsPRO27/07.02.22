import random

from flask import Flask
from flask import redirect,url_for

app=Flask(__name__)


@app.route('/')
def home_page():
    return f'guy is the best'

@app.route('/king')
def king_page():
    return 'tomer is a king'

@app.route('/quotes')
def quotes_page():
    lis=['old keys dont open new doors','be a warrior not a worrier','no pain ni gain ','pizza is life ','with great power comes great responsibilty']
    i=random.randint(0,4)
    return f'<h1 style="color:aqua;"> the quote of the day is :{lis[i]}</h1>'

@app.route('/htmlexm')
def htmlexm():
    return '<body><h1>hodi is king </h1><p> this is paragraph <br> cake is life</p> \
    <h1 style="color:aqua;"> this text is blue</h1><button> hothaifa </button><form><p>first name\
     <input id="11" name="firstnametxt" type="password" required=true></p><p>Email <input id="12" name="emailtxt" \
     type="email" required=true ></p><button>ok</button></form></body>'

@app.route('/hello/<name>')
def hello_name(name):
    return f'hello {name}'


# targil - create URL which gets 2 numbers and print their sum
# 'sum/3/4' --> will display: 3 + 4 = 7
@app.route('/calc/<int:x>/<int:y>')
def calc(x,y):
    return f'{x} + {y} = {x+y} '


@app.route('/calc2/<int:x>')
def calc2(x):
    return f'{x%10} + {x//10} = {x//10+x%10} '


@app.route('/pizza')
def pizza():
    return redirect('https://www.google.com/search?q=pizza&sxsrf=APq-WBsZMIbfnMsvMQyUyaWuN8vXGWrTJQ:1644260503227&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj1zNnZo-71AhW0oFwKHQDTBIcQ_AUoAXoECAMQAw&biw=764&bih=308&dpr=1.25')


@app.route('/admin')
def admin_page():
    return f'welcome SIR   ADMIN'

@app.route('/login/<name>')
def hello_user(name):
    if name=="oreil":
        return redirect(url_for('admin_page'))
    else:
        return f'hiiii {name} '




app.run()