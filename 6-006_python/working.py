import os

currentWorkingDir = os.getcwd()
print(currentWorkingDir)

trialFile = open('./6-006_python/trial.txt')
print(trialFile.read())