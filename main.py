from flask import Flask,render_template, request

app = Flask(__name__,template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    user = {}
    if request.method == 'POST':
        r1 = request.form['q1']
        
        # i1 = request.form.getlist('value1')
        # i2 = request.form.getlist('value2')
        # i3 = request.form.getlist('value3')
        # i4 = request.form.getlist('value4')
        # text_field_1 = request.form.get('subject_1')
        # text_field_2 = request.form.get('subject_2')
        # text_field_3 = request.form.get('subject_3')
        # text_field_4 = request.form.get('subject_4')
        # text_field_5 = request.form.get('subject_5')
        # text_field_6 = request.form.get('subject_6')
        # text_field_7 = request.form.get('subject_7')
        # text_field_8 = request.form.get('subject_8')
        # text_field_9 = request.form.get('subject_9')
        # text_field_10 = request.form.get('subject_10')
        # text_field_11 = request.form.get('subject_11')
        # text_field_12 = request.form.get('subject_12')
        print('====================')
        # user['value1'] = i1,i2
        # user['value2'] = i2
        # user['value3'] = i3
        # user['value4'] = i4
        # if user['value1'] == ['1']:
        #     print('cs')
        # print(user)
        # print(type(user))
        if 'submit' in request.form:
            print(r1)

    return render_template('index.html')

def test_print():
    majors = {
        'cs':'Computer Science',
        'des':'designer',
        'bus':'Business',
        'law':'law',
        'ce':'Civil & Structural Engineer',
        'med':'Medical',
        'hnt':'Hospitality & Tourism',
        'teac':'Teacher',
        'ir':'International Relation',
        'pi':'Pilot',
        'fl':'Flight attendent',
        'chef':'chef',
    }
    user = {}

    for i in majors:
        print(majors[i])
test_print()
if __name__ == '__main__':
    app.run(debug=True,port=5000)