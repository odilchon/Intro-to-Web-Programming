CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    full_name TEXT NOT NULL,
    phone TEXT
);

CREATE TABLE invoices (
    invoice_id INT PRIMARY KEY,
    client_id INT,
    invoice_total NUMERIC(10,2)
);

INSERT INTO clients VALUES
(1, 'Michael Reed', '555-1234'),
(2, 'Olivia Parker', '555-5678'),
(3, 'Daniel Young', '555-9012'),
(4, 'Sophia Turner', '555-3456');

INSERT INTO invoices VALUES
(201, 1, 500.00),
(202, 2, 750.00),
(203, NULL, 300.00),
(204, 4, 450.00);

CREATE TABLE workers (
    worker_id INT PRIMARY KEY,
    worker_name TEXT NOT NULL,
    unit_id INT
);

CREATE TABLE units (
    unit_id INT PRIMARY KEY,
    unit_name TEXT NOT NULL
);

INSERT INTO workers VALUES
(1, 'Ethan Cole', 100),
(2, 'Mia Scott', 200),
(3, 'Lucas Hill', NULL);

INSERT INTO units VALUES
(100, 'Operations'),
(200, 'Technology'),
(300, 'Logistics');

CREATE TABLE learners (
    learner_id INT PRIMARY KEY,
    learner_name TEXT NOT NULL
);

CREATE TABLE subjects (
    subject_id INT PRIMARY KEY,
    subject_title TEXT NOT NULL
);

CREATE TABLE registrations (
    registration_id INT PRIMARY KEY,
    learner_id INT,
    subject_id INT
);

INSERT INTO learners VALUES
(1, 'Noah Adams'),
(2, 'Lily Moore'),
(3, 'Henry Clark');

INSERT INTO subjects VALUES
(501, 'Physics'),
(502, 'Chemistry'),
(503, 'Biology');

INSERT INTO registrations VALUES
(1, 1, 501),
(2, 2, 502);

SELECT cl.full_name, i.invoice_id, i.invoice_total
FROM clients cl
INNER JOIN invoices i
ON cl.client_id = i.client_id;

SELECT w.worker_name, u.unit_name
FROM workers w
INNER JOIN units u
ON w.unit_id = u.unit_id;

SELECT l.learner_name, s.subject_title
FROM learners l
INNER JOIN registrations r
ON l.learner_id = r.learner_id
INNER JOIN subjects s
ON r.subject_id = s.subject_id;

SELECT cl.full_name, i.invoice_id, i.invoice_total
FROM clients cl
LEFT JOIN invoices i
ON cl.client_id = i.client_id;

SELECT w.worker_name, u.unit_name
FROM workers w
LEFT JOIN units u
ON w.unit_id = u.unit_id;

SELECT l.learner_name, s.subject_title
FROM learners l
LEFT JOIN registrations r
ON l.learner_id = r.learner_id
LEFT JOIN subjects s
ON r.subject_id = s.subject_id;

SELECT i.invoice_id, i.invoice_total, cl.full_name
FROM clients cl
RIGHT JOIN invoices i
ON cl.client_id = i.client_id;

SELECT w.worker_name, u.unit_name
FROM workers w
RIGHT JOIN units u
ON w.unit_id = u.unit_id;

SELECT l.learner_name, s.subject_title
FROM learners l
RIGHT JOIN registrations r
ON l.learner_id = r.learner_id
RIGHT JOIN subjects s
ON r.subject_id = s.subject_id;

SELECT cl.full_name, i.invoice_id, i.invoice_total
FROM clients cl
FULL JOIN invoices i
ON cl.client_id = i.client_id;

SELECT w.worker_name, w.unit_id, u.unit_name
FROM workers w
FULL JOIN units u
ON w.unit_id = u.unit_id;

SELECT l.learner_name, s.subject_title
FROM learners l
FULL JOIN registrations r
ON l.learner_id = r.learner_id
FULL JOIN subjects s
ON r.subject_id = s.subject_id;
