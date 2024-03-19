import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

#--------------------------------------------------
# fig, ax = plt.subplots() #Create a figure containing a single axes.
# ax.plot([1,2,3,4], [1,4,3,4])
# plt.show()


#--------------------------------------------------
# fig, ax = plt.subplots(figsize=(2, 2), facecolor='lightskyblue',
#                        layout='constrained')
# fig.suptitle('Figure')
# ax.set_title('Axes', loc='left', fontstyle='oblique', fontsize='medium')
# ax.plot(["Hola", "Saludos","Adios"], [6, 1, 3])
# # plt.show()

#--------------------------------------------------

# fig, axs = plt.subplot_mosaic([['A', 'right'], ['B', 'right']],
#                               figsize=(4, 3), layout='constrained')
# for ax_name, ax in axs.items():
#     ax.text(0.5, 0.5, ax_name, ha='center', va='center')
# plt.show()

#--------------------------------------------------
# plt.subplot(1,2,1)
# ax = plt.gca()
# ax.plot([1,2,3], [0,0.5,0.2])

# plt.subplot(1, 2, 2)
# ax = plt.gca()
# ax.plot([3, 2, 1], [0, 0.5, 0.2])
# plt.show()
#--------------------------------------------------

# plt.style.use('_mpl-gallery')

# # make data:
# x = 0.5 + np.arange(8)
# y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

# # plot
# fig, ax = plt.subplots()

# ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#     ylim=(0, 8), yticks=np.arange(1, 8))

# plt.show()
#--------------------------------------------------

df = pd.read_csv('revisionTarea7\\fernanda\\1989_db_csv.csv')
df.plot()
plt.show()

#-----------------------------------------------------------------
df = pd.read_csv('revisionTarea7\\fernanda\\1989_db_csv.csv')

ax = df.plot.bar(x='song_title', y='song_page_views', rot=0)
ax.set_title("Taylor Swift Songs")
ax.set_xlabel("Songs")
ax.set_ylabel("Listenings")

plt.show()
# songs = df.plot.bar(x='song_title', rot=0)

# fig, ax = plt.subplots()
# ax.plot(df['song_title'], df['song_page_views'])
# ax.bar(df['song_title'], df['song_page_views'])

