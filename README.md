# Flexi Shift- Backend
**Project By:** Susie Gordon


## Descripton
Flexi Shift is an app that conveniently helps employers and employees schedule individual work shifts. Users can view their manually added list of shifts and the calendar month of choice displaying all other reserved shifts added by supervisors, colleagues, or coworkers. 
</br>

## Link
[**Github**](https://github.com/choisus08/flexi_shift_backend)
[**Deployment**](https://flexi-shift-backend.onrender.com/shifts/)
</br>

## Technologies Used
- Django
- Postman
- Python
</br>

## Backend Endpoints

| ENDPOINT | METHOD | PURPOSE |
|----------|--------|---------|
| /shift | GET | return list of shift entries|
| /shift/:id | DELETE | delete a shift entry from database |
| /shift/:id | PUT | receive info & update shift entry in database |
| /shift | POST | receive info from new form & create new shift entry in database |
| /shift/:id | GET | render page with the shift entry|
</br>

## ERD

``` mermaid
erDiagram
    USER {
        id primaryKey
        username string 
        password string
    }
    USER ||--|{ SHIFTS : Create
    SHIFTS {
        Name foreignKey
        Position string
        Date string 
        StartTime string 
        EndTime string 
    }
```