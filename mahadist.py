import sys
import numpy as np
def readData(path):
    f=open(path)
    info=[int (i) for i in f.readline().strip().split()]
    data=dict()
    data['n']=info[0]
    data['dim']=info[1]
    data['data']=[]
    for line in f.readlines():
        data['data'].append([float(i) for i in line.strip().split()])
    data['data']=np.array(data['data'])
    return data

def computeCov(data):
    data['Centroid']=data['data'].mean(0)
    subtracted_mean=data['data']-data['Centroid']
    data['cov']=subtracted_mean.T.dot(subtracted_mean)/float(data['n'])

def computeDist(train, test):
    vec=test['data']-train['Centroid']
    dist=[]
    for v in vec:
        dist.append(np.sqrt(v.T.dot(np.linalg.inv(train['cov'])).dot(v)))
    test['dist']=np.array(dist)

def arr2str(arr):
    s=''
    if len(arr.shape)==1:

        return ' '.join(map(str,arr))
    else:
        for subarr in arr:
            s+=arr2str(subarr)+'\n'
    return s
        
def result(train,test):
    print 'Centroid:'
    print arr2str(train['Centroid'])
    print 'Covariance matrix:'
    print arr2str(train['cov'])
    print 'Distances:'
    for i,j,k in zip(range(1,test['n']+1),test['data'],test['dist']):
        print i, '. ', arr2str(j), '--', k
        
def main():
    raw_train=sys.argv[1]
    raw_test=sys.argv[2]
    data=readData(raw_train)
    computeCov(data)
    test=readData(raw_test)
    computeDist(data,test)
    result(data,test)

main()
# if __name__="__main__":
#     main()
