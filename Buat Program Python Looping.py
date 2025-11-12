while True:
    print("\n=== MENU SEDERHANA ===")
    print("1. Tampilkan 10 bilangan pertama")
    print("2. Tampilkan bilangan genap 1-20")
    print("3. Hitung jumlah 1-100")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\n10 bilangan pertama:")
        for i in range(1, 11):
            print(i, end=" ")
        print()  # ganti baris

    elif pilihan == "2":
        print("\nBilangan genap dari 1-20:")
        for i in range(2, 21, 2):
            print(i, end=" ")
        print()

    elif pilihan == "3":
        total = 0
        for i in range(1, 101):
            total += i
        print(f"\nJumlah bilangan 1-100 adalah: {total}")

    elif pilihan == "4":
        print("\nTerima kasih! Program selesai.")
        break

    else:
        print("\nPilihan tidak valid, silakan coba lagi.")
