import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# load data
used_car_df = pd.read_csv("used_car.csv")

# sidebar
with st.sidebar:
    st.image("https://img.freepik.com/free-vector/modern-truck-city_1284-40676.jpg?ga=GA1.1.862628023.1727632898&semt=ais_hybrid")
    st.write("""
        # Proyek Analisis Data: Used Car Dataset🚘
        - Nama: Muthia Nashiroh Ramadhani
        - Email: muthianashiroh@gmail.com

    """)

# Sidebar untuk filter
st.sidebar.header('Filter Data')

# Filter berdasarkan Merek Mobil
selected_brand = st.sidebar.selectbox('Pilih Merek Mobil', used_car_df['Brand'].unique())

# Filter berdasarkan Jenis Bahan Bakar
selected_fuel_type = st.sidebar.selectbox('Pilih Jenis Bahan Bakar', used_car_df['FuelType'].unique())

# Filter berdasarkan Transmisi
selected_transmission = st.sidebar.selectbox('Pilih Transmisi', used_car_df['Transmission'].unique())

# Filter berdasarkan Tahun Produksi
selected_year = st.sidebar.selectbox('Pilih Tahun', used_car_df['Year'].unique())

# Menyaring data berdasarkan filter
filtered_df = used_car_df[
    (used_car_df['Brand'] == selected_brand) &
    (used_car_df['FuelType'] == selected_fuel_type) &
    (used_car_df['Transmission'] == selected_transmission) &
    (used_car_df['Year'] == selected_year)
]

# Header Dashboard 
st.header('🚘Dashboard Data Mobil Bekas🚘')
st.write(filtered_df)

# Pertanyaan 1 - Berapa jumlah varian model untuk merek Toyota dan bagaimana hubungannya dengan harga yang ditawarkan?
st.subheader("Daftar model dan harga rata-rata merek Toyota🚘💰")
brand_name = 'Toyota'
brand_data = used_car_df[used_car_df['Brand'] == brand_name]
brand_model_counts = brand_data['model'].value_counts()
brand_model_avg_price = brand_data.groupby('model')['AskPrice'].mean()

fig, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x=brand_model_counts.index, y=brand_model_counts.values, palette='viridis', ax=ax1)
ax1.set_xlabel('Model')
ax1.set_ylabel('Jumlah Mobil')
ax1.set_title(f'Jumlah Mobil {brand_name} berdasarkan Model dan Harga Rata-rata')

ax2 = ax1.twinx()
sns.lineplot(x=brand_model_avg_price.index, y=brand_model_avg_price.values, marker='o', ax=ax2, color='red', label='Harga Rata-rata')
ax2.set_ylabel('Harga Rata-rata (₹)')
ax1.tick_params(axis='x', rotation=90)
ax1.legend(labelspacing=1.2)
ax2.legend(labelspacing=1.2)

st.pyplot(fig)
with st.expander("Conclusion📝"):
     st.write(
        """Dari hasil visualisasi data, jumlah varian model untuk merek Toyota sebanyak 19 model. 
        Hubungan antara jumlah varian model dengan harga yang ditawarkan menunjukkan bahwa model dengan jumlah mobil lebih banyak, 
        seperti Innova Crysta dan Fortuner, cenderung memiliki harga rata-rata yang lebih rendah. 
        Sebaliknya, model dengan jumlah mobil yang lebih sedikit, seperti Land Cruiser, memiliki harga rata-rata yang lebih tinggi.
        """  
    )

# Pertanyaan 2 - Merek mobil mana yang memiliki harga rata-rata tertinggi?
st.subheader("Merek Mobil dengan Harga Rata-Rata Tertinggi📈")
average_price_per_brand = used_car_df.groupby('Brand')['AskPrice'].mean().sort_values(ascending=False).head(10).reset_index()
plt.figure(figsize=(12, 8))
sns.barplot(x='AskPrice', y='Brand', data=average_price_per_brand, palette='viridis')
plt.title('10 Merek Mobil dengan Harga Rata-rata Tertinggi', fontsize=16)
plt.xlabel('Harga Rata-rata (₹)', fontsize=12)
plt.ylabel('Merek Mobil', fontsize=12)

st.pyplot(plt)
with st.expander("Conclusion📝"):
     st.write(
        """Dari hasil visualisasi data, Aston Martin memiliki harga rata-rata tertinggi dibandingkan merek-merek mobil lainnya seperti 
        Rolls-Royce, Bentley, Maserati, Porsche, Lexus, Land Rover, Mercedes-Benz, BMW, dan Mini.
        """  
    )

# Pertanyaan 3 - Bagaimana distribusi jenis bahan bakar yang digunakan?
st.subheader("Distribusi jenis bahan bakar⛽")
fuel_counts = used_car_df['FuelType'].value_counts()
plt.figure(figsize=(10, 7))
colors = sns.color_palette("coolwarm", len(fuel_counts))
explode = [0.03] * len(fuel_counts)

plt.pie(fuel_counts,
        labels=fuel_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        explode=explode,
        wedgeprops={'edgecolor': 'black', 'linewidth': 0.2, 'linestyle': 'solid'},
        textprops={'fontsize': 12, 'color': 'black'})
plt.title('Distribusi Jenis Bahan Bakar pada Mobil', fontsize=14)
plt.axis('equal')

