from pydub import AudioSegment
import os

# 指定输入目录和输出文件名
input_directory = '/Users/chenjian/Desktop/思考的真相'
output_file = 'combined_audio.mp3'

# 获取输入目录中的所有音频文件
audio_files = [f for f in os.listdir(input_directory) if f.endswith('.m4a')]

# 初始化一个空的音频段列表
segments = []

# 遍历每个音频文件并加载到音频段列表中
for f in audio_files:
    audio = AudioSegment.from_file(os.path.join(input_directory, f))
    segments.append(audio)

# 合并所有音频段
combined = sum(segments)

# 导出合并后的音频文件
combined.export(output_file, format='mp3')
