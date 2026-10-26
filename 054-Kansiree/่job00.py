# 1. รับค่าราคาสินค้าและอัตราภาษี VAT จากผู้ใช้
price = float(input("กรุณากรอกราคาสินค้า: "))
vat_rate = float(input("กรุณากรอกอัตราภาษี VAT (%): "))

#  2. คำนวณภ่าษี VAT และราคาสุทธิ
vat_amount = price * (vat_rate / 100)
total_price = price + vat_amount

# 3.แสดงผลลัพธ์ออกทางหน้าจอ
print("\n---- ผลการคำนวณภาษีมูลค่าเพิ่ม (VAT) ----");
print(f"ราคาสินค้า: {price:.2f} บาท")
print(f"ภาษี VAT ({vat_rate} %): {vat_amount:.2f} บาท")
print(f"ราคาสุทธิ: {total_price:.2f} บาท");