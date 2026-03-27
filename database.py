import json
import random

# 假设这是你原始的10条数据（请替换成你真实的数据）
original_data = [
    {"text": "我喜欢吃苹果"},
    {"text": "今天天气真好"},
    {"text": "机器学习很有趣"},
    {"text": "Python编程很简单"},
    {"text": "这本书值得一读"},
    {"text": "运动让人健康"},
    {"text": "音乐能放松心情"},
    {"text": "旅行可以开阔眼界"},
    {"text": "朋友之间要互相尊重"},
    {"text": "学习需要持之以恒"}
]

# 定义同义词和替换词（针对你的数据特点定制）
synonyms = {
    "喜欢": ["喜爱", "爱", "钟爱", "热衷于"],
    "吃": ["品尝", "享用", "啃", "食用"],
    "苹果": ["香蕉", "橘子", "草莓", "西瓜", "水果"],
    "今天": ["此刻", "当下", "今日", "现在"],
    "天气": ["气候", "天色", "气象"],
    "真好": ["很棒", "不错", "宜人", "舒适"],
    "机器学习": ["深度学习", "人工智能", "神经网络", "算法"],
    "有趣": ["好玩", "有意思", "充满乐趣", "吸引人"],
    "Python": ["编程", "代码", "软件开发", "计算机语言"],
    "编程": ["写代码", "开发", "编码", "程序设计"],
    "简单": ["容易", "轻松", "不复杂", "上手快"],
    "这本书": ["这部作品", "这本小说", "这篇文章", "这个内容"],
    "值得一读": ["推荐观看", "值得品味", "很有价值", "不容错过"],
    "运动": ["锻炼", "健身", "体育活动", "跑步"],
    "健康": ["强壮", "有活力", "身体好", "精力充沛"],
    "音乐": ["歌曲", "旋律", "乐章", "乐曲"],
    "放松": ["舒缓", "减压", "平静", "治愈"],
    "旅行": ["出游", "远足", "观光", "探索世界"],
    "开阔眼界": ["增长见识", "拓展视野", "丰富阅历", "看到更多"],
    "朋友": ["伙伴", "同伴", "知己", "好友"],
    "互相尊重": ["彼此理解", "相互包容", "友好相处", "真诚相待"],
    "学习": ["求知", "钻研", "进步", "提升自我"],
    "需要": ["必须", "应当", "离不开", "依赖于"],
    "持之以恒": ["坚持不懈", "锲而不舍", "始终如一", "长期坚持"]
}

# 句式变换模板（让数据更丰富）
templates = [
    "我{verb}{object}",
    "我非常{verb}{object}",
    "{object}让我感到{feeling}",
    "我觉得{object}很{adjective}",
    "最近我开始{verb}{object}",
    "对于{object}，我{verb}",
    "{time}，我{verb}{object}"
]

template_params = {
    "verb": ["喜欢", "爱", "享受", "热衷于", "沉迷于"],
    "object": ["学习", "运动", "音乐", "旅行", "阅读", "编程"],
    "feeling": ["快乐", "满足", "充实", "放松", "兴奋"],
    "adjective": ["有趣", "有意义", "有价值", "轻松", "愉快"],
    "time": ["最近", "平时", "空闲时", "周末", "每天"]
}

def augment_with_synonyms(text):
    """通过同义词替换生成新数据"""
    new_text = text
    # 随机选择3-5个词进行替换
    words_to_replace = random.sample(list(synonyms.keys()), random.randint(2, 4))
    for word in words_to_replace:
        if word in text and random.random() > 0.3:  # 70%概率替换
            synonym = random.choice(synonyms[word])
            new_text = new_text.replace(word, synonym, 1)
    return new_text

def augment_with_templates():
    """通过句式模板生成新数据"""
    template = random.choice(templates)
    filled_template = template
    for key, values in template_params.items():
        if f"{{{key}}}" in template:
            filled_template = filled_template.replace(f"{{{key}}}", random.choice(values))
    return filled_template

# 生成增强数据
augmented_dataset = []

# 1. 加入原始数据
for item in original_data:
    augmented_dataset.append(item)

# 2. 同义词替换（每条原始数据生成10个变体）
for item in original_data:
    for _ in range(10):
        new_text = augment_with_synonyms(item['text'])
        if new_text != item['text']:  # 确保生成了不同的内容
            augmented_dataset.append({"text": new_text})

# 3. 句式模板生成（生成50条全新数据）
for _ in range(50):
    new_text = augment_with_templates()
    augmented_dataset.append({"text": new_text})

# 4. 随机打乱数据
random.shuffle(augmented_dataset)

# 5. 保存数据
with open('pretrain.jsonl', 'w', encoding='utf-8') as f:
    for item in augmented_dataset:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')

print(f"原始数据量: {len(original_data)}")
print(f"增强后数据量: {len(augmented_dataset)}")
print("数据增强完成！新数据已保存到 pretrain.jsonl")

# 打印前5条增强数据示例
print("\n增强数据示例：")
for i, item in enumerate(augmented_dataset[:5]):
    print(f"{i+1}. {item['text']}")