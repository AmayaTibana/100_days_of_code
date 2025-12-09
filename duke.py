-- Create sample table
CREATE TABLE users (
  id INTEGER PRIMARY KEY, 
  name TEXT,
  email TEXT
);

-- Insert some data
INSERT INTO users VALUES 
  (1, 'John', 'john@email.com'),
  (2, 'Mary', 'mary@email.com'), 
  (3, 'Robert', 'robert@email.com'),
  (4, 'Laura', 'laura@email.com');

-- Basic select query
SELECT name, email
FROM users;