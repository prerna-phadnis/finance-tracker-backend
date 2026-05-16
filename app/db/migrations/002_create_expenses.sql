CREATE TABLE expenses (

    id SERIAL PRIMARY KEY,

    title VARCHAR(255) NOT NULL,

    amount NUMERIC(10,2) NOT NULL,

    category VARCHAR(100),

    expense_date DATE DEFAULT CURRENT_DATE,

    receipt_url TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    user_id INTEGER REFERENCES users(id)
);