<h1>Steptech Flask Project</h1>

<p>This is a Flask API that provides endpoints to manage users. It allows you to view a list of users, create new
        users, and view individual user details. The application uses MySQL as the database to store user information.
</p>


    <h3>Setup and Run:</h3>
    <p></p>To set up and run the Flask application, follow these steps:</p>
    <ol>
        <li>Clone the repository<br>
            <ul><li>git clone https://github.com/your_username/your_flask_app.git</li>
            <li>cd your_flask_app</li>
        </ul></l1>
        <li>Install dependencies 
   "pip install Flask mysql-connector-python"
            
        </li>
        <li>
            <ul>
                <li>Configure the database<br>
                    db_config = {<br>
                    'host': 'your_database_host',<br>
                    'user': 'your_database_user',<br>
                    'password': 'your_database_password',<br>
                    'database': 'your_database_name'<br>
                    }</li>
                <li>Create the required table(s) in your MySQL database. You can find the database schema details in the
                    next section.</li>
            </ul>
        </li>

        <li> Run the Flask application 
            "python app.py"</li>
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


    <h3>Git Workflow and Contribution</h3>

    <p>main: The main branch that stores the stable version of the application.<br>
        develop: The development branch where new features are integrated before being merged into the main.<br>
        Feature Branches: For each new feature, bug fix, or improvement, create a new branch based on the develop branch
        and name it descriptively.</p>

    <h4>To contribute to the project, follow these steps:</h4>

    <ol>
        <li>Fork the repository on GitHub.</li>
        <li>Clone your forked repository locally:<br>
            <ul>
                <li>git clone https://github.com/your_username/your_flask_app.git</li>
                <li>cd your_flask_app</li>
            </ul>
        </li>
        <li> Create a new branch for your changes:<br>
            <ul>
                <li>git checkout -b new_feature</li>
            </ul>
        </li>
        <li> Make your changes and commit them:<br>
            <ul>
                <li>git add .</li>
                <li>git commit -m "Add new feature"</li>
            </ul>
        </li>
        <li>Push your changes to your forked repository:<br>
            <ul>
                <li>
                    git push origin new_feature</li>
            </ul>
        </li>
        <li>Create a pull request on GitHub, targeting the develop branch of the original repository.</li>

        <li>Wait for the maintainers to review your pull request. If there are any requested changes, make them in your
        branch and push the changes. The pull request will be updated automatically.</li>

    <li>Once your pull request is approved, it will be merged into the develop branch, and your contribution will
        become part of the project.</li>

        <h4 >Note: Please ensure that your changes are well-tested and follow the project's coding guidelines before
        submitting a pull request.</h4>

        <p></p>
        Insert sample data into the "users" table:<br>
        INSERT INTO users (id,name, email,role) VALUES<br>
        (1,'John Doe', 'john.doe@example.com',hr),<br>
        (2,'Jane Smith', 'jane.smith@example.com',analyst),<br>
        (3,'Michael Johnson', 'michael.johnson@example.com',sales);<br>
    </p>
    <p>
        Retrieve all users from the "users" table:<br>
        SELECT * FROM users;<br>
    </p>
</p>
        Retrieve a specific user by their ID:<br>
        SELECT * FROM users WHERE id = &lt; user_id &gt;<br>
        </p>
