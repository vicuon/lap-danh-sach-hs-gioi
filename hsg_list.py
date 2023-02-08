import csv
'''
+ hsg.csv: mẫu danh sách học sinh giỏi
gồm có 04 cột chính Stt, môn dự thi, họ và tên, lớp
+ k12.csv: file dữ liệu chứ điểm tổng kết học kì 1 các môn
lưu ý các môn phải theo đúng thứ tự cột
+ moi.csv: file mới tạo thành quả
'''

file_hsg = open("hsg.csv", "r", encoding="utf-8-sig", newline="")
file_k12 = open("k12.csv", "r", encoding="utf-8-sig", newline="")
file_moi = open("moi.csv", "w", encoding="utf-8-sig", newline="")

csv_hsg = csv.reader(file_hsg)
csv_k12 = csv.reader(file_k12)
csv_moi = csv.writer(file_moi)

next(csv_hsg)
next(csv_k12)

lst_hsg = list(csv_hsg)  # chuyển về list
lst_k12 = list(csv_k12)  # chuyển về list
dem = 0
lst_news = []

tua_file_moi = ["Stt", "Họ và tên", "MSHS", "Môn dự thi", "Điểm môn dự thi", "Lớp", "ngày sinh", "HK", "HL", ""]
csv_moi.writerow(tua_file_moi)

#so_cot_file_moi = ["(C01)", "(C02)", "(C03)", "(C04)", "(C05)", "(C06)", "(C07)", "(C08)", "(C09)", "(C10)"]
#csv_moi.writerow(so_cot_file_moi)

for i in lst_hsg:
    for j in lst_k12:
        lst_rong = [""] * 10
        if i[2] == j[2] and i[3] == j[25]:
            if i[1] == "Anh":
                lst_rong[4] = j[6]
            elif i[1] == "Toán":
                lst_rong[4] = j[4]
            elif i[1] == "Văn":
                lst_rong[4] = j[5]
            elif i[1] == "Hoá":
                lst_rong[4] = j[8]
            elif i[1] == "Lý":
                lst_rong[4] = j[7]
            elif i[1] == "Sinh":
                lst_rong[4] = j[9]
            elif i[1] == "Sử":
                lst_rong[4] = j[10]
            elif i[1] == "Địa":
                lst_rong[4] = j[11]
            elif i[1] == "Tin":
                lst_rong[4] = j[13]
            dem += 1
            lst_rong[0] = str(dem) # số thứ tự
            lst_rong[1] = j[2]      # Họ tên
            lst_rong[2] = j[1]      # Mã số học sinh
            lst_rong[3] = i[1]      # Môn dự thi
                                    # lst_rong[4] trung bình môn dự thi
            lst_rong[5] = j[25]     # Lớp
            lst_rong[6] = j[3]      # ngày sinh
            lst_rong[7] = j[20]      # hạnh kiểm
            lst_rong[8] = j[19]      # học lực

            lst_news.append(lst_rong)

csv_moi.writerows(lst_news)

file_hsg.close()
file_k12.close()
file_moi.close()
