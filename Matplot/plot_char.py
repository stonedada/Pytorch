import matplotlib.pyplot as plt
import numpy as np

a = np.load("./ResUNet_train_loss.npy", allow_pickle=True)
record = a.tolist()
b = np.load('./ResUNet_v2_train_loss.npy', allow_pickle=True)
record_1 = b.tolist()

n_epochs = len(record)
plt.figure(figsize=(9, 5))
plt.plot(np.arange(1, n_epochs + 1), record, label='ResUNnet')
plt.plot(np.arange(1, n_epochs + 1), record_1, label='ResUNet_v2')
plt.legend()

plt.title('train_loss')
plt.xlabel('Epoch')
plt.ylabel('MAELoss')

plt.show()
