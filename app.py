from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db_connection

app = Flask(__name__)

app.secret_key = "equipment_management_secret"


# HOME PAGE - DISPLAY ALL EQUIPMENT
@app.route("/")
def index():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM equipment ORDER BY id")

    equipment_list = cursor.fetchall()

    # DASHBOARD SUMMARY
    total_equipment = len(equipment_list)

    available_equipment = sum(
        1 for item in equipment_list
        if item["status"] == "Available"
    )

    borrowed_equipment = sum(
        1 for item in equipment_list
        if item["status"] == "Borrowed"
    )

    cursor.close()
    connection.close()

    return render_template(
        "index.html",
        equipment=equipment_list,
        total_equipment=total_equipment,
        available_equipment=available_equipment,
        borrowed_equipment=borrowed_equipment
    )

# ADD NEW EQUIPMENT
@app.route("/add", methods=["GET", "POST"])
def add_equipment():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()

        # INPUT VALIDATION

        if not name:
            flash("Equipment name cannot be empty!")
            return redirect(url_for("add_equipment"))

        if not category:
            flash("Equipment category cannot be empty!")
            return redirect(url_for("add_equipment"))

        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO equipment (name, category, status, borrower)
        VALUES (%s, %s, %s, %s)
        """

        values = (name, category, "Available", None)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        flash("Equipment added successfully!")

        return redirect(url_for("index"))

    return render_template("add_equipment.html")

# BORROW EQUIPMENT
@app.route("/borrow/<int:id>", methods=["POST"])
def borrow_equipment(id):

    borrower = request.form.get("borrower", "").strip()

    # INPUT VALIDATION

    if not borrower:
        flash("Borrower name cannot be empty!")
        return redirect(url_for("index"))

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT status FROM equipment WHERE id = %s",
        (id,)
    )

    result = cursor.fetchone()

    if result and result[0] == "Available":

        cursor.execute(
            """
            UPDATE equipment
            SET status = 'Borrowed', borrower = %s
            WHERE id = %s
            """,
            (borrower, id)
        )

        connection.commit()

        flash("Equipment borrowed successfully!")

    else:
        flash("Equipment is not available!")

    cursor.close()
    connection.close()

    return redirect(url_for("index"))


# RETURN EQUIPMENT
@app.route("/return/<int:id>", methods=["POST"])
def return_equipment(id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE equipment
        SET status = 'Available', borrower = NULL
        WHERE id = %s AND status = 'Borrowed'
        """,
        (id,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        flash("Equipment returned successfully!")
    else:
        flash("Equipment could not be returned.")

    cursor.close()
    connection.close()

    return redirect(url_for("index"))


# SEARCH EQUIPMENT
@app.route("/search", methods=["GET", "POST"])
def search_equipment():

    equipment_list = []
    search_query = ""

    if request.method == "POST":

        search_query = request.form["search"]

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT * FROM equipment
            WHERE name LIKE %s OR category LIKE %s
            ORDER BY id
            """,
            (f"%{search_query}%", f"%{search_query}%")
        )

        equipment_list = cursor.fetchall()

        cursor.close()
        connection.close()

    return render_template(
        "search.html",
        equipment=equipment_list,
        search_query=search_query
    )

# EDIT EQUIPMENT
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_equipment(id):

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()

        if not name or not category:
            flash("Please fill in all fields!")
            cursor.close()
            connection.close()
            return redirect(url_for("edit_equipment", id=id))

        cursor.execute(
            "UPDATE equipment SET name = %s, category = %s WHERE id = %s",
            (name, category, id)
        )

        connection.commit()

        flash("Equipment updated successfully!")

        cursor.close()
        connection.close()

        return redirect(url_for("index"))

    cursor.execute(
        "SELECT * FROM equipment WHERE id = %s",
        (id,)
    )

    equipment = cursor.fetchone()

    cursor.close()
    connection.close()

    if equipment is None:
        flash("Equipment not found!")
        return redirect(url_for("index"))

    return render_template("edit_equipment.html", equipment=equipment)

# DELETE EQUIPMENT
@app.route("/delete/<int:id>", methods=["POST"])
def delete_equipment(id):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM equipment WHERE id = %s",
        (id,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        flash("Equipment deleted successfully!")
    else:
        flash("Equipment not found!")

    cursor.close()
    connection.close()

    return redirect(url_for("index"))

# RUN FLASK APPLICATION
if __name__ == "__main__":
    app.run(debug=True)