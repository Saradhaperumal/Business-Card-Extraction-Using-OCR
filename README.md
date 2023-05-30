# Business-Card-Extraction-Using-OCR
Extracting Business Card Data with OCR and display using Streamlit


**Problem Statement:**

Developing a Streamlit application that allows users to upload an image of a business card and extract relevant information from it using
easyOCR. The extracted information should include the company name, card holder name, designation, mobile number, email address, website URL, area, city, state,
and pin code. The extracted information should then be displayed in the application's graphical user interface (GUI)

In addition, the application should allow users to save the extracted information into a database along with the uploaded business card image. The database should be
able to store multiple entries, each with its own business card image and extracted information.

Packages Used:

Streamlit
Python
EasyOCR
Sqlite

Approach:

1. Install the required packages: You will need to install Python, Streamlit,easyOCR, and a database management system like SQLite or MySQL.


3. Design the user interface: Create a simple and intuitive user interface using Streamlit that guides users through the process of uploading the business
card image and extracting its information. You can use widgets like file uploader, buttons, and text boxes to make the interface more interactive.


3. Implement the image processing and OCR: Use easyOCR to extract the relevant information from the uploaded business card image. You can use
image processing techniques like resizing, cropping, and thresholding to enhance the image quality before passing it to the OCR engine.

4. Display the extracted information: Once the information has been extracted,display it in a clean and organized manner in the Streamlit GUI. You can use
widgets like tables, text boxes, and labels to present the information.

5. Implement database integration: Use a database management system like SQLite or MySQL to store the extracted information along with the uploaded
business card image. You can use SQL queries to create tables, insert data,and retrieve data from the database, Update the data and Allow the user to
delete the data through the streamlit UI

6. Test the application: Test the application thoroughly to ensure that it works as expected. You can run the application on your local machine by running the
command streamlit run app.py in the terminal, where app.py is the name of your Streamlit application file.

7. Improve the application: Continuously improve the application by adding new features, optimizing the code, and fixing bugs. You can also add user
authentication and authorization to make the application more secure.
![image](https://github.com/Saradhaperumal/Business-Card-Extraction-Using-OCR/assets/116868444/e35a4438-c3c8-451d-981b-059a4a5f1370)
![image](https://github.com/Saradhaperumal/Business-Card-Extraction-Using-OCR/assets/116868444/e54050ce-1691-4585-a475-dbcf5ffa36cc)
![image](https://github.com/Saradhaperumal/Business-Card-Extraction-Using-OCR/assets/116868444/3f793270-31d1-4fd2-99d6-0ba650f052b6)
![image](https://github.com/Saradhaperumal/Business-Card-Extraction-Using-OCR/assets/116868444/9a44e9b0-03b3-4d76-b17e-d076eb545310)



