phone_input = input("Telefon numaranızı girin (başında 0 olmadan): ")

cleaned = phone_input.strip()

for ch in ["-", "(", ")", ".", "+", " "]:
    cleaned = cleaned.replace(ch, "")

if cleaned.startswith("90"):
    cleaned = cleaned[2:]

if len(cleaned) == 10 and cleaned.startswith("5") and cleaned.isdigit():
    first = cleaned[0:3]
    mid = cleaned[3:6]
    part1 = cleaned[6:8]
    part2 = cleaned[8:]
    print(f"Formatlanmış numara: 0{first} {mid} {part1} {part2}")
else:
    print("Hata: Lütfen başında 0 olmadan, tam 10 haneli geçerli bir Türk numarası girin.")