with open('example text.txt', 'r') as f:
    with open('gecenler','w') as g:
        with open('kalanlar','w') as k:
            icerik=f.readlines()
            m=0
            for setir in icerik:
                if m==0:
                    m+=1
                    continue
                setir=setir.replace('\n','')
                bosluq_sayi=0
                index=0
                bosluq_indexi=[]
                for karakter in setir:
                    if karakter==' ':
                        bosluq_sayi+=1
                        bosluq_indexi.append(index)
                    index+=1
                ad_soyad=setir[:bosluq_indexi[0]]
                soyad=ad_soyad.split('-')[-1]
                ad= ad_soyad[:ad_soyad.index(soyad)-1].replace('-',' ')
                notlar=setir.split(' ')[-1]
                notlar=notlar.split('/')
                birinci_vize=notlar[0]
                ikinci_vize=notlar[1]
                final=notlar[2]
                ortalama= int(birinci_vize) * 0.3 + int(ikinci_vize) * 0.3 + int(final) * 0.4
                bolum=setir[bosluq_indexi[0]+1:bosluq_indexi[len(bosluq_indexi)-1]]
                if int(ortalama) >= 70 and int(final) >= 70:
                    g.write(ad)
                    g.write(' '*(25-len(ad)))
                    g.write(soyad)
                    g.write(' '*(25-len(soyad)))
                    g.write(bolum)
                    g.write(' '*(25-len(bolum)))
                    g.write(str(round(ortalama,1)))
                    g.write(' '*20)
                    g.write('gecti')
                    g.write('\n')
                else:
                    k.write(ad)
                    k.write(' ' * (25 - len(ad)))
                    k.write(soyad)
                    k.write(' ' * (25 - len(soyad)))
                    k.write(bolum)
                    k.write(' ' * (25 - len(bolum)))
                    k.write(str(round(ortalama, 1)))
                    k.write(' ' * 20)
                    k.write('gecti')
                    k.write('\n')
