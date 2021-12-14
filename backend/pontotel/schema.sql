DROP TABLE IF EXISTS user;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  name TEXT NOT NULL,
  country TEXT NOT NULL,
  federal_state TEXT NOT NULL, 
  city TEXT NOT NULL,
  cep TEXT NOT NULL, 
  street TEXT NOT NULL, 
  residential_number TEXT NOT NULL,
  aditional_address_info TEXT, 
  cpf TEXT NOT NULL,
  pis TEXT NOT NULL
);