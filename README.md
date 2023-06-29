# Library Book Collection and Reservation System
# DCPE/FT/2A/02 - Group B

To encourage and increase the number of people reading and loaning books from the
public libraries, an automated book loan and return system is proposed.

## How the Library Book Collection and Reservation System works
The Library Book Collection and Reservation System works in the following manner:
- Individual users are allowed to borrow / reserve a maximum of 10 books at any time

**Reservation:**
- The system allows users to select the books that they would like to reserve online via a
website powered by a Flask Web Server
- Users can select which library branch they would like to collect the book from

**Renewal:**
- The system allows users to select the books that they would like to renew online via a
website powered by a Flask Web Server
- Each book has a loan period of 18 days and can be renewed only once for an additional
7 days

**Tracking Service**
The tracking service runs as a thread in conjunction with the Web Server, so that every day (12AM):
- Reservations for any books that are not collected by the user within 5 days are
automatically cancelled
- There will be a fine of $0.15 per book for each day after the return date

## Running the Library Book Collection and Reservation System Locally
The Library Book Collection and Reservation System can be deployed locally on your personal computer.
### Cloning the Repository
```shell
git clone https://github.com/ET0735-DevOps-AIoT-AY2310/DCPE-2A-02-GroupB
```

### Running the Flask Web Server
Navigate to the folder in which you have just cloned, and run the following commands in **cmd**:
```shell
pip install -r requirements.txt
cd app
python app.py
```
