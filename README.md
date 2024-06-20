# Bangkit 2024 Capstone Team : Credit (C241-PS483)

Hello everyone!. Here is our repository Machine Learning path Team for Bangkit 2024 Capstone project. Our team consist of 3 Machine Learning, 2 Android, and 2 Cloud Computing.

## Our Knights

|            Nama             |  Bangkit-ID  |       Path       |
| :-------------------------: | :----------: | :--------------: |
|        Ariyova Banua        | M391D4KY1880 | Machine Learning |
|       Fajar Al Najiim       | M391D4KY2415 | Machine Learning |
|   Josep Daniel Simatupang   | M391D4KY2654 | Machine Learning |
|      Zaky Irsyad Rais       | C214D4KY0273 | Cloud Computing  |
|       Hanun Salsabila       |   C0121278   | Cloud Computing  |
| Ahmad Ryan Saffah Yartavick | A548D4NY4609 |     Android      |
|       Ekasari Amalia        | A548D4NX4606 |     Android      |

## What is this project

We created a mobile application called **Credit Predict**.

**Credit Predict** is an application to predict credit card applications by customers by inputting personal data, and various other certain data. With this application, everyone can check whether their personal data such as age, work history, and so on are eligible to be approved to get a credit card application or even rejected.

## Guidance for running our model on local

Make sure you intalled all this dependencies first on your local machine. You can use conda virtual env for making things easier with pip

```text
Flask==3.0.3
Flask-Cors==4.0.1
gunicorn==22.0.0
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
packaging==24.1
python-dotenv==1.0.1
Werkzeug>=3.0.0
tensorflow
numpy
pandas
scikit-learn
```

For using our CNN Model, You must clone our repository first with this following command :

`git clone https://github.com/Jafarrrr25/CapstoneML.git`

after cloning the repository, go to the CapstoneML directory and run the following command on your favorite CLI (make sure you are in /CapstoneML app.py) :

`if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)`

We already provide you all of the data set and NLP model, so you just need to run the command above

You can also test our API [Here](https://creditapp-64tbubeb5q-et.a.run.app/predict)

## Project Update

**TBD**
