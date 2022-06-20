import csv
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as pltWins
import matplotlib.pyplot as pltPts

"""
min max home
18 - 184
min max visitor
19 - 186
"""

inputTrainPts = []
outputTrainPts = []
inputTrainWins = []
outputTrainWins = []
inputEvaluationPts = []
outputEvaluationPts = []
inputEvaluationWins = []
outputEvaluationWins = []

with open("gT.csv") as gamesTrain:
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

with open("gTW.csv") as gamesTrainWins:
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

with open("gE.csv") as gamesEvaluation:
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

with open("gEW.csv") as gamesEvaluationWins:
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

modelPts = tf.keras.models.Sequential([
    tf.keras.layers.Dense(
        units=2, activation=tf.nn.sigmoid, input_shape=(2,)),
    tf.keras.layers.Dense(units=5, activation=tf.nn.sigmoid),
    tf.keras.layers.Dense(units=5, activation=tf.nn.sigmoid),
    tf.keras.layers.Dense(units=4, activation=tf.nn.sigmoid),
])
modelWins = tf.keras.models.Sequential([
    tf.keras.layers.Dense(
        units=2, activation=tf.nn.sigmoid, input_shape=(2,)),
    tf.keras.layers.Dense(units=5, activation=tf.nn.sigmoid),
    tf.keras.layers.Dense(units=5, activation=tf.nn.sigmoid),
    tf.keras.layers.Dense(units=2, activation=tf.nn.sigmoid),
])

modelPts.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.3, nesterov=True),
    loss="mean_squared_error",
    metrics=["accuracy"]
)
modelWins.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.3, nesterov=True),
    loss="mean_squared_error",
    metrics=["accuracy"]
)

historyPts = modelPts.fit(
    inputTrainPts, outputTrainPts, epochs=1000, verbose=False)
modelPts.save("saved/nba-model-pts.h5")
modelPts.save_weights("saved/nba-weights-pts.h5")
print("Pts Trained!")

historyWins = modelWins.fit(
    inputTrainWins, outputTrainWins, epochs=1000, verbose=False)
modelWins.save("saved/nba-model-wins.h5")
modelWins.save_weights("saved/nba-weights-wins.h5")
print("Wins Trained!")

pltPts.xlabel("# Epoch")
pltPts.ylabel("Loss")
pltPts.plot(historyPts.history["loss"])

pltWins.xlabel("# Epoch")
pltWins.ylabel("Loss")
pltWins.plot(historyWins.history["loss"])