st.pyplot(plt)
with st.expander("Conclusion📝"):
     st.write(
        """Dari hasil visualisasi data, Diesel adalah jenis bahan bakar yang paling banyak digunakan dengan persentase sebesar 39.8%. 
        Petrol berada di urutan kedua dengan persentase yang hampir sama, yaitu 39.7%. 
        Sementara itu, Hybrid/CNG merupakan jenis bahan bakar yang paling sedikit digunakan dengan persentase sebesar 20.5%.
        Secara keseluruhan, Diesel dan Petrol mendominasi penggunaan bahan bakar dengan persentase yang hampir seimbang, 
        sementara penggunaan Hybrid/CNG masih relatif rendah.
        """  
    )

# Pertanyaan 4 - Apakah mobil dengan transmisi otomatis lebih mahal dibandingkan transmisi manual?
st.subheader("Harga rata-rata berdasarkan transmisi🛞")
transmission_avg_price = used_car_df.groupby('Transmission')['AskPrice'].mean().reset_index()
plt.figure(figsize=(8, 6))
sns.barplot(data=transmission_avg_price, x='Transmission', y='AskPrice', palette='coolwarm')
plt.title('Harga Rata-Rata Berdasarkan Transmisi', fontsize=14)
plt.xlabel('Jenis Transmisi', fontsize=12)
plt.ylabel('Harga Rata-Rata (₹)', fontsize=12)

st.pyplot(plt)
with st.expander("Conclusion📝"):
     st.write(
        """Dari hasil visualisasi data, dapat disimpulkan bahwa mobil dengan transmisi otomatis cenderung memiliki harga yang lebih tinggi dibandingkan dengan mobil dengan transmisi manual. 
        Grafik menunjukkan bahwa rata-rata harga mobil dengan transmisi otomatis mencapai sekitar 1,5 juta INR, sementara rata-rata harga mobil dengan transmisi manual hanya sekitar 0,6 juta INR.
        """  
    )

# Pertanyaan 5 - Tahun berapa mobil paling banyak dan paling sedikit diproduksi?
st.subheader("Jumlah mobil per tahun produksi📊")
car_production_by_year = used_car_df['Year'].value_counts().sort_index()
max_year = car_production_by_year.idxmax()
min_year = car_production_by_year.idxmin()
max_count = car_production_by_year.max()
min_count = car_production_by_year.min()

plt.figure(figsize=(12, 6))
sns.barplot(x=car_production_by_year.index, y=car_production_by_year.values, palette='viridis')

plt.axvline(x=car_production_by_year.index.get_loc(max_year), color='red', linestyle='--', label=f'Most cars: {max_year} ({max_count})')
plt.axvline(x=car_production_by_year.index.get_loc(min_year), color='blue', linestyle='--', label=f'Fewest cars: {min_year} ({min_count})')

plt.title('Distribusi Jumlah Mobil Berdasarkan Tahun Produksi')
plt.xlabel('Tahun Produksi')
plt.ylabel('Jumlah Mobil')
plt.legend()
plt.xticks(rotation=45)

st.pyplot(plt)
with st.expander("Conclusion📝"):
     st.write(
        """Dari hasil visualisasi data, mobil paling banyak diproduksi pada tahun 2017, dengan jumlah produksi mencapai 954 mobil. 
        Sedangkan, mobil paling sedikit diproduksi pada tahun 1986, dengan hanya 1 mobil yang diproduksi pada tahun tersebut. 
        Hal ini menunjukkan adanya fluktuasi signifikan dalam jumlah produksi mobil selama periode waktu yang ditinjau.
        """  
    )

# Pertanyaan 6 - Berapa rata-rata usia mobil dan apakah mempengaruhi harganya?
st.subheader("Usia mobil dan harga berdasarkan usia")
fig, ax = plt.subplots(1, 2, figsize=(15, 6))
sns.histplot(used_car_df['Age'], bins=20, kde=True, color='skyblue', ax=ax[0])
ax[0].axvline(used_car_df['Age'].mean(), color='red', linestyle='--', label=f'Mean Age: {used_car_df["Age"].mean():.2f} years')
ax[0].set_title('Distribusi Usia Mobil')
ax[0].set_xlabel('Usia Mobil (Tahun)')
ax[0].set_ylabel('Frekuensi')
ax[0].legend()

sns.boxplot(x=used_car_df['Age'], y=used_car_df['AskPrice'], palette='coolwarm', ax=ax[1])
ax[1].set_title('Harga Mobil Berdasarkan Usia')
ax[1].set_xlabel('Usia Mobil (Tahun)')
ax[1].set_ylabel('Harga Jual (₹)')

plt.tight_layout()
st.pyplot(fig)
with st.expander("Conclusion📝"):
     st.write(
        """Dari hasil visualisasi data, rata-rata usia mobil adalah sekitar 7 tahun, dengan puncak distribusi usia mobil berada pada rentang usia 5-10 tahun. 
        Berdasarkan analisis harga, mobil dengan usia 0-10 tahun cenderung memiliki harga yang lebih tinggi, 
        sementara mobil yang lebih tua biasanya memiliki harga yang lebih rendah, 
        yang menunjukkan bahwa usia mobil mempengaruhi harga yang ditawarkan.
        """  
    )