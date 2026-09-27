import pandas as pd
import time

#ID
file_id = "1ed8GdLI3W575SKtWahf5h4gDz2KywY5i"
# URL CSV
url = f"https://docs.google.com/spreadsheets/d/{file_id}/export?format=csv"

df = pd.read_csv(url, header=None).fillna('-')


################## INDEXING ##############

cabang = df.iloc[2, 1]
tanggal = df.iloc[1, 1]

################## STORING ##############

espresso = df.iloc[35,1]
creamer = df.iloc[36,1]
milo = df.iloc[37,1]
skm = df.iloc[38,1]
gula = df.iloc[39,1]
uht = df.iloc[40,1]

strawberry = df.iloc[41,1]
lemon = df.iloc[42,1]
melon = df.iloc[43,1]

brown = df.iloc[44,1]
bts = df.iloc[45,1]

choco = df.iloc[46,1]
rv = df.iloc[47,1]
taro = df.iloc[48,1]
matcha = df.iloc[49,1]

################# ALTERNATE ##############

grespresso = df.iloc[35,2]
grcreamer = df.iloc[36,2]
grmilo = df.iloc[37,2]
grskm = df.iloc[38,2]
grgula = df.iloc[39,2]
gruht = df.iloc[40,2]

grstrawberry = df.iloc[41,2]
grlemon = df.iloc[42,2]
grmelon = df.iloc[43,2]

grbrown = df.iloc[44,2]
grbts = df.iloc[45,2]

grchoco = df.iloc[46,2]
grrv = df.iloc[47,2]
grtaro = df.iloc[48,2]
grmatcha = df.iloc[49,2]

############### STORING ###################

cristalinstoring = df.iloc[50,1]

slopmold = df.iloc[59,2]
sloplold = df.iloc[60,2]
slophold = df.iloc[61,2]

slopmnew = df.iloc[59,1]
sloplnew = df.iloc[60,1]
slophnew = df.iloc[61,1]

tutupold = df.iloc[62,1]
tutupnew = df.iloc[62,2]
tutuph = df.iloc[63,1]

plastik1 = df.iloc[64,1]
plastik2 = df.iloc[65,1]
sedotan = df.iloc[66,1]


############# REPORT ####################

shift1 = df.iloc[4, 1]
shift2 = df.iloc[4, 3]

omsetc1 = df.iloc[5, 1]
omsetq1 = df.iloc[6, 1]
omsetc2 = df.iloc[5, 3]
omsetq2 = df.iloc[6, 3]
omseto = df.iloc[7, 1]

pengeluaran1 = df.iloc[9, 1]
pengeluaran2 = df.iloc[10, 1]
pengeluaran3 = df.iloc[9, 3]
pengeluaran4 = df.iloc[10, 3]

notep1 = df.iloc[9, 0]
notep2 = df.iloc[10, 0]
notep3 = df.iloc[9, 2]
notep4 = df.iloc[10, 2]

totalc = df.iloc[15, 1]
totalq = df.iloc[16, 1]
totalp = df.iloc[12, 2]

cupawalm = df.iloc[20, 1]
cupawall = df.iloc[21, 1]
cupawalh = df.iloc[22, 1]

cup1m = df.iloc[20, 2]
cup1l = df.iloc[21, 2]
cup1h = df.iloc[22, 2]

cup2m = df.iloc[20, 3]
cup2l = df.iloc[21, 3]
cup2h = df.iloc[22, 3]

cupakhirm = df.iloc[20, 4]
cupakhirl = df.iloc[21, 4]
cupakhirh = df.iloc[22, 4]

cupplusm = df.iloc[15, 3]
cupplusl = df.iloc[16, 3]
cupplush = df.iloc[17, 3]

cupminm = df.iloc[15, 4]
cupminl = df.iloc[16, 4]
cupminh = df.iloc[17, 4]

cupjualm = df.iloc[25, 1]
cupjuall = df.iloc[26, 1]
cupjualh = df.iloc[27, 1]

dimsum2 = df.iloc[25, 3]
dimsum4 = df.iloc[26, 3]
cristalin = df.iloc[27, 3]

#####################################
print("VARIABLES CHECKING UNDERWAY")

variables = {
    "cabang": cabang,
    "tanggal": tanggal,
    "espresso": espresso,
    "creamer": creamer,
    "milo": milo,
    "skm": skm,
    "gula": gula,
    "uht": uht,
    "strawberry": strawberry,
    "lemon": lemon,
    "melon": melon,
    "brown": brown,
    "bts": bts,
    "choco": choco,
    "rv": rv,
    "taro": taro,
    "matcha": matcha,
    "grespresso": grespresso,
    "grcreamer": grcreamer,
    "grmilo": grmilo,
    "grskm": grskm,
    "grgula": grgula,
    "gruht": gruht,
    "grstrawberry": grstrawberry,
    "grlemon": grlemon,
    "grmelon": grmelon,
    "grbrown": grbrown,
    "grbts": grbts,
    "grchoco": grchoco,
    "grrv": grrv,
    "grtaro": grtaro,
    "grmatcha": grmatcha,
    "cristalinstoring": cristalinstoring,
    "slopmold": slopmold,
    "sloplold": sloplold,
    "slophold": slophold,
    "slopmnew": slopmnew,
    "sloplnew": sloplnew,
    "slophnew": slophnew,
    "tutupold": tutupold,
    "tutupnew": tutupnew,
    "tutuph": tutuph,
    "plastik1": plastik1,
    "plastik2": plastik2,
    "sedotan": sedotan,
    "shift1": shift1,
    "shift2": shift2,
    "omsetc1": omsetc1,
    "omsetq1": omsetq1,
    "omsetc2": omsetc2,
    "omsetq2": omsetq2,
    "omseto": omseto,
    "pengeluaran1": pengeluaran1,
    "pengeluaran2": pengeluaran2,
    "pengeluaran3": pengeluaran3,
    "pengeluaran4": pengeluaran4,
    "notep1": notep1,
    "notep2": notep2,
    "notep3": notep3,
    "notep4": notep4,
    "totalc": totalc,
    "totalq": totalq,
    "totalp": totalp,
    "cupawalm": cupawalm,
    "cupawall": cupawall,
    "cupawalh": cupawalh,
    "cup1m": cup1m,
    "cup1l": cup1l,
    "cup1h": cup1h,
    "cup2m": cup2m,
    "cup2l": cup2l,
    "cup2h": cup2h,
    "cupakhirm": cupakhirm,
    "cupakhirl": cupakhirl,
    "cupakhirh": cupakhirh,
    "cupplusm": cupplusm,
    "cupplusl": cupplusl,
    "cupplush": cupplush,
    "cupminm": cupminm,
    "cupminl": cupminl,
    "cupminh": cupminh,
    "cupjualm": cupjualm,
    "cupjuall": cupjuall,
    "cupjualh": cupjualh,
    "dimsum2": dimsum2,
    "dimsum4": dimsum4,
    "cristalin": cristalin,
}

