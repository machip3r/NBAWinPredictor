import csv
import tensorflow as tf
from tensorflow import keras
""" import matplotlib.pyplot as pltWins
import matplotlib.pyplot as pltPts """

inputTrainPts = []
outputTrainPts = []
inputTrainWins = []
outputTrainWins = []
inputEvaluationPts = []
outputEvaluationPts = []
inputEvaluationWins = []
outputEvaluationWins = []

with open("gamesTrain.csv") as gamesTrain:
    csv_readerTP = csv.reader(gamesTrain, delimiter=",")
    lineCounterTP = 0
    inputsTP = []
    outputsTP = []
    for row in csv_readerTP:
        if lineCounterTP != 0:
            inputsTP.append([int(row[0]), int(row[1])])
            outputsTP.append(
                [float(float(row[2]) / 190), float(float(row[3]) / 190), int(row[4]), int(row[5])])
        lineCounterTP += 1
    inputTrainPts = inputsTP
    outputTrainPts = outputsTP

with open("gamesTrainWins.csv") as gamesTrainWins:
    csv_readerTW = csv.reader(gamesTrainWins, delimiter=",")
    lineCounterTW = 0
    inputsTW = []
    outputsTW = []
    for row in csv_readerTW:
        if lineCounterTW != 0:
            inputsTW.append([int(row[0]), int(row[1])])
            outputsTW.append([int(row[2]), int(row[3])])
        lineCounterTW += 1
    inputTrainWins = inputsTW
    outputTrainWins = outputsTW

with open("gamesEvaluation.csv") as gamesEvaluation:
    csv_readerEP = csv.reader(gamesEvaluation, delimiter=",")
    lineCounterEP = 0
    inputsEP = []
    outputsEP = []
    for row in csv_readerEP:
        if lineCounterEP != 0:
            inputsEP.append([int(row[0]), int(row[1])])
            outputsEP.append(
                [float(float(row[2]) / 190), float(float(row[3]) / 190), int(row[4]), int(row[5])])
        lineCounterEP += 1
    inputEvaluationPts = inputsEP
    outputEvaluationPts = outputsEP

with open("gamesEvaluationWins.csv") as gamesEvaluationWins:
    csv_readerEW = csv.reader(gamesEvaluationWins, delimiter=",")
    lineCounterEW = 0
    inputsEW = []
    outputsEW = []
    for row in csv_readerEW:
        if lineCounterEW != 0:
            inputsEW.append([int(row[0]), int(row[1])])
            outputsEW.append([int(row[2]), int(row[3])])
        lineCounterEW += 1
    inputEvaluationWins = inputsEW
    outputEvaluationWins = outputsEW

modelPts = tf.keras.models.load_model('saved/nba-model-pts.h5')
modelWins = tf.keras.models.load_model('saved/nba-model-wins.h5')

""" modelPts.summary()
modelWins.summary() """

modelPts.load_weights("saved/nba-weights-pts.h5")
modelWins.load_weights("saved/nba-weights-wins.h5")

""" historyPts = modelPts.fit(inputTrainPts, outputTrainPts,
                          epochs=1, verbose=False)
print("Pts Trained!")
historyWins = modelWins.fit(
    inputTrainWins, outputTrainWins, epochs=1, verbose=False)
print("Wins Trained!") """

modelPts.evaluate(inputEvaluationPts, outputEvaluationPts)
modelWins.evaluate(inputEvaluationWins, outputEvaluationWins)

loss, acc = modelPts.evaluate(
    inputEvaluationPts, outputEvaluationPts, verbose=2)
print('Restored model PTS, accuracy: {:5.2f}%'.format(100 * acc))
loss, acc = modelWins.evaluate(
    inputEvaluationWins, outputEvaluationWins, verbose=2)
print('Restored model WINS, accuracy: {:5.2f}%'.format(100 * acc))

""" pltPts.xlabel("# Epoch")
pltPts.ylabel("Loss")
pltPts.plot(historyPts.history["loss"])

pltWins.xlabel("# Epoch")
pltWins.ylabel("Loss")
pltWins.plot(historyWins.history["loss"]) """

modelPts.predict([[50, 25]])
modelWins.predict([[52, 56]])
