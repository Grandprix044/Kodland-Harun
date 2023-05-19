direkt = {
    "LOL": "komik bir şeye verilen cevap",
    "CRINGE": "garip ya da utandırıcı bir şey",
    "ROFL": "bir şakaya karşılık cevap",
    "SHEESH": "onaylamamak",
    "CREEPY": "korkunç",
    "AGGRO": "agresifleşmek/sinirlenmek",
    "GG": "Good Game - Bir oyunun sonunda veya bir rakibe saygı göstermek amacıyla kullanılır",
    "Noob": "Yeni veya becerisi düşük bir oyuncuyu tanımlamak için kullanılan bir terim",
    "PogChamp": "Heyecan veya şaşkınlık ifade etmek için kullanılan bir emote veya ifade",
    "EZ": "Easy - Bir oyunu kolay bir şekilde kazanmak veya rakipleri küçümsemek amacıyla kullanılır",
    "Rage Quit": "Bir oyuncunun öfkeyle veya hayal kırıklığıyla bir oyundan çıkması veya terk etmesi durumunu ifade eder",
    "AFK": "Away From Keyboard - Oyuncunun klavye veya oyun kumandasından uzak olduğunu veya oyunla ilgilenmediğini ifade eder",
    "Loot Goblin": "Oyunlarda sürekli olarak eşya toplayan veya hırsızlık yapan oyunculara atıfta bulunmak için kullanılan bir terim",
    "Nerf": "Bir oyun karakterinin veya eşyanın aşırı güçlü olduğunu düşündüğümüzde onun zayıflatılmasını veya dengelemesini talep etmek için kullanılan bir terim",
    "Buff": "Bir oyun karakterinin veya eşyanın daha güçlü hale getirilmesini veya iyileştirilmesini talep etmek için kullanılan bir terim",
    "OP": "Overpowered - Bir şeyin oyun içinde aşırı güçlü veya dengesiz olduğunu ifade eder"
    "POGGERS": "Heyecanlı bir durumu ifade etmek için kullanılan bir emote veya ifade",
    "FACEPALM": "Hayal kırıklığı veya utanç anında kullanılan bir hareket veya ifade",
    "EPIC": "Çok büyük, etkileyici veya muhteşem bir şeyi ifade etmek için kullanılır",
    "GET REKT": "Bir oyuncunun rakibini kolayca yendiğinde veya üstünlük kurduğunda kullanılan bir ifade",
    "SPAM": "Bir kelime, ifade veya hareketi tekrarlayarak rahatsız edici veya dikkat dağıtıcı olmak",
    "TROLL": "Diğer oyuncuları rahatsız etmek veya kışkırtmak için amacıyla yapay olarak davranmak veya provokatif davranışlarda bulunmak",
    "NANI?!": "Şaşkınlık veya anlamayı ifade etmek için kullanılan bir ifade",
    "EZ Clap": "Kolay bir zaferin veya başarının kutlanması için kullanılan bir ifade",
    "LOLW": "Gülmek veya komik bir şeye tepki vermek için kullanılan bir emote veya ifade",
    "OMG": "Oh My God - Şaşkınlık veya hayret ifadesi",
    "SALT": "Tuzlu - Bir oyuncunun öfke, hayal kırıklığı veya kıskançlık ifade etmesi",
    "REKT": "Bir oyuncunun ezildiğini veya yenildiğini ifade etmek için kullanılan bir terim",
    "LUL": "Laugh Out Loud - Gülmek veya bir şeye güldüğünü ifade etmek için kullanılan bir ifade"

}

cıktı = input("Anlamadığınız bir kelime yazın (Büyük küçük harf fark eder!): ")

if cıktı in direkt.keys():
    print(direkt[cıktı])
else:
    print("Anlaşılmadı")
