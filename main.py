import cv2
import sys
v = cv2.VideoCapture(r'C:\Users\addis\Videos\minecraft-shaders-gan\vanilla.mp4')
s = cv2.VideoCapture(r'C:\Users\addis\Videos\minecraft-shaders-gan\shader.mp4')

from tqdm import tdqm LENGTH = 10 # Number of iterations required to fill

pbar pbar = tqdm(total=LENGTH)
pbar.update(n=1)

length = 21600

count = 1
for i in range(4240000):
    a,iv = v.read()
    c,iis = s.read()
    if i % 5 == 0:
        iv =cv2.resize(iv,[192,108])
        iis =cv2.resize(iis,[192,108])
        cv2.imwrite('data\shader\\'+str(count)+'.jpg',iv)
        cv2.imwrite('data\default\\'+str(count)+'.jpg',iis)
        sys.stdout.flush()
        sys.stdout.write('\rCount: '+str(count)+' i: ' + str(i))
        count +=1
        pbar.update(n=1)
