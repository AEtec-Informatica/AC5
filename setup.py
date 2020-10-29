import sqlite3

conn = sqlite3.connect ('exemplo.db')
c = conn.cursor ()

c.execute ('' 'CREATE TABLE ações
(texto de data, texto trans, texto de símbolo, quantidade real, preço real) '' ')

c.execute ("INSERT INTO stocks VALUES
('2006-01-05', 'BUY', 'RHAT', 100,35.14) ")

conn.commit ()
conn.close ()
