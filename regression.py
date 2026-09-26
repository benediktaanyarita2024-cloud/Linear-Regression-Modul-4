# Core Pkgs
import streamlit as st
import sklearn
import joblib,os
import numpy as np

# Loading Models
def load_prediction_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model

def main():
	"""Regresi Linier Sederhana"""

	st.title("Prediksi Harga Mobil")

	html_templ = """
	<div style="background-color:#726E6D;padding:10px;">
	<h3 style="color:white">Prediksi Harga Mobil Berdasarkan Ukuran Mesin Menggunakan Regresi Linier</h3>
	</div>
	"""

	st.markdown(html_templ,unsafe_allow_html=True)

	activity = ["Prediksi Harga Mobil","Apa itu Regresi?"]
	choice = st.sidebar.selectbox("Menu",activity)

# Car Price Prediction CHOICE
	if choice == 'Prediksi Harga Mobil':

		st.subheader("Prediksi Harga Mobil")

		engine = st.slider("Berapa ukuran mesin mobilnya? (cubic inch)",60,330)

		if st.button("Proses"):

			regressor = load_prediction_model("models/linear_regression_carprice.pkl")
			engine_reshaped = np.array(engine).reshape(-1,1)

			predicted_price = regressor.predict(engine_reshaped)

			st.info("Perkiraan harga mobil dengan ukuran mesin {}: ${}".format(engine,(predicted_price[0][0].round(2))))

# What is Regression CHOICE
	if choice == 'Apa itu Regresi?':

		st.subheader("Apa itu Regresi Linier?")
		st.write("Regresi linier sederhana adalah metode untuk memodelkan hubungan antara satu variabel bebas (X) "
			"dan satu variabel terikat (y) dengan sebuah garis lurus: y = b + mx.")
		st.write("Di aplikasi ini, X adalah ukuran mesin mobil dan y adalah harga mobil. "
			"Model dilatih dari dataset Car Price sehingga bisa memperkirakan harga mobil berdasarkan ukuran mesinnya.")



if __name__ == '__main__':
	main()
