# -*- coding: utf-8 -*-
"""
Created on Mon May  2 21:30:23 2016

@author: Daniel_2

major used sites:
https://pythonprogramming.net/image-recognition-python/
https://pythonprogramming.net/linear-svc-example-scikit-learn-svm-python/
http://stackoverflow.com/questions/15564410/scikit-learn-svm-how-to-save-load-support-vectors
"""

#all the imports
from PIL import Image
import numpy as np
from functools import reduce
import os
from sklearn import svm
from sklearn.externals import joblib
import sys

#this is the path to the testing data
dataPath = ('../TESTING')

def main():
    
    #this command argument is the path to the image to be identified (or "Setup")
    readFile = str(sys.argv[1])

    #this is for setting up and training the SVM
    if(readFile == "Setup"):
        data, labels = loadData()
        clf = svm.SVC(kernel='linear', C = 1.0)
        #trains the SVM
        clf.fit(np.array(data), labels)
        #pickles the SVM to be used later
        joblib.dump(clf, 'proj3SVM.pkl')
        print("Setup Complete")
    #if readFile != "Setup", it uses the SVM to identify the image thats at the path readFile
    else:
        clf = joblib.load('proj3SVM.pkl')
        prediction = clf.predict(threshold(np.array(Image.open(readFile),dtype='int64')))
        print("The image has been identified as: " + prediction[0])


#loads all the training data and uses threshold function to turn them into usable arrays
def loadData():
    
    data = []
    labels = []
    for foldername in os.listdir(dataPath):

        #wont open folders that dont have one of these names
        if(foldername == '01' or
           foldername == '02' or
           foldername == '03' or
           foldername == '04' or
           foldername == '05'):
               
            #runs for each file in the folder
            for filename in os.listdir(dataPath + '/' + foldername):
                
                #opens the image, reduces it to an array, then appends it to a different array
                #also records what the label is (supervised learning)
                image = Image.open(dataPath + '/' + foldername + '/' + filename)
                if(foldername == '01'):
                    data.append(threshold(np.array(image,dtype='int64')))
                    labels.append('Smile')
                elif(foldername == '02'):
                    data.append(threshold(np.array(image,dtype='int64')))
                    labels.append('Hat')
                elif(foldername == '03'):
                    data.append(threshold(np.array(image,dtype='int64')))
                    labels.append('Hash')
                elif(foldername == '04'):
                    data.append(threshold(np.array(image,dtype='int64')))
                    labels.append('Heart')
                else:
                    data.append(threshold(np.array(image,dtype='int64')))
                    labels.append('Dollar')
                    
    return data, labels
            
#reduces an image array in an array of 1s and 0s
def threshold(imageArray):
    balanceAr = []
    newAr = imageArray
    
    #basically determines what shades should become black and which shades should become white
    #based on average color of the image (average stored as balance)
    for eachRow in imageArray:
        for eachPix in eachRow:
            #creates a value for the color and stores in an array
            avgNum = reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3])
            balanceAr.append(avgNum)
    #averages all the colors of the array and stores as balance
    balance = reduce(lambda x, y: x + y, balanceAr)/len(balanceAr)
    
    threshArray = []
    r = 0
    for eachRow in newAr:
        c = 0
        for eachPix in eachRow:
            #if the pixels color is above the balance color, pixel is black, otherwise it is white
            if (reduce(lambda x, y: x + y, eachPix[:3])/len(eachPix[:3]) > balance):
                threshArray.append(0)
            else:
                threshArray.append(1)
            c += 1
        r += 1
    return threshArray
    
main()