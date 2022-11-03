# ATM OTP AUTH SYSTEM
This is proof of concept of implementation of OTP authentication as Multifactor Authentication in Automated tailor machine (ATM) for enhanced security in fincancial sector. 

# Tools & Technology 
This proof of concept will be based on python, Tkinter for GUI ATM-Like Appearance,  & use twilio API for sending SMS to phone with OTP code. 

# Concept 
Enable the multi-factor Authentication in ATM system where user have to go through a added step to access their account from ATM card in ATM machine. Likewise in traditional ATM systems, Users need to insert thier card which is first step of authentication of the user and requires to enter their pin. The added step will be, after user is verified with the ATM card and Pin, The user needs to provide an OTP code sent to the verified phone number by the user and only then they will be able to access the account and withdraw amount from their account. 

# About ATM simulator
This ATM simulator is made with python using tkinter module for GUI interface, This system is based on MySQl database and Twilio API. I have tried to give the real-atm experience in the simulator making the ATM looks alike to the real automated tailor machines available in the real world. The requirements for running this simulator are mentioned below and in requirements.txt file. 

##### certifi==2022.12.7
##### charset-normalizer==3.0.1
##### idna==3.4
##### mysql-connector-python==8.0.32
##### playsound==1.2.2
##### protobuf==3.20.3
##### PyJWT==2.6.0
##### pytz==2022.7.1
##### requests==2.28.2
##### twilio==7.16.2
##### urllib3==1.26.14

The steps to run the program is, 

### Step 1: create a Virtual Environment 

##### pip install virtualenv
##### python -m venv .env

### Step 2: activate the virtual Environment

#### Linux
##### source .env/bin/activate

#### Windows 
##### .env/Scripts/activate

### Step 3 : Install the Requirements
##### pip install -r requirement.txt

### step 4: Run the application. 
##### python atm_simulator.py 

### NOTE
Please Change the credentials of the database in the code as per yours to run the program. 