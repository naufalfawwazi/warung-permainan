import random, os, time

class Papan:
	def buatPapan(self):
		print('Buat Papan')
		print('1. Papan Persegi')
		print('2. Papan Kustom')
		papan = int(input('Pilih Papan : '))
		if papan == 1:
			self.baris = int(input('Jumlah baris persegi : '))
			while self.baris < 3:
				print('Jumlah baris persegi minimal 3, ulang!')
				self.baris = int(input('Jumlah baris persegi : '))
			self.kolom = self.baris
			self.data = [' ']*(self.baris*self.kolom)
			os.system('cls')
		elif papan == 2:
			self.baris = int(input('Jumlah baris : '))
			self.kolom = int(input('Jumlah kolom : '))
			while self.baris < 3 or self.kolom < 3:
				print('Jumlah baris atau kolom minimal 3, ulang!')
				self.baris = int(input('Jumlah baris : '))
				self.kolom = int(input('Jumlah kolom : '))
			self.data = [' ']*(self.baris*self.kolom)
			os.system('cls')
		else:
			print('Masukan salah!')
			time.sleep(0.5)
			os.system('cls')
			self.buatPapan()

	def buatKotak(self):
		print('FORMAT :')
		count = 1
		for i in range(self.baris):
			for j in range(self.kolom):
				if count < 10:
					print(count, end='  ')
				else:
					print(count, end=' ')
				count += 1
			print()
		print()

		count = 0
		for i in range(self.baris):
			if i == 0:
				print('+---'*self.kolom+'+')
			for j in range(self.kolom):
				if j == 0:
					print('|', end='')
				print(f' {self.data[count]} |', end='')
				count += 1
			print()
			print('+---'*self.kolom+'+')

class TicTacToe(Papan):
	def __init__(self, namaPemain):
		print(f'Hai {namaPemain}, Selamat datang di permainan Tic Tac Toe!\n')
		self.__poin_user = 0
		self.__poin_comp = 0

	def mulaiPermainan(self, giliran=0):
		self.buatKotak()
		if ' ' in self.data:
			if giliran % 2 == 0:
				print('Giliran Anda')
				kotak = int(input('Anda memilih kotak ke : '))-1
				if kotak < 0 or kotak >= len(self.data):
					print('Kotak tersebut tidak ada, ulang!')
					time.sleep(0.5)
					os.system('cls')
					self.mulaiPermainan()
				else:
					if self.data[kotak] != ' ':
						print('Kotak tersebut telah terisi, ulang!')
						time.sleep(0.5)
						os.system('cls')
						self.mulaiPermainan()
					else:
						self.data[kotak] = 'O'
						os.system('cls')
						self.mulaiPermainan(giliran+1)
			else:
				print('Giliran Komputer')
				kotak = random.randint(0, self.baris * self.kolom-1)
				while self.data[kotak] != ' ':
					kotak = random.randint(0, self.baris * self.kolom-1)
				time.sleep(0.5)
				print('Komputer memilih kotak ke :', kotak+1)
				self.data[kotak] = 'X'
				time.sleep(0.5)
				os.system('cls')
				self.mulaiPermainan(giliran+1)
		else:
			self.cekPoin()

	def cekPoin(self):
		count = 0
		self.array = []
		for i in range(self.baris):
			array2d = []
			for j in range(self.kolom):
				array2d += [self.data[count]]
				count += 1
			self.array += [array2d]

		def Horizontal(pemain, baris=self.baris, kolom=self.kolom, array=self.array):
			poin_pemain = 0
			for i in range(baris):
				t_poin = []
				for j in range(kolom):
					if array[i][j] == pemain:
						if len(t_poin) < 1:
							t_poin += [j]
						else:
							if j - t_poin[len(t_poin)-1] == 1:
								t_poin += [j]
							else:
								t_poin = [j]
					if len(t_poin) == 3:
						poin_pemain += 1
						t_poin =  [t_poin[2]]
			return poin_pemain

		def Vertikal(pemain, baris=self.baris, kolom=self.kolom, array=self.array):
			poin_pemain = 0
			for i in range(kolom):
				t_poin = []
				for j in range(baris):
					if array[j][i] == pemain:
						if len(t_poin) < 1:
							t_poin += [j]
						else:
							if j - t_poin[len(t_poin)-1] == 1:
								t_poin += [j]
							else:
								t_poin = [j]
					if len(t_poin) == 3:
						poin_pemain += 1
						t_poin =  [t_poin[2]]
			return poin_pemain

		def DiagonalKiri(pemain, baris=self.baris, kolom=self.kolom, array=self.array):
			cache = []; poin_pemain = 0
			for i in range(baris):
				for j in range(kolom):
					if array[i][j] == pemain:
						t_poin = [j]
						t_baris = i
						cache += [f'{i}{j}']
						for k in range(i+1, baris):
							for l in range(kolom):
								if array[k][l] == pemain:
									if l - t_poin[len(t_poin)-1] == 1 and k - t_baris == 1 and f'{k}{l}' not in cache:
										t_poin += [l]
										t_baris = k
										cache += [f'{k}{l}']
									if len(t_poin) == 3:
										poin_pemain += 1
										t_poin = [t_poin[2]]
			return poin_pemain

		def DiagonalKanan(pemain, baris=self.baris, kolom=self.kolom, array=self.array):
			cache = []; poin_pemain = 0
			for i in range(baris):
				for j in range(kolom-1,-1,-1):
					if array[i][j] == pemain:
						t_poin = [j]
						t_baris = i
						cache += [f'{i}{j}']
						for k in range(i+1, baris):
							for l in range(kolom-1,-1,-1):
								if array[k][l] == pemain:
									if l - t_poin[len(t_poin)-1] == -1 and k - t_baris == 1 and f'{k}{l}' not in cache:
										t_poin += [l]
										t_baris = k
										cache += [f'{k}{l}']
									if len(t_poin) == 3:
										poin_pemain += 1
										t_poin = [t_poin[2]]
			return poin_pemain

		self.__poin_user = Vertikal('O') + Horizontal('O') + DiagonalKiri('O') + DiagonalKanan('O')
		self.__poin_comp = Vertikal('X') + Horizontal('X') + DiagonalKiri('X') + DiagonalKanan('X')

	def getPoin(self):
		if self.__poin_user > self.__poin_comp:
			print('Selamat! Anda menang dan mendapatkan', self.__poin_user, 'poin!')
			print('Komputer memperoleh', self.__poin_comp, 'poin.')
		elif self.__poin_user < self.__poin_comp:
			print('Anda kalah dengan perolehan', self.__poin_user, 'poin!')
			print('Komputer memperoleh', self.__poin_comp, 'poin.')
		elif self.__poin_user == self.__poin_comp:
			print('Pertandingan seri! Anda mendapatkan', self.__poin_user, 'poin!')
			print('Komputer memperoleh', self.__poin_comp, 'poin.')

