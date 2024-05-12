// Require the mysql module
import mysql from "mysql"

// Create a connection to the MySQL database
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'reapercreeper399',
    database: 'hello'
});

// Connect to the database
connection.connect((err) => {
    if (err) {
        console.error('Error connecting to MySQL database: ' + err.stack);
        return;
    }
    console.log('Connected to MySQL database as id ' + connection.threadId);
});

// Execute a sample SQL query
connection.query('SELECT * FROM student', (err, results, fields) => {
    if (err) {
        console.error('Error executing query: ' + err.stack);
        return;
    }
    console.log('Query results:', results[0]["name"]);
});

// Close the database connection
connection.end();