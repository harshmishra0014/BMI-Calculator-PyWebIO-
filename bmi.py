from pywebio.input import *
from pywebio.output import *

def bmicalculator():
    name=input("Please enter name")
    height=input("Please enter the height in cm",type=FLOAT)
    weight=input("Please enter the weight in Kg",type=FLOAT)
    
    bmi=weight/(height/100)**2
    
    bmi_output=[(16, 'Severely underweight'), (18.5, 'Underweight'),
                  (25, 'Normal'), (30, 'Overweight'),
                  (35, 'Moderately obese'), (float('inf'), 'Severely obese')]
    
    for tuple1,tuple2 in bmi_output:
        if bmi<=tuple1:
            put_text('Hey',name,'! your BMI is :%.1f and you are :%s'%(bmi,tuple2))
            break
        
    
if __name__=='__main__':
    bmicalculator()