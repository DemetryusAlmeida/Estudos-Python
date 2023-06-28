n = float(input('Digite um valor em metros: '))
#print('{}m em quilômetros é {}km\n{}m em hectômetro é {}hm\n{}m em decâmetro é {}dam\n{}m em decímetros é {}dm\n {}m em centímetros é {}cm\n{}m em milímetros é {}mm'.format(n, n/1000, n, n/100, n, n/10, n, n, n*10, n*100, n, n*1000))
km = n/1000
hm = n/100
dam = n/10
dm = n*10
cm = n*100
mm = n*1000
print('{}km\n{}hm\n{}dam\n{}dm\n{}dm\n{}mm'.format(km, hm, dam, dm, cm, mm))