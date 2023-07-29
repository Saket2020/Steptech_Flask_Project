<h1>Steptech Flask Project</h1>

<p>This is a Flask API that provides endpoints to manage users. It allows you to view a list of users, create new users, and view individual user details. The application uses MySQL as the database to store user information.</p>


<h3>Setup and Run:</h3>
<p></p>To set up and run the Flask application, follow these steps:</p>
<ol>
           <li>Clone the repository<br>
           git clone https://github.com/your_username/your_flask_app.git<br>
           cd your_flask_app<br>
           </l1>
<li>Install dependencies<br>
          pip install Flask mysql-connector-python
</li>
<li>
           <ol><li>Configure the database<br>
          db_config = {<br>
    'host': 'your_database_host',<br>
    'user': 'your_database_user',<br>
    'password': 'your_database_password',<br>
    'database': 'your_database_name'<br>
  }<br></li>
  <li></li>Create the required table(s) in your MySQL database. You can find the database schema details in the next section.</li>
           </ol></li>

  <li> Run the Flask application<br>
             python app.py</li>
<li> Access the application in your web browser at http://localhost:5000</li>
</ol>
<p>The application uses a simple table named users to store user information. The schema is as follows:</p>
<table>
                  <tr>
                         <th>Field</th>
                         <th>Type</th>
                         <th>Key</th>
                  </tr>  
                  <tr>
                         <td>id</td>
                         <td>INT</td>
                         <td>PK</td>
                  </tr>  
                  <tr>
                         <td>name</td>
                         <td>VARCHAR(100)</td>
                         <td></td>
                  </tr> 
                  <tr>
                         <td>email</td>
                         <td>VARCHAR(100)</td>
                         <td></td>
                  </tr> 
                  <tr>
                         <td>role</td>
                         <td>VARCHAR(100)</td>
                         <td></td>
                  </tr> 
</table>


Git Workflow and Contribution

main: The main branch that stores the stable version of the application.
develop: The development branch where new features are integrated before being merged into the main.
Feature Branches: For each new feature, bug fix, or improvement, create a new branch based on the develop branch and name it descriptively.

To contribute to the project, follow these steps:

1-> Fork the repository on GitHub.
2-> Clone your forked repository locally:
           git clone https://github.com/your_username/your_flask_app.git
           cd your_flask_app
3-> Create a new branch for your changes:
           git checkout -b new_feature
4->  Make your changes and commit them:
            git add .
            git commit -m "Add new feature"
5->Push your changes to your forked repository:
          git push origin new_feature
6->Create a pull request on GitHub, targeting the develop branch of the original repository.

7->Wait for the maintainers to review your pull request. If there are any requested changes, make them in your branch and push the changes. The pull request will be updated automatically.

8->Once your pull request is approved, it will be merged into the develop branch, and your contribution will become part of the project.



Note: Please ensure that your changes are well-tested and follow the project's coding guidelines before submitting a pull request.



Insert sample data into the "users" table:
 INSERT INTO users (id,name, email,role) VALUES
  (1,'John Doe', 'john.doe@example.com',hr),
  (2,'Jane Smith', 'jane.smith@example.com',analyst),
  (3,'Michael Johnson', 'michael.johnson@example.com',sales);

  Retrieve all users from the "users" table:
     SELECT * FROM users;

Retrieve a specific user by their ID:
      SELECT * FROM users WHERE id = <user_id>;






