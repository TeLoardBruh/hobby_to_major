user = {}

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
q1 = 'do you like computer?'
a1 = {'1': ['cs','des'],'2': ['chef','law','hnt']}
user_input  = input("please enter 1/2")
major_list = []
# tes = ['cs','des']
# major_list.append(tes)
print(major_list)
print(type(major_list))

if user_input:
    ans = a1[user_input]
    major_list.append(ans)

    print(major_list)
    print(ans)
    print(type(ans))

print (q1)