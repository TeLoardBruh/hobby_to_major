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
q1 = 'do you like computer? \n 1. Yes \n 2. No \n'
q2 = 'I\'m interested in law, debate, government, and politics. \n 1. Yes \n 2. No  \n'
q3 = "I'm interested in intellectual ideas, including those that are philosophical or religious. \n 1. Yes \n 2. No \n"
q4 = "I enjoy performing as an actor, or working behind the scenes on theatrical productions. \n 1. Yes \n 2. No \n"
q5 = "I like to offer advice to others. \n 1. Yes \n 2. No \n"
q6 = "I'm concerned about the state of the environment and want to work to improve it. \n 1. Yes \n 2. No \n"
q7 = "I enjoy working with people, and I have strong verbal and written communication skills. \n 1. Yes \n 2. No \n"
q8 = "I enjoy learning about how the human body and natural world work. \n 1. Yes \n 2. No \n"
q9 = "I want to work with people on the margins of society or who have been oppressed. \n 1. Yes \n 2. No \n"
q10 = "I'm interested in graphic and/or Web design. \n 1. Yes \n 2. No \n"
q11 = "I'm very ambitious, persuasive, and love coming up with my own ideas. \n 1. Yes \n 2. No \n"
q12 = "I especially love working with children. \n 1. Yes \n 2. No \n"
q13 = "I'm interested in science and enjoy helping people. \n 1. Yes \n 2. No \n"
q14 = "I like to sing and/or play musical instruments. \n 1. Yes \n 2. No \n"
q15 = "I have a strong interest and ability in visual art. \n 1. Yes \n 2. No \n"
q16 = "I enjoy learning about different parts of the world. \n 1. Yes \n 2. No \n" 
q17 = "I like to work with my hands and be outdoors. \n 1. Yes \n 2. No \n"
q18 = "I enjoy learning about languages. \n 1. Yes \n 2. No \n"
q19 = "I need the freedom to be creative and express myself. \n 1. Yes \n 2. No \n"
q20 = "I'm good with numbers and am detail-oriented. \n 1. Yes \n 2. No \n"
q21 = "I enjoy helping people. \n 1. Yes \n 2. No \n"
q22 = "I am interested in helping bodies heal and rehabilitate. \n 1. Yes \n 2. No \n" 
q23 = "I like math and figuring out how things work. \n 1. Yes \n 2. No \n"
q24 = "I'm interested in technology and learning how computers work. \n 1. Yes \n 2. No \n"
q25 = "I am interested in conflict resolution, criminal justice or mediation. \n 1. Yes \n 2. No \n"
q26 = "I am always reading a book or writing my own stories. \n 1. Yes \n 2. No \n"
q27 = "I like to experiment with better and faster ways of doing things. \n 1. Yes \n 2. No \n"


questions = [
    q1,
    q2,
    q3,
    q4,
    q5,
    q6,
    q7,
    q8,
    q9,
    q10,
    q11,
    q12,
    q13,
    q14,
    q15,
    q16,
    q17,
    q18,
    q19,
    q20,
    q21,
    q22,
    q23,
    q24,
    q25,
    q26,
    q27,
    ]
test_list = []
for i in questions:
    user_input = input(i)
    test_list.append(user_input)
print(test_list)
# user_list = []
# user_list.append(user_input)

# print(user_list)

# print (q1)
