user:
    - user_id
    - name
    - address
    - date of birth
    - reservations
    - tickets

profile:
    - user_id
    - picture

ticket:
    - ticket_id
    - type -> train/bus/flight
    - departure time
    - transport number
    - train/bus/flight name
    - boarding point
    - destination point
    - ticket fare
    - date of travel.

reservation:
    - reservation_id
    - type -> train/bus/flight
    - departure time
    - transport number
    - train/bus/flight name
    - boarding point
    - destination point
    - no. of seats in first class
    - fare per ticket/bus/flight
    - no. of seats in second class
    - fare per ticket
    - date of travel

transportation:
    - transport_id
    - type -> train/bus/flight