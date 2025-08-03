from flask import Flask, render_template
import pymysql

app = Flask(__name__)  # WAJIB ADA SEBELUM @app.route()

@app.route('/')
def index():
    try:
        conn = pymysql.connect(
            host='eccomerce-db.cz0kaw2y8v5e.ap-southeast-1.rds.amazonaws.com',
            user='admin',
            password='Ecommerce123!',
            db='produk'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT nama, harga, gambar_url FROM produk")
        data = cursor.fetchall()
        conn.close()
        return render_template('index.html', produk=data)
    except Exception as e:
        return f"<h1>INTERNAL ERROR</h1><pre>{e}</pre>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
