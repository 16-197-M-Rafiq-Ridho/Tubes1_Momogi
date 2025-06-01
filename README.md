
# <h1 align="center">TUBES STIMA</h1>

##  Deskripsi

<p align="justify">
  Algoritma greedy yang digunakan oleh bot ini mengambil keputusan terbaik di setiap langkah berdasarkan kondisi saat itu, tanpa memperhitungkan dampak jangka panjang. Bot secara konsisten memilih diamond terdekat sebagai target utama dan bergerak langsung menuju posisinya untuk mengoptimalkan pengumpulan diamond secara cepat dan efisien. Jika inventory bot sudah penuh, bot segera kembali ke base untuk menyimpan diamond dan bersiap mengumpulkan diamond lagi. Dalam beberapa situasi, bot juga memanfaatkan fitur teleport jika terbukti dapat mempersingkat jarak menuju target seperti diamond atau base, demi meningkatkan efisiensi gerakan. Saat bot menentukan arah gerakan, bot memastikan bahwa langkah yang dipilih valid dan sesuai aturan permainan. Jika langkah pertama tidak memungkinkan, bot akan mencari alternatif gerakan lain. Pemilihan langkah dilakukan berdasarkan perhitungan jarak yang bertujuan untuk selalu mendekat ke target, menjadikan keputusan bersifat cepat dan lokal. Namun, bot tidak mempertimbangkan strategi jangka panjang seperti memilih diamond yang lebih bernilai tetapi lebih jauh, sehingga fokus utamanya adalah pada keuntungan langsung di setiap langkah.

</p>

## Cara menjalankan bot
<p>1. Pastikan sudah mendownload python dan jika belum installer di https://www.python.org/
      dan centang opsi “Add Python to PATH” saat instalasi</p>
<p>2. Dowloan file zip game engine (https://github.com/haziqam/tubes1-IF2211-game-engine/releases/tag/v1.1.0) atau dapat mendownload panduan untuk lebih lengkapnya</p>

<p>3. Download file bot starter pack (https://github.com/16-197-M-Rafiq-Ridho/Tubes-Stima)</p>

<p>4. download Node.js (https://nodejs.org/en) dan docker (https://www.docker.com/products/docker-desktop/)</p>

## Buka CMD lalu
1. Masuk direktori game engine
   ```
   cd ./tubes1-IF2110-game-engine
   ```
3. Install dependencies

   ```
   yarn
   ```

4. Setup default environment variables

   For windows

   ```
   ./scripts/copy-env.bat
   ```

   For Linux /(possibly) macOS

   ```
   chmod +x ./scripts/copy-env.sh
   ./scripts/copy-env.sh
   ```

5. Setup local database

   ```
   docker compose up -d database
   ```

   For windows

   ```
   ./scripts/setup-db-prisma.bat
   ```

   For Linux /(possibly) macOS

   ```
   chmod +x ./scripts/setup-db-prisma.sh
   ./scripts/setup-db-prisma.sh
   ```

6. Build

   ```
   npm run build
   ```

## How to Run 💻

```
npm run start
```

## Menjalankan bot
1. masuk directory bot starterpack
   ```
   cd ./tubes1-IF2211-bot-starter-pack-1.0.1
   ```
2. Install dependencies menggunakan pip
   ```
   pip install -r requirements.txt
   ```
3. Run
  Untuk menjalankan satu bot (pada contoh ini, kita menjalankan satu bot dengan logic yang terdapat pada file game/logic/random.py)
   ```
   python main.py --logic Random --email=your_email@example.com --name=your_name --password=your_password --team etimo
   ```
   Untuk menjalankan beberapa bot sekaligus
   untuk windows
   ```
   run-bots.bat
   ```
   untuk linux
   ```
   ./run-bots.sh
   ```

<p>and Enjjooyyyy.........walaupun bekum optimal</p>


## Contributors

| Nama                        | NIM       | Link Github                                                                            |
| ----------------------------| --------- | -------------------------------------------------------------------------------------- |
| Maxavier Girvanus Manurung  | 123140191 | [@01-191-MaxavierGirvanusManurung](https://github.com/01-191-MaxavierGirvanusManurung) |
| Gilang Surya Agung          | 123140187 | [@15-187-GilangSuryaAgung](https://github.com/15-187-GilangSuryaAgung)                 |
| Muhammad Rafiq Ridho        | 123140197 | [@16-197-M-Rafiq-Ridho](https://github.com/16-197-M-Rafiq-Ridho)                       |

