print('欢迎使用“你帮我助”v1.0\n')

help = '使用说明：\n' \
       '输入“add”--在平台上添加物品信息\n' \
       '输入“delete”--根据物品名称+联系电话删除物品信息\n' \
       '输入“show”--打印在列表中的物品信息\n' \
       '输入“find”--根据物品名称查找物品\n' \
       '输入“help”--打印帮助\n' \
       '输入“quit”--结束程序\n'
print(help)

prompt = '\n请输入您希望进行的操作(quit可终止程序):'
choice = ''
while choice != 'Quit':
    choice = input(prompt)
    #choice = choice.replace(" ", "")
    
    if choice == 'add':    
         #goods=[]
         #addgoods=input('请输入您想要添加的物品')
         #goods.append(addgoods)
         goods = list(map(str, input('请输入您想要添加的物品').split(',')))
         print('您已添加成功')
         print(goods)

    elif choice == 'delete':
        print('现有以下物品'+str(goods))
        scgoods=input('请输入您想要删除的物品')
        goods.remove(scgoods)
        print('删除后物品还有：',goods)
        
    
    elif choice == 'find':
        czgoods=input('请输入您想要查找的物品：')
        goods.index(czgoods)

    elif choice == 'show':
        print('现在仓库内有以下物品')
        print(goods)
        
    elif choice == 'Help':
        print(help)
        
    elif choice == 'quit':
        continue
        
    else:
        print('您的输入不合规范(输入“Help”获取帮助)，请检查后重新输入，谢谢！')