class Minesweeper(Papan):
	def __init__(self, namaPemain):
		print(f'Hai {namaPemain}, Selamat datang di permainan Minesweeper!\n')
		self.__poin_user = 0

	def pilihLevel(self):
		print('Level Tersedia')
		print('1. Mudah')
		print('2. Sulit')
		self.level = int(input('Pilih Level : '))
		if self.level != 1 and self.level != 2:
			print('Masukan salah!')
			time.sleep(0.5)
			os.system('cls')
			self.pilihLevel()
		else:
			self.bom = []
			os.system('cls')
			self.buatBom()

	def buatBom(self):
		posisi = random.randint(0,self.baris*self.kolom-1)
		if self.level == 1:
			self.bom = [posisi]
		elif self.level == 2:
			if len(self.bom) < 4:
				if posisi in self.bom:
					self.buatBom()
				else:
					self.bom += [posisi]
					self.buatBom()

	def mulaiPermainan(self, terisi=[]):
		self.buatKotak()
		lengkap = True if terisi == [i for i in range(len(self.data)) if i not in self.bom] else False
		if not lengkap:
			kotak = int(input('Pilih kotak : '))-1
			if kotak not in self.bom:
				if kotak < 0 or kotak >= len(self.data):
					print('Kotak tersebut tidak ada, ulang!')
					time.sleep(0.5)
					os.system('cls')
					self.mulaiPermainan(terisi)
				else:
					if self.data[kotak] != ' ':
						print('Kotak tersebut telah terisi, ulang!')
						time.sleep(0.5)
						os.system('cls')
						self.mulaiPermainan(terisi)
					else:
						self.data[kotak] = 'O'
						os.system('cls')
						self.mulaiPermainan(terisi+[kotak])
			else:
				for i in self.bom:
					self.data[i] = '!'
				os.system('cls')
				self.buatKotak()
				print('Anda terkena bom, permainan berakhir!')
				self.cekPoin()
		else:
			for i in self.bom:
				self.data[i] = '!'
			self.buatKotak()
			print('Selamat anda berhasil!')
			self.cekPoin()

	def cekPoin(self):
		self.__poin_user = len([i for i in self.data if i == 'O'])

	def getPoin(self):
		print('Selamat! Anda mendapatkan', self.__poin_user, 'poin!')