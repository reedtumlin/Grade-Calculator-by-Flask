# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:57:08 2021

@author: MXS3524
"""

from flask import Flask,render_template,request
import datetime as dt


grades_dict={}
colors_dict={}
colors_dict['A']='green'
colors_dict['B']='blue'
colors_dict['C']='orange'
colors_dict['D']='purple'
colors_dict['F']='red'

colors=['RED','BLUE','GREEN','YELLOW','ORANGE','PURPLE','GREY','SILVER','TEAL']

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
    }


app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/<name>')
def hello_name(name):
    return f"Hello {name}..."


@app.route('/color',methods=['GET','POST'])
def show_page():
    if request.method=='GET':
        return render_template('color.html')
    elif request.method=='POST':
        name=request.form['student_name']
        color=request.form['student_color']
        data={'name' : name, 'color' : color}
        return render_template('color.html',data=data)
        


@app.route('/gradetracker',methods=['GET'])
def show_grades():
    return render_template('grades.html')
    
@app.route('/dictionary',methods=['GET'])
def show_dict():
    return str(grades_dict)

@app.route('/calculate',methods=['POST','GET'])
def show_calculation():
    #global grades_dict
    grades=request.form['grades']
    name=request.form['student_name']
    grades=grades.split(';')
    grades=[int(g) for g in grades]
    final_grade=sum(grades) / len(grades)
    if 90 <=final_grade<=100:
        grade='A'
    elif 80 <=final_grade<90:
        grade='B'    
    elif 70 <=final_grade<80:
        grade='C'
    elif 60 <=final_grade<70:
        grade='D'    
    else:
        grade='F'
     
        
    grades_dict.update({name : [final_grade,grade]})
    grades_output='Here are the final grades:<br><br>'
    for key,val in grades_dict.items():
        color_setting=f"'color:{colors_dict[val[1]]}'"
        grades_output+=f'<label style={color_setting}>{key}:{val[0]}</label><br>'
    grades_output+='<a href="/gradetracker">Enter Grades</a>'    
    
    
    return grades_output
    


@app.route('/states',methods=['GET','POST'])
def show_states():
    return render_template('states2.html')








   
if __name__=='__main__':
    app.debug=True
    app.run(port=8000)