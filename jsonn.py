import json


data = """{
    "classCode" : "IT201",
    "day" : "1" ,
    "week" : "1",
    "branch" : "IT",
    "students" :[

        
        ]
        }"""

listt = ["""Aamir_Khan
Abhay_Deol
Abhishek_Bachchan
Aftab_Shivdasani
Aishwarya_Rai
Ajay_Devgn
Akshaye_Khanna
Akshay_Kumar
Alia_Bhatt
Ameesha_Patel
Amitabh_Bachchan
Amrita_Rao
Amy_Jackson
Anil_Kapoor
Anushka_Sharma
Anushka_Shetty
Arjun_Kapoor
Arjun_Rampal
Arshad_Warsi
Asin
Ayushmann_Khurrana
Bhumi_Pednekar
Bipasha_Basu
Bobby_Deol
Deepika_Padukone
Disha_Patani
Emraan_Hashmi
Esha_Gupta
Farhan_Akhtar
Govinda
Hrithik_Roshan
Huma_Qureshi
Ileana_D+ô+ç+ûCruz
Irrfan_Khan
Jacqueline_Fernandez
John_Abraham
Juhi_Chawla
Kajal_Aggarwal
Kajol
Kangana_Ranaut
Kareena_Kapoor
Karisma_Kapoor
Kartik_Aaryan
Katrina_Kaif
Kiara_Advani
Kriti_Kharbanda
Kriti_Sanon
Kunal_Khemu
Lara_Dutta
Madhuri_Dixit
Manoj_Bajpayee
Mrunal_Thakur
Nana_Patekar
Nargis_Fakhri
Naseeruddin_Shah
Nushrat_Bharucha
Paresh_Rawal
Parineeti_Chopra
Pooja_Hegde
Prabhas
Prachi_Desai
Preity_Zinta
Priyanka_Chopra
Rajkummar_Rao
Ranbir_Kapoor
R_Madhavan
Randeep_Hooda
Rani_Mukerji
Ranveer_Singh
Richa_Chadda
Riteish_Deshmukh
Saif_Ali_Khan
Salman_Khan
Sanjay_Dutt
Sara_Ali_Khan
Shahid_Kapoor
Shah_Rukh_Khan
Shilpa_Shetty
Shraddha_Kapoor
Shreyas_Talpade
Shruti_Haasan
Sidharth_Malhotra
Sonakshi_Sinha
Sonam_Kapoor
Suniel_Shetty
Sunny_Deol
Sushant_Singh_Rajput
Taapsee_Pannu
Tabu
Tamannaah_Bhatia
Tiger_Shroff
Tusshar_Kapoor
Uday_Chopra
Vaani_Kapoor
Varun_Dhawan
Vicky_Kaushal
Vidya_Balan
Vivek_Oberoi
Yami_Gautam
Zareen_Khan"""]
# y = {"name": str(f'{match}')}
# tempjson.append(y)
j = json.loads(data)
temp = j["students"]

f = open("bollywood_list.txt", "r")
f.readline()
for x in f:
    print(x)
    t = x
    t = t[:-1]
    y = {"name": t}
    temp.append(y)

print(json.dumps(j))
print("")
# print(listt.readline())
# for i in f:
#     print(i)

# f.close()