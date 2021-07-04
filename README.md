*to be moved to wiki*

# Overview
- June 16th, 2020 project
- a reservation system, applicable to railways, buses, flight
- 0616_merakcyborg_oop-eip-4

Features:

`Administrator mode`: 
- There are two modes in this project – the administrator mode and the user mode
    - Create Users from the Admin mode. 
    - Once users are created, the same user is usable again and again, and they will be stored in separate files.

- The operations related to both these modes are quite similar in this railway/bus/flight reservation system project in. 
    - In Admin mode:
        - create detail database
        - add details
        - display details
        - perform user management functions
        - and display passenger details.

`User mode`: 
- As aforementioned,
    - User need to go to the administrator mode and create users. 
    - After that, these users are usable as we wish, and the information related to them will be recorded in separate files.
    - In the user mode:
        - create id database
        - add detail
        - and display details.

`Train and Reservation` details:
- In this railway reservation system project:
    - Users can get both the train/bus/flight details and the train/bus/flight reservation details. 
    - The details to be provided for train/bus/flight are:
        - train/bus/flight no.
        - train/bus/flight name
        - boarding point
        - destination point
        - no. of seats in first class
        - and fare per ticket/bus/flight
        - no. of seats in second class
        - and fare per ticket
        - and date of travel.

    - In case of reservation details, the information to be provided are:
        - train no.
        - train name
        - boarding point
        - destination point
        - no. of seats required
            - additional information 
                - passenger name
                - and passenger age are to be provided
        - seat class specification
        - date of reservation
        - passenger category:
            - military
            - senior citizen
            - children and none 
        - and amount to be paid.

`Cancel reservation`:
- It is somewhat similar to the feature mentioned above.
- This feature requires the date of cancellation in this railway reservation system project.
- Then cancellation details can be displayed; 
    - the details here include:
        - train no.
        - train name
        - boarding point
        - destination point
        - passenger class
        - no. of seats to be cancelled
        - passenger name and age
        - date of cancellation
        - and the amount to be collected back.

`Password`: 
- This railway/bus/flight reservation system project in requires the administrator password to access the admin mode.
- The password is “to be decided”. If you enter the wrong password, it displays the message – “You are not permitted to login.”

### Progress
- Create main menu UI(terminal) class Paparan
    - Scaffold -> `DONE`
- Basic DB (without using SQL or any common solution) -> `WIP`
    - Connect admin to db -> `WIP`

### Microservices
    - Using hasura combinations with cubejs for data modelling
    - react combined with antd for graph