import sys
from scipy.io import wavfile
from scipy.fft import fft, ifft, fftfreq
from scipy.signal import blackman
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import heartpy as hp
import tensorflow as tf
from sklearn.metrics import r2_score
from tensorflow import keras
import keras_tuner as kt

if __name__ == "__main__":
    # creating custom data/ x and y values
    X = np.arange(-210, 210, 3).reshape((140, 1))
    X_square = X**2
    '''
    For this input matrix:
    [X^2 X] 
    obtained weights will have the coefficient order a,b,c
    where a is for X^2, b is for X and c as a intercept
    '''
    X_input = np.append(X_square,X, axis=1)
    a_exact = 4
    b_exact = 70
    c_exact = 12
    print(X.shape)
    y = a_exact*X_square + b_exact*X + c_exact
    # 400*np.random.rand(X.size)


    # size of the plot
    plt.figure(figsize=(12, 6))
    plt.scatter(X, y, c="r", label="Exact model")
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    # plt.show()

    # Splitting training and test data
    X_train = X_input[:110,:]
    y_train = y[:110]
    X_test = X_input[110:,:]
    y_test = y[110:]


    # # size of the plot
    # plt.figure(figsize=(12, 6))
    # plt.scatter(X_train[:,0], y_train, c="r", label="Train data")
    # plt.scatter(X_test[:,0], y_test, c="b", label="Test data")
    # plt.grid()
    # plt.xlabel("X")
    # plt.ylabel("Y")
    # plt.legend()
    # plt.show()

    # Model
    Histories = []
    LR = []
    LR_sgd = [0.01, 0.02]
    LR_adam = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5]
    LR_adam = [0.1]
    LR_set = LR_adam
    for lr in LR_set:
        model = tf.keras.Sequential([tf.keras.layers.InputLayer(input_shape=2,),
                                    tf.keras.layers.Dense(1),
                                    ])

        # compiling the neural network model
        model.compile(loss=tf.keras.losses.mse,
                    optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
                    # optimizer=tf.keras.optimizers.SGD(learning_rate=lr),
                    #   optimizer=tf.keras.optimizers.SGD(),
                    metrics=['mae','mse','accuracy'])

        history = model.fit(X_train, y_train, epochs=400)
        Histories.append(history)
        LR.append(lr)
        # preds = model.predict(X_test)
        # print('R score is :', r2_score(y_test, preds))
        # print(history.history.keys())

    # size of the plot
    plt.figure(figsize=(12, 6))
    colors = ["r", "g", "b", "m", "k", "c"]
    for ind,lr in enumerate(LR):
        plt.plot(Histories[ind].history['mae'], c=colors[ind], label=f"Learning rage {str(lr)}")
    # plt.plot(history.history['mse'])
    plt.title('Mean absolute error for different learning rates')
    plt.ylabel('MAE')
    plt.xlabel('epochs')
    plt.grid()
    plt.legend()
    # plt.show()

    a = float(model.layers[0].get_weights()[0][0])
    b = float(model.layers[0].get_weights()[0][1])
    c = float(model.layers[0].get_weights()[1][0])

    yp = a*X_square + b*X + c
    preds = model.predict(X_test)

    print(f"a predicted = {a}")
    print(f"a_exact = {a_exact}")
    print(f"b predicted = {b}")
    print(f"b_exact = {b_exact}")
    print(f"b predicted = {c}")
    print(f"b_exact = {c_exact}")

    # size of the plot
    plt.figure(figsize=(12, 6))
    plt.scatter(X_train[:,1], y_train, c="b", label="Train data")
    plt.scatter(X_test[:,1], y_test, c="g", label="Test set")
    plt.scatter(X_test[:,1], preds, c="r", label="Predictions")
    plt.plot(X, yp, c="k", label="Predicted model")
    plt.grid()
    plt.legend()
    plt.show()
