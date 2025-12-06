import keyword

def convert_source_file(input_path, output_path):
    # 读取原文件内容
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 获取Python保留字集合
    reserved_words = set(keyword.kwlist)
    result = []
    # 按单词拆分（简单处理，实际可优化分词逻辑）
    words = content.split()
    for word in words:
        if word in reserved_words:
            # 保留字不转换
            result.append(word)
        else:
            # 非保留字转为大写
            result.append(word.upper())
    # 拼接回字符串（保留空格分隔）
    converted_content = ' '.join(result)
    
    # 写入新文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(converted_content)

# 调用示例：处理random_int.py，输出到converted_random_int.py
convert_source_file('random_int.py', 'converted_random_int.py')
