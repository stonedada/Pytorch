import matplotlib.pyplot as plt
import numpy as np

a = np.load("UTransform_train_loss.npy", allow_pickle=True)
record = a.tolist()
b = np.load('TransFuse_train_loss.npy', allow_pickle=True)
record_1 = b.tolist()
c = np.load('ResUNet_v3_train_loss.npy', allow_pickle=True)
record_2 = c.tolist()
d = np.load('TransUNet_train_loss (1).npy', allow_pickle=True)
record_3 = d.tolist()
e = np.load('STNet_train_loss_F-actin (1).npy', allow_pickle=True)
record_4 = e.tolist()

n_epochs = len(record)
plt.figure(figsize=(9, 5))
plt.plot(np.arange(1, n_epochs + 1), record, label='UTransformer')
plt.plot(np.arange(1, n_epochs + 1), record_3, label='TransUNet')
plt.plot(np.arange(1, n_epochs + 1), record_1, label='TransFuse')
plt.plot(np.arange(1, n_epochs + 1), record_2, label='ResUNet')
plt.plot(np.arange(1, n_epochs + 1), record_4, label='STNet')

plt.legend()

plt.title('Losses Model')
plt.xlabel('Epochs')
plt.ylabel('Loss for Each Epoch')
dest = './train_loss_v5.png'
plt.savefig(dest)

plt.show()
