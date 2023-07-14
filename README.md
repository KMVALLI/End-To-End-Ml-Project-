## this is my first project
## src --> components are useded for specifically training the data    inside the  components we have a modules is nothing but python files 
# 1) first we need to set up the setup.py file in that we mention requriedede packegers  and creatdede in requriement.txt file
# 2)  next we  creatded exeption.py file hear we are implimemtdede coustome exceptions  hear we used our own coustomexception funtion and with help of our base exception we are inheretded from base exception class the that converteded in to string 
# 3)  then we are implementded  logging funtinality to store in one file when ever  exception is riseded 
# 4) create a note book 

<!-- Student Performance Indicator
Life cycle of Machine learning Project
==>1)  Understanding the Problem Statement
==>2)  Data Collection
==>3)  Data Checks to perform
==>4)  Exploratory data analysis
==>5) Data Pre-Processing
==>6) Model Training
==>7) Choose best model


1) Problem statement

	This project understands how the student's performance (test scores) is affected by other variables such as Gender, Ethnicity, Parental level of education, Lunch and Test preparation course.
2) Data Collection
	Dataset Source - https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977
The data consists of 8 column and 1000 rows.

2.1)Import Data and Required Packages
Importing Pandas, Numpy, Matplotlib, Seaborn and Warings Library.

Import the CSV Data as Pandas DataFrame
df = pd.read_csv('data/stud.csv')

Show Top 5 Records
df.head()

Shape of the dataset(df.shape)



2.2 Dataset information

gender : sex of students -> (Male/female)
race/ethnicity : ethnicity of students -> (Group A, B,C, D,E)
parental level of education : parents' final education ->(bachelor's degree,some college,master's degree,associate's degree,high school)
lunch : having lunch before test (standard or free/reduced)
test preparation course : complete or not complete before test
math score
reading score
writing score

3. Data Checks to perform

==> Check Missing values 
df.isna().sum()

==> Check Duplicates
df.duplicated().sum()

==> Check data type
df.info()

==> Check the number of unique values of each column
df.nunique()


==> Check statistics of data set
df.describe()


==> Exploring Data
df.head()



==>  Adding columns for "Total Score" and "Average"

df['total score'] = df['math_score'] + df['reading_score'] + df['writing_score']
df['average'] = df['total score']/3
df.head()


4. Exploring Data ( Visualization )

4.1 Visualize average score distribution to make some conclusion.
Histogram
Kernel Distribution Function (KDE)

4.1.1 Histogram & KDE


4.2 Maximumum score of students in all three subjects



4.3 Multivariate analysis using pieplot





4.4.1 GENDER COLUMN



4.4.3 PARENTAL LEVEL OF EDUCATION COLUMN

4.4.4 LUNCH COLUMN

4.4.5 TEST PREPARATION COURSE COLUMN

4.4.6 CHECKING OUTLIERS
reparation course is benefitial. -->