
"""<US Census>Copyright (c) 2020LicensedWritten by <Manpreet Kaur>"""

#Module file Capstone_Group2_Utility.py

#Here, we have balanced the male female dataset.Next, we selected the desired category i.e. >50K or <50K.

def high_salary(num, data):
    df_female = data[(data["sex"]=='Female') & ((data['education_number'] == num-3) | (data['education_number'] == num-2) | (data['education_number'] == num-1)|  (data['education_number'] == num))]
    df_male = data[(data["sex"]=='Male') & ((data['education_number'] == num-3) | (data['education_number'] == num-2) | (data['education_number'] == num-1)|  (data['education_number'] == num))].sample(df_female.shape[0])
    print("\nBalanced the male and female population size, Male population : {}, Female population : {}".format(df_male.shape[0], df_female.shape[0]))
    df_male = df_male[(df_male["income"]==">50K")]
    df_female = df_female[(df_female["income"]==">50K")]
        
    d = (((df_male.shape[0] - df_female.shape[0])/ df_male.shape[0])*100)
    print("\n The count of men with respect to women is " , str (d),"percentage")
    
    return(df_male, df_female)



def low_salary(num, data):
    df_female = data[(data["sex"]=='Female') & ((data['education_number'] == num-3) | (data['education_number'] == num-2) | (data['education_number'] == num-1)|  (data['education_number'] == num))]
    df_male = data[(data["sex"]=='Male') & ((data['education_number'] == num-3) | (data['education_number'] == num-2) | (data['education_number'] == num-1)|  (data['education_number'] == num))].sample(df_female.shape[0])
    print("\nBalanced the male and female population size, Male population : {}, Female population : {}".format(df_male.shape[0], df_female.shape[0]))
    df_male = df_male[(df_male["income"]=="<=50K")]
    df_female = df_female[(df_female["income"]=="<=50K")]

    d = (((df_male.shape[0] - df_female.shape[0])/ df_male.shape[0])*100)
    print("\n The count of men with respect to women is " , str (d),"percentage")
    return(df_male, df_female)








