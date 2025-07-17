from itertools import combinations

# 1. 将词条转换为Python字典格式
animal_data = {
    "会下蛋的动物": ["鳄霸", "地包天", "阿瓜", "阿呆", "木木", "柯蒂斯", "锤子", "咕咕", "布鲁斯", "阿宝", "豆豆", "泰雷斯", "哥斯拉", "扣扣", "糊涂", "瑞文"],
    "会潜水的动物": ["鳄霸", "瓦特", "阿瓜", "阿呆", "图斯卡尔", "锤子", "布鲁斯", "阿宝", "哈士企", "哥斯拉", "2662", "奥里", "扣扣", "巴巴拉"],
    "会飞的动物": ["阿瓜", "阿呆", "木木", "咕咕", "优罗莎", "暴莉", "阿宝", "瑞文", "2662", "糊涂"],
    "吃植物的动物": ["卡洛特", "培根", "芭比", "瓦力", "莫斯", "阿瓜", "阿呆", "柯蒂斯", "白菜狗", "咕咕", "优罗莎", "宝伯", "小新", "可乐", "高非", "奥姆诺姆", "豆豆", "福吉", "福宝", "坨坨", "巴巴拉"],
    "吃肉的动物": ["尼莫", "鳄霸", "地包天", "玛奇朵", "瓦特", "泰哥", "斯帕奇", "图斯卡尔", "八公", "加肥", "珞珞", "木木", "毛毛", "麦克斯", "锤子", "利威尔", "布鲁斯", "希子", "卡托", "雪诺", "嘟嘟", "刺头", "桑尼", "玛奈奇", "山姆", "哈士企", "苗苗", "星期天", "罗恩", "斯黛拉", "扣扣", "妙妙", "瑞文", "狐狸Vicksy", "糊涂"],
    "头上长角的动物": ["地包天", "瓦力", "莫斯", "柯蒂斯", "暴莉", "咩咩", "阿宝"],
    "尾巴长的动物": ["鳄霸", "地包天", "玛奇朵", "泰哥", "斯帕奇", "八公", "加肥", "珞珞", "毛毛", "麦克斯", "柯蒂斯", "锤子", "利威尔", "咕咕", "布鲁斯", "奥里", "希子", "卡托", "雪诺", "嘟嘟", "阿宝", "玛奈奇", "山姆", "福吉", "苗苗", "星期天", "坨坨", "狐狸Vicksy", "妙妙"],
    "毛茸茸的动物": ["尼莫", "玛奇朵", "卡洛特", "瓦特", "泰哥", "芭比", "瓦力", "莫斯", "八公", "加肥", "珞珞", "毛毛", "麦克斯", "利威尔", "希子", "卡托", "宝伯", "咩咩", "雪诺", "嘟嘟", "刺头", "可乐", "阿宝", "高非", "玛奈奇", "山姆", "福吉", "福宝", "哈士企", "苗苗", "星期天", "罗恩", "斯黛拉", "坨坨", "狐狸Vicksy", "妙妙", "扣扣", "巴巴拉", "瑞文"],
    "犬科动物": ["尼莫", "斯帕奇", "八公", "珞珞", "毛毛", "麦克斯", "卡托", "雪诺", "桑尼", "山姆", "哈士企", "罗恩", "斯黛拉", "狐狸Vicksy"],
    "猫科动物": ["玛奇朵", "泰哥", "加肥", "利威尔", "希子", "嘟嘟", "玛奈奇", "苗苗", "星期天", "妙妙"],
    "眼睛大的动物": ["鳄霸", "地包天", "阿瓜", "木木", "柯蒂斯", "咕咕", "奥里", "咩咩", "嘟嘟", "阿宝", "奥姆诺姆", "豆豆", "哈士企", "2662", "瑞文", "Vicksy", "糊涂", "坨坨"]
}

def find_intersection(categories_to_check):
    """计算给定分类列表的交集"""
    if not categories_to_check:
        return set()
    
    # 将动物列表转换为集合以便进行交集运算
    animal_sets = [set(animal_data.get(cat, [])) for cat in categories_to_check]
    
    # 从第一个集合开始，依次与其他集合求交集
    intersection_result = animal_sets[0]
    for animal_set in animal_sets[1:]:
        intersection_result.intersection_update(animal_set)
        
    return intersection_result

def main():
    """主函数，处理用户交互"""
    categories_list = list(animal_data.keys())
    
    print("欢迎使用动物分类器！")
    print("="*30)
    
    while True:
        print("\n可用的动物分类：")
        for i, cat in enumerate(categories_list):
            print(f"  {i + 1}. {cat}")
        
        print("\n请输入您想选择的分类编号（用空格或逗号隔开），或输入 'q' 退出：")
        
        try:
            user_input = input("> ").strip()
            
            if user_input.lower() == 'q':
                print("感谢使用，再见！")
                break

            if not user_input:
                continue

            # 解析用户输入
            raw_indices = user_input.replace(',', ' ').split()
            selected_indices = [int(i) - 1 for i in raw_indices]
            
            selected_categories = []
            valid = True
            for i in selected_indices:
                if 0 <= i < len(categories_list):
                    selected_categories.append(categories_list[i])
                else:
                    print(f"错误：编号 {i + 1} 无效，请重新输入。")
                    valid = False
                    break
            
            if not valid or not selected_categories:
                continue

            print("\n--- 查询结果 ---")
            found_any_result = False
            # 从选择的分类数量开始，递减计算所有组合的交集
            for i in range(len(selected_categories), 0, -1):
                for combo in combinations(selected_categories, i):
                    intersection = find_intersection(list(combo))
                    if intersection:
                        found_any_result = True
                        # 组合标题，例如："毛茸茸的猫科动物"
                        title = "".join(c.replace("的动物", "") for c in combo) + "的动物"
                        animals = "、".join(sorted(list(intersection)))
                        print(f"\n{title}:")
                        print(f"  {animals}")
            
            if not found_any_result:
                print("\n在所选分类的任何组合中都找不到共同的动物。")
            
            print("\n" + "="*30)

        except ValueError:
            print("输入无效，请输入数字编号。")
        except KeyboardInterrupt:
            print("\n程序退出。")
            break
        except Exception as e:
            print(f"发生未知错误: {e}")

if __name__ == "__main__":
    main()