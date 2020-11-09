from flask import Flask,render_template, request

app = Flask(__name__,template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        i = request.form.getlist('value')
        text_field_1 = request.form.get('subject_1')
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
        if text_field_1 == 'exploring':
            print('cs')
        
        print(
            {
                'text_field_1':text_field_1,
                # 'text_field_2':text_field_2,
                # 'text_field_3':text_field_3,
                # 'text_field_4':text_field_4,
                # 'text_field_5':text_field_5,
                # 'text_field_6':text_field_6,
                # 'text_field_7':text_field_7,
                # 'text_field_8':text_field_8,
                # 'text_field_9':text_field_9,
                # 'text_field_10':text_field_10,
                # 'text_field_10':text_field_10,
                # 'text_field_11':text_field_11,
                # 'text_field_12':text_field_12,
            }
            )
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
    for i in majors:
        print(majors[i])
test_print()
if __name__ == '__main__':
    app.run(debug=True,port=5000)