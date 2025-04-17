import sqlite3
db=sqlite3.connect('quest.db')
cursor=db.cursor()

s ="""

-- Создание базы данных
CREATE DATABASE LibraryDB;
USE LibraryDB;

-- Таблица авторов
CREATE TABLE Authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birth_year INT
);

-- Таблица книг
CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author_id INT,
    published_year INT,
    genre VARCHAR(50),
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- Таблица читателей
CREATE TABLE Readers (
    reader_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    registration_date DATE
);

-- Таблица выдачи книг
CREATE TABLE BorrowedBooks (
    borrow_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    reader_id INT,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (reader_id) REFERENCES Readers(reader_id)
);

"""
cursor.executescript(s)
db.commit()
db.close()