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
    X = np.arange(-210, 210, 3)
    a_exact = 3
    b_exact = 100
    print(X.shape)
    y = a_exact*X + b_exact + 400*np.random.rand(X.size)


    # size of the plot
    plt.figure(figsize=(12, 6))
    plt.scatter(X, y, c="r", label="Exact model")
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()


    # Splitting training and test data
    X_train = X[:110]
    y_train = y[:110]
    X_test = X[110:]
    y_test = y[110:]


    # size of the plot
    plt.figure(figsize=(12, 6))
    plt.scatter(X_train, y_train, c="r", label="Train data")
    plt.scatter(X_test, y_test, c="b", label="Test data")
    plt.grid()
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

    # Model
    Histories = []
    LR = []
    LR_sgd = [0.01, 0.02]
    LR_adam = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5]
    # LR_adam = [0.1]
    LR_set = LR_adam
    for lr in LR_set:
        model = tf.keras.Sequential([tf.keras.layers.InputLayer(input_shape=1,),
                                    tf.keras.layers.Dense(1)
                                    ])

        # compiling the neural network model
        model.compile(loss=tf.keras.losses.mse,
                    optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
                    # optimizer=tf.keras.optimizers.SGD(learning_rate=lr),
                    #   optimizer=tf.keras.optimizers.SGD(),
                    metrics=['mae','mse','accuracy'])

        history = model.fit(tf.expand_dims(X_train, axis=-1), y_train, epochs=800)
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

    a = float(model.layers[0].get_weights()[0])
    b = float(model.layers[0].get_weights()[1])

    yp = a*X + b
    preds = model.predict(X_test)

    print(f"a predicted = {a}")
    print(f"a_exact = {a_exact}")
    print(f"b predicted = {b}")
    print(f"b_exact = {b_exact}")

    # size of the plot
    plt.figure(figsize=(12, 6))
    plt.scatter(X_train, y_train, c="b", label="Train data")
    plt.scatter(X_test, y_test, c="g", label="Test set")
    plt.scatter(X_test, preds, c="r", label="Predictions")
    plt.plot(X, yp, c="k", label="Predicted model")
    # plt.plot(X, y, c="k", label="Exact model")
    plt.grid()
    plt.legend()
    plt.show()

    # -------------------------------------------------------------------------------------------
    # # initializing the tunner 
    # tuner = kt.Hyperband(model_builder,
    #                     objective='val_loss',
    #                     max_epochs=200,
    #                     )

    # # Early stopping in keras
    # stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience = 4)

    # # Seaching the tunner 
    # tuner.search(X, y, validation_split=0.2, callbacks=[stop_early])
    # # Get the optimal hyperparameters
    # best_hps=tuner.get_best_hyperparameters(num_trials=1)[0]
    # # creating model with the optimum parameters
    # model = tuner.hypermodel.build(best_hps)
    # # fixed max max epohcs to 300
    # Training_model = model.fit(X, y, epochs=200, validation_split=0.2)
    # # val_loss 
    # val_acc_per_epoch = Training_model.history['val_loss']
    # # printing optimum eppoc
    # best_epoch = val_acc_per_epoch.index(max(val_acc_per_epoch)) + 1
    # print('Best epoch:',  best_epoch)
    # # printing the optimal number of nodes 
    # print('The optimal number of node in the hidden layer is: ', best_hps.get('units'))

    # plt.figure()
    # plt.plot(Training_model.history['val_loss'])
    # plt.title('model val_loss')
    # plt.ylabel('val_loss')
    # plt.xlabel('epoch')
    # plt.legend(['train','validate'], loc='upper left')
    # plt.show()