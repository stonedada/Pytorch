import matplotlib.pyplot as plt
import numpy as np

a = np.load("UTransform_train_loss_f-actin.npy", allow_pickle=True)
record = a.tolist()
# b = np.load('TransUNet_train_loss.npy', allow_pickle=True)
# record_1 = b.tolist()
# c = np.load('ResUNet_v3_train_loss.npy', allow_pickle=True)
# record_2 = c.tolist()
# d = np.load('TransUNet_train_loss (1).npy', allow_pickle=True)
# record_3 = d.tolist()

n_epochs = len(record)
plt.figure(figsize=(9, 5))
plt.plot(np.arange(1, n_epochs + 1), record, label='UTransform')
# plt.plot(np.arange(1, n_epochs + 1), record_3, label='TransUNet')
# plt.plot(np.arange(1, n_epochs + 1), record_1, label='TransUNet')
# plt.plot(np.arange(1, n_epochs + 1), record_2, label='ResUNet')

plt.legend()

plt.title('train_loss')
plt.xlabel('Epoch')
plt.ylabel('MAELoss')

dest = './train_loss_nuclei.png'
plt.savefig(dest)

plt.show()
