To Run tests with allure reporting, enter in pycharm terminal:
pytest --alluredir=/tmp/my_allure_results TestCases.py

To Run tests without allure reporting, enter in pycharm terminal:
pytest TestCases.py

To view Allure reports, enter in pycharm terminal:
allure serve /tmp/my_allure_results

Required Packages:
Install allure : https://docs.qameta.io/allure/#_installing_a_commandline

packages installed (run pip freeze)
allure-pytest==2.8.40
allure-python-commons==2.8.40
allure-robotframework==2.8.40
atomicwrites==1.4.0
attrs==20.3.0
colorama==0.4.4
Faker==8.0.0
iniconfig==1.1.1
namedlist==1.8
packaging==20.9
pluggy==0.13.1
py==1.10.0
pyparsing==2.4.7
pytest==6.2.3
python-dateutil==2.8.1
pytz==2021.1
robotframework==4.0
selenium==3.141.0
six==1.15.0
text-unidecode==1.3
toml==0.10.2
urllib3==1.26.4


