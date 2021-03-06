from matplotlib import pyplot as plt
from base_model import history


# TODO: plotting code refactor, simplify in loop
def plot_metrics():
    plt.figure(1, figsize=(15, 5))
    plt.suptitle('FFN Metric Plots', fontsize=16)
    plt.subplot(321)
    plt.plot(history.history['loss'], label='loss')
    plt.ylim([0, 0.00001])
    plt.ylim([0, 0.00001])
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.legend()
    plt.grid(True)
    plt.subplot(322)
    plt.plot(history.history['val_loss'], label='val_loss')
    plt.ylim([0, 0.00001])
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.legend()
    plt.grid(True)
    plt.subplot(323)
    plt.plot(history.history['cosine_similarity'], label='cosine_similarity')
    plt.ylim([.9991, 1.0001])
    plt.xlabel('Epoch')
    plt.ylabel('Similarity')
    plt.legend()
    plt.grid(True)    
    plt.subplot(324)
    plt.plot(history.history['val_cosine_similarity'], label='val_cosine_similarity')
    plt.ylim([.9991, 1.0001])
    plt.xlabel('Epoch')
    plt.ylabel('Similarity')
    plt.legend()
    plt.grid(True)
    plt.subplot(325)
    plt.plot(history.history['hinge'], label='hinge')
    plt.ylim([.851, .852])
    plt.xlabel('Epoch')
    plt.ylabel('Hinge')
    plt.legend()
    plt.grid(True)
    plt.subplot(326)
    plt.plot(history.history['val_hinge'], label='val_hinge')
    plt.ylim([.851, .852])
    plt.xlabel('Epoch')
    plt.ylabel('Hinge')
    plt.legend()
    plt.grid(True)
    return plt


if __name__ == '__main__':
    plot_metrics().savefig('metrics_plots.png')
    plot_metrics().show()
