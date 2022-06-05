from algo import *

def main():
	print('Selamat datang di Warung Permainan Nopal!\n')
	while True:
		print('Permainan Tersedia')
		print('      1. Tic Tac Toe')
		print('      2. Minesweeper')
		print('Lainnya. Keluar')
		pilih = int(input('Pilih Permainan : '))
		if pilih == 1:
			os.system('cls')
			mainan = TicTacToe(input('Siapa namamu : '))
			mainan.buatPapan()
			mainan.mulaiPermainan()
			mainan.__poin_user = 9999
			mainan.getPoin()
		elif pilih == 2:
			os.system('cls')
			mainan2 = Minesweeper(input('Siapa namamu : '))
			mainan2.buatPapan()
			mainan2.pilihLevel()
			mainan2.mulaiPermainan()
			mainan2.__poin_user = 9797
			mainan2.getPoin()
		else:
			print('Terima kasih telah berkunjung ke Warung Permainan Nopal!')
			time.sleep(1)
			os.system('cls')
			break

		restart = input('\nMain lagi? [Y/T] : ')
		if restart != 'Y' and restart != 'y':
			print('Terima kasih telah bermain di Warung Permainan Nopal!')
			break
		os.system('cls')

if __name__ == '__main__':
	main()