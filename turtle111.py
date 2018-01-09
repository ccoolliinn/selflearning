import turtle
# 控制画笔颜色
turtle.pencolor('red')
# 落笔
turtle.pendown()
# 设置填充颜色
turtle.fillcolor('blue')
# 开始填充
turtle.begin_fill()
# 从原点开始，画出一个边长为100的正方形
for i in range(4):
    # 正向运动 100 的距离
    turtle.forward(200)
    # 向右偏 90 度
    turtle.right(90)
    # 结束填充
turtle.end_fill()
turtle.penup()
turtle.goto(100,-100)
turtle.write('Crossin编程教室')