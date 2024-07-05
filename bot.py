import discord
# import * - adalah cara cepat untuk mengimpor semua file di perpustakaan

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan memindahkan hak istimewa
client = discord.Client(intents=intents)

# Setelah bot siap, ia akan mencetak namanya!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Saat bot menerima pesan, bot akan mengirimkan pesan di saluran yang sama!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('haii')
    elif message.content.startswith('$sampah organik'):
        await message.channel.send('Sampah organik adalah jenis sampah yang berasal dari bahan-bahan alami dan mudah terurai oleh proses alami, seperti sisa makanan, daun, ranting, dan limbah dari tumbuhan dan hewan. Sampah organik bisa diuraikan oleh mikroorganisme menjadi bahan yang lebih sederhana yang bisa digunakan kembali oleh lingkungan, misalnya sebagai kompos.')
    elif message.content.startswith('$sampah nonorganik'):
        await message.channel.send('Sampah non-organik adalah jenis sampah yang berasal dari bahan-bahan yang tidak mudah terurai secara alami oleh mikroorganisme. Sampah ini biasanya berasal dari bahan sintetis atau hasil olahan industri yang membutuhkan waktu yang sangat lama untuk terurai, atau bahkan tidak bisa terurai sama sekali.')
    elif message.content.startswith('$sampah elektronik'):
        await message.channel.send('Sampah elektronik (juga dikenal sebagai e-waste atau limbah elektronik) adalah jenis sampah yang terdiri dari perangkat elektronik yang sudah tidak digunakan atau rusak. Sampah ini mencakup berbagai jenis perangkat elektronik yang memerlukan listrik untuk beroperasi.')
    elif message.content.startswith('$makasih'):
        await message.channel.send('sama sama')
    else:
        await message.channel.send("Tidak dapat memproses perintah ini, maaf")

client.run("token")
