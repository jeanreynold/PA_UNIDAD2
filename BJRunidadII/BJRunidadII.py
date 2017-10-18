from flask import Flask, render_template, request, redirect
from test_module3 import cubo_area, cubo_vol

app = Flask(__name__)


@app.route('/')
def hello_world() ->'302':
    return redirect('/entry')


@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html',the_title='Area')


@app.route('/test_module3', methods=['POST'])
def b() -> 'html':
    a = float(request.form['a'])
    title = 'Aqui esta el resultado'
    result = float(cubo_area(a))
    return render_template('result.html',
                           the_a=a,
                           the_title=title,
                           the_result=result, )

def c() -> 'html':
    a = float(request.form['a'])
    title = 'Aqui es el resultado'
    result = float(cubo_vol(a))
    return render_template('result.html',
                           the_a=a,
                           the_title=title,
                           the_result=result, )




if __name__ == '__main__':
    app.run()

