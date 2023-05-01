import matplotlib.pyplot as plt
import numpy as np

a = np.load("UTransform_train_loss_nuclei.npy", allow_pickle=True)
record = a.tolist()
b = np.load('ResUNet_train_loss_nuclei.npy', allow_pickle=True)
record_1 = b.tolist()
c = np.load('TransUNet_train_loss_nuclei.npy', allow_pickle=True)
record_2 = c.tolist()

n_epochs = len(record)
plt.figure(figsize=(9, 5))
plt.plot(np.arange(1, n_epochs + 1), record, label='UTransform')
plt.plot(np.arange(1, n_epochs + 1), record_1, label='ResUNet')
plt.plot(np.arange(1, n_epochs + 1), record_2, label='TransUNet')
plt.legend()

plt.title('train_loss')
plt.xlabel('Epoch')
plt.ylabel('MAELoss')

dest = './train_loss_nuclei_v2.png'
plt.savefig(dest)

plt.show()
