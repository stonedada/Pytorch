import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.gridspec as gridspec

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def PCC():
    y_axis_data1 = [0.820, 0.849, 0.845, 0.819, 0.864, ]
    y_axis_data2 = [0.859, 0.857, 0.857, 0.850, 0.869, ]
    y_axis_data3 = [0.662, 0.696, 0.679, 0.683, 0.699, ]
    y_axis_data4 = [0.702, 0.683, 0.705, 0.693, 0.736, ]
    y_axis_data5 = [0.641, 0.688, 0.696, 0.648, 0.705, ]
    return y_axis_data1,y_axis_data2,y_axis_data3,y_axis_data4,y_axis_data5


def R2Score():
    y_axis_data1 = [0.669,0.720,0.709,0.646,0.747]
    y_axis_data2 = [0.734,0.733,0.728,0.689,0.755]
    y_axis_data3 = [0.434,0.480,0.451,0.466,0.488]
    y_axis_data4 = [0.488,0.465,0.483,0.468,0.524]
    y_axis_data5 = [0.411,0.464,0.461,0.392,0.485]
    return y_axis_data1,y_axis_data2,y_axis_data3,y_axis_data4,y_axis_data5


def MAE():
    y_axis_data1 = [0.412,0.355,0.365,0.439,0.342]
    y_axis_data2 = [0.248,0.247,0.246,0.302,0.229]
    y_axis_data3 = [0.506,0.490,0.492,0.512,0.486]
    y_axis_data4 = [0.595,0.592,0.582,0.591,0.549]
    y_axis_data5 = [0.626,0.588,0.592,0.631,0.577]
    return y_axis_data1,y_axis_data2,y_axis_data3,y_axis_data4,y_axis_data5

def SSIM():
    y_axis_data1 = [0.693,0.734,0.736,0.655,0.766,]
    y_axis_data2 = [0.729,0.749,0.819,0.746,0.826]
    y_axis_data3 = [0.519,0.571,0.585,0.557,0.584]
    y_axis_data4 = [0.406,0.403,0.352,0.378,0.404,]
    y_axis_data5 = [0.490,0.500,0.511,0.435,0.526]
    return y_axis_data1,y_axis_data2,y_axis_data3,y_axis_data4,y_axis_data5

