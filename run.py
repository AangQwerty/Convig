#usr/bin/env python3 
#coding=utf-8

# Code © Moch Aang Ardiansyah XD. | Open Source Code
# Tools for get & convert cookies Instagram
# Github.com/AangQwerty/Convig

import os, sys

H = "\x1b[0;32m"
P = "\x1b[0;37m"

class Convert:

	def __init__(self):
		self.cookies = []
		
	def convert_cookies(self, filepath):
		try:
			with open(filepath, "r") as yntkts:
				lines = yntkts.readlines()
		except FileNotFoundError:
			sys.exit(f"❌ File '{filepath}' tidak ditemukan.")
			return
			
		start = False
		
		for line in lines:
			if line.startswith("#") or not line.strip():
				continue
			parts = line.strip().split("\t")
			if len(parts) < 7:
				continue
			name = parts[5]
			value = parts[6]
			if name == "dpr":
				start = True
			if start:
				self.cookies.append(f"{name}={value}")

		if self.cookies:
			result = "; ".join(self.cookies)
			sys.exit(f"\n✅ Hasil cookies string: {H}{result}{P}")
		else:
			sys.exit("\n❗Tidak ditemukan data dari 'dpr'.")

if __name__ == "__main__":
	os.system("clear")
	print(f"[ Baca Deskripsi Di '{H}github.com/AangQwerty/Convig{P}' Untuk Menggunakan ]\n")
	filepath = input("[?] Masukkan nama file (.txt): ").strip()
	Convert().convert_cookies(filepath)