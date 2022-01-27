from PIL import Image

n = [20, 8, 9, 8, 5, 3, 12]
name = ['Stand_', 'go_', 'jump_', 'attack_', 'None', 'loss', 'win']
y = [0, 65, 133, 235, 301, 369, 430, 496]
x = [0, 59, 77.5, 77.8, 84.4, 62, 86.7, 84]
i = 312

# for i in range(len(n)):
for k in range(n[i]+1):
    image = Image.open('../pic/Miku1.png')
    cropped = image.crop((k*x[i+1], y[i], k*x[i+1]+x[i+1], y[i]+y[i+1]-y[i]))
    cropped = cropped.transpose(Image.FLIP_LEFT_RIGHT)
    cropped.save('../res/' + name[i] + str(k) + '.png')