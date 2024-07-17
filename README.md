## Building a Robust Data Entry Application with Flask and SQL

### Introduction

Creating a web-based data entry application can greatly enhance data management and accessibility. In this blog post, we'll explore how to build a powerful data entry app using Flask, a lightweight web framework for Python, integrated with SQL for robust data storage. This application will support entering data into multiple fields, viewing and downloading data, executing SQL queries, and deleting records.

### Key Features

1. **Data Entry**: Users can enter data across 20 fields.
2. **View Data**: Display all entered data in a tabular format.
3. **Download Data**: Export the data as an Excel file.
4. **Execute SQL Queries**: Run custom SQL queries on the database.
5. **Delete Data**: Remove records based on the primary key.

### Technology Stack

- **Flask**: Web framework for Python.
- **Flask-SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) for Flask.
- **pandas**: Data manipulation and analysis.
- **openpyxl**: Excel file creation and manipulation.
- **HTML/CSS**: Frontend structure and styling.

### How to Run the Project

Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/horizontalformdata.git
    cd horizontalformdata
    ```

2. **Create and Activate a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install Flask Flask-SQLAlchemy pandas openpyxl
    ```

4. **Run the Application**:
    ```sh
    flask run
    ```

5. **Access the Application**:
    Open your web browser and go to `http://127.0.0.1:5000`.

### Detailed Functionalities

1. **Data Entry**:
    - The main page (`/`) allows users to enter data into 20 fields.
    - Users can add multiple rows of data without losing previous entries.

2. **View Data**:
    - The `/view` route displays all the data stored in the SQL database in a tabular format.
    - Users can download the displayed data as an Excel file.

3. **Execute SQL Queries**:
    - The `/sql` route provides an interface for executing custom SQL queries.
    - The results of the queries are displayed on the same page and can be downloaded as an Excel file.

4. **Delete Data**:
    - The `/delete` route allows users to delete a specific row based on the primary key.

### Conclusion

This project demonstrates how to create a full-featured data entry application using Flask and SQL. With a simple yet powerful interface, users can manage and manipulate data efficiently. Whether you're a developer looking to learn Flask or a professional needing a customizable data entry solution, this project provides a solid foundation.

### GitHub Repository

Check out the complete code on [GitHub](https://github.com/VeedantBrahmbhatt/horizontalformdata).

Feel free to fork the repository and customize it further to fit your specific needs. Happy coding!
