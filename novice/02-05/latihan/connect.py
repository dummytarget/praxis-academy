import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123",
  database="toko_mainan"
)

if db.is_connected():
  print("Berhasil terhubung ke database")

