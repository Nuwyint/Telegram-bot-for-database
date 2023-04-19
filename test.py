dict = {861546282: {'id': '123', 'stage': 'done', 'name': 'Tower', 'category': 'Bilding', 'positions': '1 2', 'modelUrl': 'Https', 'ImgUrl': 'Https', 'text': 'Kill me'}}
a = list(map(int, (dict[861546282]['positions']).split()))
pos = ({ "x": a[0] , "y": a[1] })
print(pos)