print("\n--- SCANNING IN PROGRESS ---\n")
for key, value in variables.items():
    time.sleep(0.05)
    if value == "-":
        print(f"{key:<18} : null")
    else:
        print(f"{key:<18} : {value} ✓")
print("\n ALL SCANNED !!! \n")
    
if cupplusm == "-":
    cupplusm = "0"
if cupplusl == "-":
    cupplusl = "0"
if cupplush == "-":
    cupplush = "0"
    
print("""

=== AUTOCHECK REPORT FILCOF REIN V1 ===

IN PROGRESS!!!
""")

time.sleep(2)

print(f"""
=======================================

SUCESSFULLY GENERATED!!! [REPORT]

‎📍 *Filcof {cabang} {tanggal}* 

‎ *Cup awal* 
- Medium : {cupawalm} + {cupplusm} sisa {cupakhirm}
- Large : {cupawall} + {cupplusl} sisa {cupakhirl}
- Hot : {cupawalh} + {cupplush} sisa {cupakhirh}

*Cup Terjual Per Shift*

*Shift 1 ( {shift1} )*
- Medium : {cup1m} cup 
- Large : {cup1l} cup
- Hot : {cup1h} cup

*Shift 2 ( {shift2} )*
- Medium : {cup2m} cup 
- Large : {cup2l} cup
- Hot : {cup2h} cup

*Online* 
- Medium : - cup
- Large : - cup
- Hot : - cup

‎ *Cup Terjual Total* 
- Medium : {cupjualm} cup
- Large : {cupjuall} cup
- Hot : {cupjualh} cup
‎Total cup terjual : 

Keterangan : 
- 

*Kemasan Botol*
- 1000 ml : - botol
- ⁠500 ml : - botol
- ⁠250 ml : - botol 
‎
‎ *Snack* 
- Dimsum 4 pcs : {dimsum4}
- Dimsum 2 pcs : {dimsum2}
- ⁠Bakpao : -
- ⁠Pop Mie : -
- Air mineral: {cristalin}
- Doubleshot: 

‎ *Pengeluaran*
- {notep1} {pengeluaran1}
- {notep2} {pengeluaran2}
- {notep3} {pengeluaran3}
- {notep4} {pengeluaran4}
‎
‎*Diskon*
- ‎cash : -
- qris : -
‎Total : -
‎
‎ *Omset* 
‎ Cash : ({omsetc1}+{omsetc2})-{totalp} = Rp.{totalc}
 Qris : {omsetq1}+{omsetq2} = Rp.{totalq}
 Online : Rp.{omseto} """)
 
 
print(f"""
SUCESSFULLY GENERATED!!! [STORING]

*Update stock {cabang}*

*{tanggal}*
Bahan : 
- KOPI POWDER : {espresso} Pack {grespresso} Gram
- CREAMER : {creamer} Ember {grcreamer} Gram 
- BROWN SUGAR : {brown} Botol
- SIRUP STRAWBERRY : {strawberry} Botol
- SIRUP LEMON : {lemon} Botol
- SIRUP MELON : {melon} Botol
- MILO : {milo} Pack {grmilo} Gram
- SKM : {skm} Pack {grskm} Gram
- GULA PASIR : {gula} Gram
- UHT : {uht} Botol {gruht} Ml
- CHOCO : {choco} Pack {grchoco}
- RED VELVET : {rv} Pack
- TARO : {taro} Pack
- BUTTERSCOTH : {bts} Botol
- MATCHA : {matcha} Pack {grmatcha} Gram
- CRYSTALIN : {cristalinstoring} Botol

Barang : 
- CUP REGULER: [Baru: {slopmnew} slop] [Lama {slopmold} slop] {cupawalm} pcs
- CUP LARGE: [Baru: {sloplnew} slop] [Lama {sloplold} slop] {cupawall} pcs
- CUP HOT: {slophnew} slop {cupawalh} pcs
- TUTUP R+L: [Baru: {tutupnew} slop] [Lama {tutupold} slop]
- TUTUP HOT: {tutuph} slop
- PLASTIK 1 CUP: {plastik1}
- PLASTIK 2 CUP: {plastik2}
- SEDOTAN: {sedotan}""")










