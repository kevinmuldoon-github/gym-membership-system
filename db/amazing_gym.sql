DROP TABLE bookings;
DROP TABLE members;
DROP TABLE activities;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    premium BOOLEAN,
    deactivated BOOLEAN
);

CREATE TABLE activities(
    id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    date DATE,
    time VARCHAR(255),
    capacity INT
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    activity_id INT REFERENCES activities(id) ON DELETE CASCADE
);