import pandas as pd

df = pd.read_csv('tarea7_mysql\\train.csv')

print(df)
# age = df["Age"]
# print(age)

df = pd.DataFrame()
# print(df)

# ----------------------------------------------------------------
# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]

df = pd.DataFrame(data, columns=['Name', 'Age'])
# print(df)
# ----------------------------------------------------------------
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}
 
df = pd.DataFrame(data)
print(df)
df.to_csv('tarea7_mysql\\my.csv')
# ----------------------------------------------------------------
data = [{'a': 1, 'b': 2, 'c': 3},
        {'a': 10, 'b': 20, 'c': 30}]

df = pd.DataFrame(data)
# print(df)
# ----------------------------------------------------------------
data = [{'b': 2, 'c': 3}, {'a': 10, 'b': 20, 'c': 30}]
 
df = pd.DataFrame(data, index=['first', 'second'])

# print(df)
# ----------------------------------------------------------------
d = {'one': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd']),
     'two': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
# print(df)
# ----------------------------------------------------------------
data = {'Name': ['Tom', 'Jack', 'nick', 'juli'],
        'marks': [99, 98, 95, 90]}

df = pd.DataFrame(data, index=['rank1',
                               'rank2',
                               'rank3',
                               'rank4'])
# print(df)



# print(df["PassengerId"].dtypes)
# print(df["Name"].dtypes)
# print(df["Age"].dtypes)
# print(df["Survived"].dtypes)
# print(df["Cabin"].dtypes)
# df['Age'] = df['Age'].astype(int)
# gender_male = df[df["Sex"] == "male"]
# gender_female = df[df["Sex"] == "female"]

# data_male = gender_male[["PassengerId", "Survived","Name","Cabin"]]
# data_female = gender_female[["PassengerId", "Survived","Name","Cabin"]]

# print(data_male.head())
# print(data_female.head())

# data_males = gender_male[["PassengerId", "Name", "Age", "Survived","Cabin"]].fillna(0).sample(n=100)
# data_females = gender_female[["PassengerId", "Name", "Age", "Survived","Cabin"]].sample(n=100)

# my_tuple = (
#     data_males["PassengerId"].to_string(index=False), 
#     data_males["Survived"].to_string(index=False), 
#     data_males["Name"].to_string(index=False), 
#     data_males["Cabin"].to_string(index=False)
#     )

# my_new_tuple = [
#     data_males.iloc[0, 0]
# ]

# print(data_males["PassengerId"].fillna(0).to_string(index=False))
# print(data_males["Name"].to_string(index=False))
# print(data_males["Age"].to_string(index=False))
# print(data_males["Survived"].to_string(index=False))
# print(data_males["Cabin"].to_string(index=False))
# print(my_new_tuple)

# for i in range(len(data_males)):
#     my_tuple = [(
#         data_males.iloc[i, 0], 
#         data_males.iloc[i, 1],
#         data_males.iloc[i, 2],
#         data_males.iloc[i, 3],
#         data_males.iloc[i, 4]
#         )]
#     print(my_tuple)


# data_males.to_csv('tarea7_mysql\\male_db.csv', index=False)
# data_females.to_csv('tarea7_mysql\\female_db.csv', index=False)

# print(type(gender_male))
# print(gender_female.head())
# print(gender_female.shape)
# print(type(gender_female))
# age = subset["Age"]
# print(type(age))
# print(df.info())

