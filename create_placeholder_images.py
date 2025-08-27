import os
import shutil

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 设置源文件和目标目录
source_file = os.path.join(current_dir, 'project-images', 'placeholder-profile.jpg')  # 使用现有的占位图片作为源文件
target_dir = os.path.join(current_dir, 'project-images', 'article')

# 确保目标目录存在
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 删除现有的文章封面图片文件，以便重新创建
for i in range(1, 5):
    old_file = os.path.join(target_dir, f'{i}.jpg')
    if os.path.exists(old_file):
        os.remove(old_file)

# 删除之前创建的带有描述性名称的图片
old_image_names = [
    'design-thinking-nature.jpg',
    'ai-design-role.jpg',
    'creative-thinking.jpg',
    'minimalism-design.jpg'
]
for old_name in old_image_names:
    old_file = os.path.join(target_dir, old_name)
    if os.path.exists(old_file):
        os.remove(old_file)

# 使用简单的命名规则创建文章封面占位图片（1.jpg到4.jpg）
for i in range(1, 5):
    target_file = os.path.join(target_dir, f'{i}.jpg')
    if os.path.exists(source_file):
        shutil.copy2(source_file, target_file)
        print(f'已创建: {target_file}')
    else:
        print(f'警告: 源文件 {source_file} 不存在，无法创建 {target_file}')

print('文章页面所需的4个封面占位图片（1.jpg到4.jpg）已创建完成')