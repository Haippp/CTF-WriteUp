# b00tl3gRSA2
## Deskripsi Challange
Pada RSA, d jauh lebih besar daripada e, mengapa kita tidak menggunakan d untuk mengenkripsi daripada e? Hubungkan dengan `nc jupiter.challenges.picoctf.org 57464`.

## Penyelesaian
Awalnya saya dengan naif nya mencoba e sebagai kunci untuk mendekripsinya. Tapi saya malah mendapatkan hasil yang aneh😅.
```
Output : Al"\x18e\xc2\x8e;\xf4&<\xd8!\xae\x96\x19sn\xff^\x9a\xa1`Q\xd4b\xcc\xd2\xde\xe4\xb9A,?3\x95\xc2\x8e\x05%\x19\xe9\x10]\xff\xc2\xf7D\x82\x95D4\\i\xed\xf8\x1b&U\x83\x9dD\xc0u\xda\xfb\xbf\xbay\x80\x9e\xad\xb9b\xcau\x9fS\xd42*\x9c\xdb^\x86\x9c]m^\xcbL`\xbaQj{R#\xc2\xb31/J\xa9+\t\x02\xc57\xf8\x7f\x0fbp\xfdJ\xae\xb5\x88BQh\x98\xda@z\xf65
```
Tapi ini wajar, karena kesulitan dari challange ini hard jadi tidak mungkin semudah itu😎. Selanjutnya saya mencari beberapa artikel tentang e yang lebih besar dari d. Dan saya mendapatkan solusi setelah ada artikel yang bilang bahwa jika e lebih kecil maka d lebih besar dan jika e lebih besar maka d lebih kecil. 

Setelah saya coba menghubungkan ke `nc jupiter.challenges.picoctf.org 57464` disini saya mendapatkan e yang sangat besar. Yang dimana berdasarkan aturan sebelumnya, berarti bahwa d akan cukup kecil. Dan kita hanya perlu untuk melakukan perulangan sampai kesekian kalinya untuk mendapatkan flagnya. dan berikut programnya:

```python
from Crypto.Util.number import long_to_bytes

c = 49364499428942386709759045218558739704197206758238234544083236918148418678546318902901921410821783978523870724731556702013645087071314355606501151512417428031120850793747553700522784872327889979371575789329040566353654720859234819170873065033922256818121931966434058383133102809006779601756651680054569802257
n = 92388317218321746284523842272743905775730199568570206175441263891283322448555641590382257161515688345172022688386537744046456526559022664360430817601173138492426806373826074299905719153968312043413062224398846619787262691631581748286443127742369695249750214057283200475480944263522915387139084511566747395439
e = 3515822560423797781918648437191560507876026026885791143957619545369190017649537972846077015438914303871996346870256879833557571711219654926452453714654710458308088658053383287907090531080769886335843458634622821796904613812510791241562410551422213065234832732141365858731867681276730669847673992398838006945

flag = b''; d = 2

while True:
    if b'picoCTF' in flag:
        print(flag)
        break
    print(d)
    flag = long_to_bytes(pow(c, d, n)) ; d += 1 
```

Program ini akan terus menerus mencoba semua kemungkinan d yang ada sampai menemukan teks format flag yang tetap baru akan berhenti. Dan yap, Challange berhasil kita selesaikan😁.