import matplotlib.pyplot as plt

def plot_result(y_test,y_pred):
  fig = plt.figure(figsize=(12, 8))
  gs = fig.add_gridspec(2,3)
  ax1 = fig.add_subplot(gs[0, 0])
  ax2 = fig.add_subplot(gs[0, 1])
  ax3 = fig.add_subplot(gs[0, 2])
  ax4 = fig.add_subplot(gs[1, 0])
  ax5 = fig.add_subplot(gs[1, 1])
  ax6 = fig.add_subplot(gs[1, 2])

  ax1.plot(y_test[:,0], y_pred[:,0], 'or')
  ax1.plot(y_test[:,0],y_test[:,0], 'b')
  ax1.set_title('correlacion C1')
  ax1.grid()

  ax2.plot(y_test[:,1], y_pred[:,1], 'or')
  ax2.plot(y_test[:,1],y_test[:,1], 'b')
  ax2.set_title('correlacion C2')
  ax2.grid()

  ax3.plot(y_test[:,2], y_pred[:,2], 'or')
  ax3.plot(y_test[:,2],y_test[:,2], 'b')
  ax3.set_title('correlacion C3')
  ax3.grid()

  ax4.plot(y_test[:,3], y_pred[:,3], 'or')
  ax4.plot(y_test[:,3],y_test[:,3], 'b')
  ax4.set_title('correlacion C4')
  ax4.grid()

  ax5.plot(y_test[:,4], y_pred[:,4], 'or')
  ax5.plot(y_test[:,4],y_test[:,4], 'b')
  ax5.set_title('correlacion C5')
  ax5.grid()

  ax6.plot(y_test[:,5], y_pred[:,5], 'or')
  ax6.plot(y_test[:,5],y_test[:,5], 'b')
  ax6.set_title('correlacion C6')
  ax6.grid()

  plt.show()