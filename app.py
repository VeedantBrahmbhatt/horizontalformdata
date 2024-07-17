from flask import Flask, render_template, request, redirect, url_for, session, send_file, flash
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from io import BytesIO
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

class DataEntry(db.Model):
    # __tablename__ ='my_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    col1 = db.Column(db.String(100))
    col2 = db.Column(db.String(100))
    col3 = db.Column(db.String(100))
    col4 = db.Column(db.String(100))
    col5 = db.Column(db.String(100))
    col6 = db.Column(db.String(100))
    col7 = db.Column(db.String(100))
    col8 = db.Column(db.String(100))
    col9 = db.Column(db.String(100))
    col10 = db.Column(db.String(100))
    col11 = db.Column(db.String(100))
    col12 = db.Column(db.String(100))
    col13 = db.Column(db.String(100))
    col14 = db.Column(db.String(100))
    col15 = db.Column(db.String(100))
    col16 = db.Column(db.String(100))
    col17 = db.Column(db.String(100))
    col18 = db.Column(db.String(100))
    col19 = db.Column(db.String(100))
    col20 = db.Column(db.String(100))

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if 'data' not in session:
#         session['data'] = []

#     if request.method == 'POST':
#         # Collect form data and add to session
#         row = [request.form.get(f'col{i}') for i in range(1, 21)]
#         session['data'].append(row)
#         session.modified = True
#         if 'submit' in request.form:
#             df = pd.DataFrame(session['data'], columns=[f'col{i}' for i in range(1, 21)])
#             df.to_sql('data_entry', con=db.engine, if_exists='append', index=False)
#             session.pop('data', None)
#             return redirect(url_for('index'))

#     return render_template('index.html')
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'data' not in session:
        session['data'] = []

    if request.method == 'POST':
        row = [request.form.get(f'col{i}_{len(session["data"])}') for i in range(1, 21)]
        session['data'].append(row)
        session.modified = True
        if 'submit' in request.form:
            df = pd.DataFrame(session['data'], columns=[f'col{i}' for i in range(1, 21)])
            df.to_sql('data_entry', con=db.engine, if_exists='append', index=False)
            session.pop('data', None)
            return redirect(url_for('index'))

    return render_template('index.html', data=session['data'])
@app.route('/view')
def view():
    data = pd.read_sql_table('data_entry', con=db.engine)
    return render_template('view.html', data=data.to_html())

@app.route('/download')
def download():
    data = pd.read_sql_table('data_entry', con=db.engine)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        data.to_excel(writer, index=False)
    output.seek(0)
    return send_file(output, download_name='data.xlsx', as_attachment=True)

@app.route('/sql', methods=['GET', 'POST'])
# def sql():
#     result = None
#     query = ""
#     if request.method == 'POST':
#         query = request.form.get('query')
#         try:
#             with db.engine.connect() as connection:
#                 result_proxy = connection.execute(text(query))
#                 result = result_proxy.fetchall()
#                 columns = result_proxy.keys()
#                 df = pd.DataFrame(result, columns=columns)
#                 output = BytesIO()
#                 with pd.ExcelWriter(output, engine='openpyxl') as writer:
#                     df.to_excel(writer, index=False)
#                 output.seek(0)
#                 return render_template('sql.html', result=result, query=query, download=True, file=output.getvalue())
#         except Exception as e:
#             result = str(e)
#     return render_template('sql.html', result=result, query=query, download=False)
def sql():
    result = None
    query = ""
    error = None
    file_content = None

    if request.method == 'POST':
        query = request.form.get('query')
        try:
            with db.engine.connect() as connection:
                result_proxy = connection.execute(text(query))
                result = [dict(row.items()) for row in result_proxy]
                if result:
                    columns = result_proxy.keys()
                    df = pd.DataFrame(result, columns=columns)
                    output = BytesIO()
                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                        df.to_excel(writer, index=False)
                    output.seek(0)
                    file_content = output.getvalue()
        except Exception as e:
            error = str(e)

    return render_template('sql.html', result=result, query=query, error=error, file=file_content)

@app.route('/sql_download', methods=['POST'])
def sql_download():
    file_content = request.form.get('file')
    output = BytesIO(file_content.encode('latin1'))
    return send_file(output, download_name='sql_result.xlsx', as_attachment=True)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        primary_key = request.form.get('primary_key')
        if primary_key:
            try:
                row_to_delete = DataEntry.query.get(primary_key)
                if row_to_delete:
                    db.session.delete(row_to_delete)
                    db.session.commit()
                    flash('Row deleted successfully.', 'success')
                else:
                    flash('Row not found.', 'danger')
            except Exception as e:
                flash(str(e), 'danger')
        return redirect(url_for('delete'))
    return render_template('delete.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