def main():
    plt.figure(figsize=(40, 21))
    gs = gridspec.GridSpec(2, 4)  # 创立2 * 6 网格
    gs.update(wspace=0.8)
    my_line=5
    my_alpha=1
    my_font=28
    plt.subplot(gs[0, :2],)

    y_axis_data1,y_axis_data2,y_axis_data3,y_axis_data4,y_axis_data5=PCC()
    # epoch,acc,loss,val_acc,val_loss
    x_axis_data = ["3DConvCaps","3DUnet","3DTransUnet","3D-UCaps","3DCellCapUnet "]

    # 画图
    plt.plot(x_axis_data, y_axis_data1, 'b*-', alpha=my_alpha, linewidth=my_line, label='Nuclear Membrane',markersize=my_line+8)  #
    plt.plot(x_axis_data, y_axis_data2, 'rp:', alpha=my_alpha, linewidth=my_line, label='Nucleoli ',markersize=my_line+8)
    plt.plot(x_axis_data, y_axis_data3, 'go-.', color='limegreen',alpha=my_alpha, linewidth=my_line, label='Mitochondria ',markersize=my_line+8)
    plt.plot(x_axis_data, y_axis_data4, 'y^:',color='orange', alpha=my_alpha, linewidth=my_line, label='Actin Filament  ',markersize=my_line+8)
    plt.plot(x_axis_data, y_axis_data5, 'ms-',color='deeppink', alpha=my_alpha, linewidth=my_line, label='DNA+ ',markersize=my_line+8)
    plt.ylabel('Pearson Correlation Coefficient', fontsize=my_font)
    #plt.legend()  # 显示上面的label
    plt.xticks(fontsize=my_font - 2)
    plt.yticks(fontsize=my_font - 2)
    plt.legend(fontsize=my_font - 5)
    plt.ylim(0.47, 0.9)  # 仅设置y轴坐标范围

    plt.rcParams['axes.labelpad'] = 10
    plt.subplot(gs[0, 2:4], )
    y_axis_data1,y_axis_data2,y_axis_data3,y_axis_data4,y_axis_data5=R2Score()
    # epoch,acc,loss,val_acc,val_loss
    x_axis_data = [" 3DConvCaps","3DUnet","3DTransUnet","3D-UCaps","3DCellCapUnet "]

    # 画图
    plt.plot(x_axis_data, y_axis_data1, 'b*-', alpha=my_alpha, linewidth=my_line, label='Nuclear Membrane',markersize=my_line+8)  #
    plt.plot(x_axis_data, y_axis_data2, 'rp:', alpha=my_alpha, linewidth=my_line, label='Nucleoli ',markersize=my_line+8)
    plt.plot(x_axis_data, y_axis_data3, 'go-.', color='limegreen',alpha=my_alpha, linewidth=my_line, label='Mitochondria ',markersize=my_line+8)
    plt.plot(x_axis_data, y_axis_data4, 'y^:',color='orange', alpha=my_alpha, linewidth=my_line, label='Actin Filament  ',markersize=my_line+8)
    plt.plot(x_axis_data, y_axis_data5, 'ms-', color='deeppink', alpha=my_alpha, linewidth=my_line, label='DNA+ ',markersize=my_line+8)

    #plt.legend(fontsize=my_font)  # 显示上面的label
    plt.xticks(fontsize=my_font - 2)
    plt.yticks(fontsize=my_font - 2)
    plt.ylabel('R2score', fontsize=my_font)
    plt.ylim(0.15,0.78)#仅设置y轴坐标范围
    plt.legend(fontsize=my_font - 5)

    plt.subplot(gs[1, 0:2])
    y_axis_data1,y_axis_data2,y_axis_data3,y_axis_data4,y_axis_data5=SSIM()
    # epoch,acc,loss,val_acc,val_loss
    x_axis_data = ["3DConvCaps","3DUnet","3DTransUnet","3D-UCaps","3DCellCapUnet "]

    # 画图
    plt.plot(x_axis_data, y_axis_data1, 'b*-', alpha=my_alpha, linewidth=my_line, label='Nuclear Membrane',markersize=my_line+8)  #
    plt.plot(x_axis_data, y_axis_data2, 'rp:', alpha=my_alpha, linewidth=my_line, label='Nucleoli ',markersize=my_line+8)
    plt.plot(x_axis_data, y_axis_data3, 'go-.',color='limegreen', alpha=my_alpha, linewidth=my_line, label='Mitochondria ',markersize=my_line+8)
    plt.plot(x_axis_data, y_axis_data4, 'y^:',color='orange', alpha=my_alpha, linewidth=my_line, label='Actin Filament  ',markersize=my_line+8)
    plt.plot(x_axis_data, y_axis_data5, 'ms-', color='deeppink',alpha=my_alpha, linewidth=my_line, label='DNA+ ',markersize=my_line+8)

    #plt.legend(fontsize=my_font)  # 显示上面的label
    plt.xticks(fontsize=my_font - 2)
    plt.yticks(fontsize=my_font - 2)
    plt.ylabel('Structural Similarity', fontsize=my_font)
    # plt.ylim(-1,1)#仅设置y轴坐标范围
    plt.legend(fontsize=my_font - 5)
    plt.ylim(0.15, 0.85)
    plt.subplot(gs[1, 2:4])
    y_axis_data1,y_axis_data2,y_axis_data3,y_axis_data4,y_axis_data5=MAE()
    # epoch,acc,loss,val_acc,val_loss
    x_axis_data = ["3DConvCaps","3DUnet","3DTransUnet","3D-UCaps","3DCellCapUnet "]

    # 画图
    plt.plot(x_axis_data, y_axis_data1, 'b*-', alpha=0.5, linewidth=my_line, label='Nuclear Membrane',markersize=my_line+8)  #
    plt.plot(x_axis_data, y_axis_data2, 'rp:', alpha=0.5, linewidth=my_line, label='Nucleoli ',markersize=my_line+8)
    plt.plot(x_axis_data, y_axis_data3, 'go-.', color='limegreen',alpha=0.5, linewidth=my_line, label='Mitochondria ',markersize=my_line+8)
    plt.plot(x_axis_data, y_axis_data4, 'y^:',color='orange', alpha=0.5, linewidth=my_line, label='Actin Filament  ',markersize=my_line+8)
    plt.plot(x_axis_data, y_axis_data5, 'ms-', color='deeppink',alpha=0.5, linewidth=my_line, label='DNA+ ',markersize=my_line+8)

    #plt.legend(fontsize=my_font)  # 显示上面的label
    plt.ylim(0.05, 0.65)
    plt.ylabel('Mean Square Error', fontsize=my_font)
    plt.xticks(fontsize=my_font-2)
    plt.yticks(fontsize=my_font-2)
    # plt.ylim(-1,1)#仅设置y轴坐标范围
    plt.legend(fontsize=my_font - 5)
    plt.savefig('a.png')
    plt.show()






if __name__ == '__main__':
    main()


