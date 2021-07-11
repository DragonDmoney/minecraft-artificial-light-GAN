import cv2
import sys
from tqdm import tqdm
v = cv2.VideoCapture(r'C:\Users\addis\Videos\minecraft-shaders-gan\test default.mp4')
s = cv2.VideoCapture(r'C:\Users\addis\Videos\minecraft-shaders-gan\shader test.mp4')

length = 400

pbar = tqdm(total=length)
pbar.update(n=1)


count = 1
for i in range(4240000):
    a,iv = v.read()
    c,iis = s.read()
    if i % 5 == 0:
        iv =cv2.resize(iv,[192,108])
        iis =cv2.resize(iis,[192,108])
        cv2.imwrite('data\shader test\\'+str(count)+'.jpg',iis)
        cv2.imwrite('data\default test\\'+str(count)+'.jpg', iv)
        sys.stdout.flush()
        # sys.stdout.write('\rCount: '+str(count)+' i: ' + str(i))
        count +=1
        pbar.update(n=1)
