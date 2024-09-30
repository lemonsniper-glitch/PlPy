import pandas as pd
import openpyxl
import fsspec

words = ''
with open("C://Users//Prajwal//Desktop//s2.txt", 'r') as file:

# Reading the input file:
    text = file.read()
    words = text.split()

# Fetching all the ids:
# id_list = []
# for word in words:
#     if word[0:3] == 'SOS' or word[0:3] == 'KXD':
#         id_list.append(word)

# Fetching all Names:
name_list = []
for i in range(0,len(words)):
    name = ''
    if words[i][0:4] == 'Name' and words[i-1] not in ['Fathers', 'Husbands', 'Husban','ds','Mothers','Others','Name:']:
        k = i+1
        while k < len(words) and words[k] not in ['Fathers', 'Husbands','Husban','ds' 'Mothers','Others','Name:']:
            if words[k] != ':':
                name = name + " "+words[k]
            k = k + 1
        if name != '':
            name_list.append(name)

#Fetching all Relaiton Names:
relation_name_list = []
relations = ['Fathers', 'Husbands','Husban','ds' 'Mothers','Others']
for i in range(0,len(words)):
    relation_name = ''
    if words[i] in relations:
        k = i + 2
        while k < len(words) and words[k] not in ['House','House Number']:
            if words[k] != ':':
                relation_name = relation_name + " "+words[k]
            k = k + 1
        relation_name_list.append(words[i]+ ' Name: '+relation_name)

#Fetching all House No:
house_no_list = []
for i in range(0,len(words)):
    house_no = ''
    if words[i] == 'House':
        k = i + 1
        while k < len(words) and words[k] not in ['Age']:
            if words[k] != ':':
                house_no = house_no + " "+ words[k]
            k = k + 1
        house_no_list.append(house_no)

#Fetching Age:
age_list = []
for i in range(0, len(words)):
    age = ''
    if words[i] == 'Age' or words[i] == 'Age:':
        k = i + 1
        while k < len(words) and words[k] not in ['Gender', 'Gender:']:
            if words[k] != ':':
                age = age + words[k]
            k = k + 1
        age_list.append(age)

#Fetching Gender:
gender_list = []
for i in range(0, len(words)):
    gender = ''
    if words[i] in ["Gender", "Gender:"]:
        k = i + 1
        while k < len(words) and words[k] not in ['Photo', 'Available', 'Photo Available']:
            if words[k] != ':':
                gender = gender + words[k]
            k = k + 1
        gender_list.append(gender)




# Determine the maximum length among all lists
max_length = max(len(name_list), len(relation_name_list), len(house_no_list), len(age_list), len(gender_list))

# Pad shorter lists with None to match the maximum length
name_list += [None] * (max_length - len(name_list))
relation_name_list += [None] * (max_length - len(relation_name_list))
house_no_list += [None] * (max_length - len(house_no_list))
age_list += [None] * (max_length - len(age_list))
gender_list += [None] * (max_length - len(gender_list))

# Writing the data to excel:
schema = {
    'Name': name_list,
    'Related to': relation_name_list,
    'House number': house_no_list,
    'Age': age_list,
    'Gender': gender_list
}

# Create a DataFrame from the schema
df = pd.DataFrame(schema)
excel_file_name = 'C://Users//Prajwal//Desktop//op.xlsx'
df.to_excel(excel_file_name, index=False)

print('Write was successful')
