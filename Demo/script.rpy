# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("艾琳")
define s = Character('希尔维亚', color="#c8ffc8")
define m = Character('我', color="#c8c8ff")



# 游戏在此开始。

label start:
    
    play music "audio/bgm1.mp3"
    scene sc1
    s "嗨！今天的课怎么样？"

    m "挺好的……"

    "我当然不会承认，上课的时候内容只是左耳进右耳出。"

    m "你现在要回家了吗？要不要跟我一起走？"

    s "当然！"

    "这是一个renpy的测试"

    s "当然，不过，什么是\"视觉小说\"？"

menu:

    "是一种视频游戏。":
        jump game

    "是一种互动小说。":
        jump book

label game:

    m "是一种可以在电脑和主机上玩的视频游戏。"

    jump marry

label book:

    m "就像一种可以在电脑和主机上阅读的互动式图书。"

    jump marry

label marry:

    "那么，我们已经成为视觉小说创作二人组了。"

    return
