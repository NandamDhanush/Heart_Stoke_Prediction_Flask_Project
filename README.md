According to the World Health Organization (WHO) stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths. In recent times, Heart Stroke prediction is one of the most complicated tasks in the medical field. In the modern era, approximately one person dies per minute due to heart Stroke. Data science plays a crucial role in processing huge amount of data in the field of healthcare. As heart stroke prediction is a complex task, there is a need to automate the prediction process to avoid risks associated with it and alert the patient well in advance.


The project aims to predict the chances of Heart Stroke and classifies the patient's risk level by implementing different Machine Learning techniques such as KNN, Decision Tree and Random Forest. From these models the Best performing model is selected and saved. Here we will be building a flask application that uses a machine learning model to get the prediction of heart stroke. We will also train our model on IBM Cloud and deployment on IBM Cloud.

Note:-
1) To work with the Stroke_Prediction.ipynb file, you can install Jupyter Notebook or Visual Studio Code (VS Code).

2) To download all the required Python libraries, use the following command format:-
   pip install <Library_Name>
   For example, to install Flask, use:-
   pip install flask
   Make sure to replace <Library_Name> with the name of the library you need to install.

3) Adjust the paths based on your system's directories. For example:- D:/Project/Training/model(or)mar_transform(or)res_transform(or)
   column in Flask_App/app.py (as referenced in the code), and set the dataset path accordingly in Stroke_Prediction.ipynb (also referenced in the code). For instance:- D:/Project/Dataset/Healthcare_Dataset_Stroke_Data.csv, as mentioned in both Flask_App/app.py and the Stroke_Prediction.ipynb file and don't change the project files structure.